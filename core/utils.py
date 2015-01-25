import os
import sys
import re
import urllib
import unicodedata

def uniquify(seq, idfun=None):  
	# order preserving 
	if idfun is None: 
		def idfun(x): return x 
	seen = set()
	result = [] 
	for item in seq: 
		marker = idfun(item) 
		if marker in seen:
			continue 
		seen.add( marker )
		result.append(item) 
	return result

def removeDiacritic( s ):
	'''
	Accept a unicode string, and return a normal string (bytes in Python 3)
	without any diacritical marks.
	'''
	if type(s) == str:
		return s
	else:
		return unicodedata.normalize('NFKD', s).encode('ASCII', 'ignore')

def toUnicode( s ):
	if isinstance( s, unicode ):
		return s
		
	encodings = (
		'utf-8', 'iso-8859-1', 'iso-8859-2', 'iso-8859-3', 'iso-8859-4', 'iso-8859-5',
		'iso-8859-7', 'iso-8859-8', 'iso-8859-9', 'iso-8859-10', 'iso-8859-11',
		'iso-8859-13', 'iso-8859-14', 'iso-8859-15',' utf-8', 
	)
	for encoding in encodings:
		try:
			return unicode( s, encoding )
		except UnicodeDecodeError as e:
			pass
	raise e

reSep = re.compile( u'[:;,-/. \t]+' )
def normalizeSeparators( s ):
	return reSep.sub( u' ', s )

def normalizeSearch( s ):
	return normalizeSeparators(removeDiacritic(s.strip())).lower()
	
def matchSearchFields( search, field ):
	if isinstance(search, (unicode, bytes)):
		search = normalizeSearch( search ).split()
	
	field = removeDiacritic( field.strip() ).lower()
	return all( s in field for s in search )
	
escChars = set( r".^$*+?()[{\|" )
def matchSearchToRegEx( search ):
	if isinstance(search, (unicode, bytes)):
		search = normalizeSearch( search ).split()
	return re.compile( u''.join([
		u'^',
		''.join( u'(?=.*{})'.format(u''.join(u'\\{}'.format(c) if c in escChars else c for c in s) for s in search)),
		u'.*$'])
	)

def get_search_text( fields ):
	if isinstance(fields, (unicode, bytes)):
		fields = [fields]
	
	return removeDiacritic(
		reSep.sub(
			u' ',
			u' '.join(u'"{}"'.format(f) for f in fields if f)
		).lower()
	)

HexChars = set( '0123456789ABCDEFabcef' )
def allHex( tag ):
	return all( c in HexChars for c in tag.strip() )

#---------------------------------------------------------------------------------------

reCap = re.compile( '[a-z0-9][A-Z]' )
def splitCapWords( word ):
	while 1:
		m = reCap.search( word )
		if not m:
			break
		i = m.start(0) + 1
		word = word[:i] + ' ' + word[i:]
	return word

class Breadcrumb( object ):
	def __init__( self, name, url ):
		if not url.endswith( '/' ):
			url += '/'
		while url.endswith( '//' ):
			url = url[:-1]
		self.name = name
		self.url = url

reNum = re.compile( '^\d+$' )
class Breadcrumbs( object ):
	def __init__( self, pathIn ):
		self.breadcrumbs = []
		try:
			path = pathIn[:pathIn.index('?')]
		except ValueError:
			path = pathIn
		
		components = path.split( '/' )
		if not components:
			return
			
		if not components[-1]:
			components = components[:-1]
			
		breadcrumbs = []
		i = 1
		while i < len(components):
			j = i + 1
			while j < len(components) and reNum.match( components[j] ):
				j += 1
			breadcrumbs.append( Breadcrumb(splitCapWords(components[i]), '/'.join(components[:j]) ) )
			i = j

		#self.breadcrumbs = breadcrumbs[1:]
		self.breadcrumbs = breadcrumbs
	
	@property
	def title( self ):
		return self.breadcrumbs[-1].name
		
	def pop( self, n = 1 ):
		try:
			return self.breadcrumbs[-1-n].url
		except IndexError:
			return ''
	
	@property
	def url( self ):
		return self.pop(0)
	
	@property
	def cancelUrl( self ):
		return self.pop(1)
	
	@property
	def popUrl( self ):
		return self.pop(1)
	
	@property
	def pop2Url( self ):
		return self.pop(2)
	
	@property
	def pop3Url( self ):
		return self.pop(3)

def popUrl( url ):
	return Breadcrumbs(url).popUrl
	
def pop2Url( url ):
	return Breadcrumbs(url).pop2Url
	
def pop3Url( url ):
	return Breadcrumbs(url).pop3Url
	
def cancelUrl( url ):
	return Breadcrumbs(url).cancelUrl
