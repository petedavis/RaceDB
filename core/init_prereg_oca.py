import sys
import datetime
from xlrd import open_workbook, xldate_as_tuple
import HTMLParser
from collections import namedtuple
from models import *
from django.db import transaction, IntegrityError
from django.db.models import Q

datemode = None

today = datetime.date.today()
earliest_year = (today - datetime.timedelta( days=106*365 )).year
latest_year = (today - datetime.timedelta( days=7*365 )).year

def date_from_value( s ):
	if isinstance(s, datetime.date):
		return s
	if isinstance(s, (float, int)):
		return datetime.date( *(xldate_as_tuple(s, datemode)[:3]) )
	
	# Assume month, day, year format.
	mm, dd, yy = [int(v.strip()) for v in s.split( '/' )]
	
	# Correct for 2-digit year.
	for century in [0, 1900, 2000, 2100]:
		if earliest_year <= yy + century <= latest_year:
			yy += century
			break
	
	# Check if day and month are reversed.
	if mm > 12:
		dd, mm = mm, dd
		
	assert 1900 <= yy
		
	try:
		return datetime.date( year = yy, month = mm, day = dd )
	except Exception as e:
		print yy, mm, dd
		raise e
		
def gender_from_str( s ):
	return 0 if s.lower().strip().startswith('m') else 1

def set_attributes( obj, attributes ):
	changed = False
	for key, value in attributes.iteritems():
		if getattr(obj, key) != value:
			setattr(obj, key, value)
			changed = True
	return changed
	
def large_delete_all( Object ):
	while Object.objects.count():
		with transaction.atomic():
			ids = Object.objects.values_list('pk', flat=True)[:999]
			Object.objects.filter(pk__in = ids).delete()

def to_int_str( v ):
	try:
		return unicode(long(v))
	except:
		pass
	return unicode(v)
		
def to_str( v ):
	if v is None:
		return v
	return unicode(v)
	
def to_bool( v ):
	if v is None:
		return None
	s = unicode(v)
	return s[:1] in 'YyTt1'

def to_int( v ):
	if v is None:
		return None
	try:
		return int(v)
	except:
		return None
		
def to_tag( v ):
	if v is None:
		return None
	return unicode(v).split('.')[0]

def init_prereg_oca( competition_name, worksheet_name, clear_existing ):
	global datemode
	
	tstart = datetime.datetime.now()
	
	html_parser = HTMLParser.HTMLParser()

	try:
		competition = Competition.objects.get( name=competition_name )
	except Competition.DoesNotExist:
		print( u'Cannot find Competition: "{}"'.format(competition_name) )
		return
	except Competition.MultipleObjectsReturned:
		print( u'Found multiple Competitions matching: "{}"'.format(competition_name) )
		return
	
	if clear_existing:
		Participant.objects.filter(competition=competition).delete()
	
	# Process the records in large transactions for efficiency.
	@transaction.atomic
	def process_ur_records( ur_records ):
		
		for i, ur in ur_records:
			bib				= to_int(ur.get('bibnum', None))
			license_code	= 'ON' + (to_int_str(ur.get('license','')) or to_int_str(ur.get('licence','<missing license code>')))
			name			= to_str(ur.get('name','')).strip()
			team_name		= to_str(ur.get('Team', None))
			preregistered	= to_bool(ur.get('preregistered', True))
			paid			= to_bool(ur.get('paid', None))
			category_code   = to_str(ur.get('category', None))

			try:
				license_holder = LicenseHolder.objects.get( license_code=license_code )
			except LicenseHolder.DoesNotExist:
				print( u'Row {}: cannot find LicenceHolder from LicenseCode: {}'.format(i, license_code) )
				continue
			
			try:
				participant = Participant.objects.get( competition=competition, license_holder=license_holder )
			except Participant.DoesNotExist:
				participant = Participant( competition=competition, license_holder=license_holder )
			except Participant.MultipleObjectsReturned:
				print( u'Row {}: found multiple Participants for this competition and license_holder.'.format(
						i,
				) )
				continue
			
			for attr, value in [ ('preregistered',preregistered), ('paid',paid), ('bib',bib), ]:
				if value is not None:
					setattr( participant, attr, value )
			
			team = None
			if team_name is not None:
				try:
					team = Team.objects.get(name=team_name)
				except Team.DoesNotExist:
					print( u'Row {}: unrecognized Team name (ignoring): "{}"'.format(
						i, team_name,
					) )
				except Team.MultipleObjectsReturned:
					print( u'Row {}: multiple Teams match name (ignoring): "{}"'.format(
						i, team_name,
					) )
			participant.team = team
			
			category = None
			if category_code is not None:
				try:
					category = Category.objects.get( format=competition.category_format, code=category_code )
				except Category.DoesNotExist:
					print( u'Row {}: unrecognized Category code (ignoring): "{}"'.format(
						i, category_code,
					) )
				except Category.MultipleObjectsReturned:
					print( u'Row {}: multiple Categories match code (ignoring): "{}"'.format(
						i, category_code,
					) )
			participant.category = category
			
			try:
				participant.save()
			except IntegrityError as e:
				print( u'Row {}: Error={}\nBib={} Category={} License={} Name={}'.format(
					i, e,
					bib, category_code, license_code, name,
				) )
				continue
			
			print u'{:>6}: {:>8} {:>10} {}, {}, {}, {}'.format( i, license_holder.license_code, license_holder.date_of_birth.strftime('%Y/%m/%d'), license_holder.uci_code, license_holder.last_name, license_holder.first_name, license_holder.city, license_holder.state_prov )
	
	try:
		fname, sheet_name = worksheet_name.split('$')
	except:
		fname = worksheet_name
		sheet_name = None
		
	ur_records = []
	wb = open_workbook( fname )
	datemode = wb.datemode
	
	ws = None
	for cur_sheet_name in wb.sheet_names():
		if cur_sheet_name == sheet_name or sheet_name is None:
			print 'Reading sheet: {}'.format(cur_sheet_name)
			ws = wb.sheet_by_name(cur_sheet_name)
			break
	
	if not ws:
		print 'Cannot find sheet "{}"'.format(sheet_name)
		return
		
	num_rows = ws.nrows
	num_cols = ws.ncols
	for r in xrange(num_rows):
		row = ws.row( r )
		if r == 0:
			# Get the header fields from the first row.
			fields = [html_parser.unescape(unicode(v.value).strip()).replace('-','_').replace('#','').strip().replace('4', 'four').replace(' ','_').lower() for v in row]
			fields = ['f{}'.format(i) if not f else f.strip() for i, f in enumerate(fields)]
			print '\n'.join( fields )
			continue
			
		ur = dict( (f, row[c].value) for c, f in enumerate(fields) )
		ur_records.append( (r+1, ur) )
		if len(ur_records) == 1000:
			process_ur_records( ur_records )
			ur_records = []
			
	process_ur_records( ur_records )
	
	print 'Initialization in: ', datetime.datetime.now() - tstart