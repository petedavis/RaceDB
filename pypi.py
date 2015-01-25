import os
import shutil
import zipfile
import subprocess

from helptxt.compile import CompileHelp
from dependencies import pyllrp
from helptxt.version import version

def pypi():
	CompileHelp( 'helptxt' )
	subprocess.call( ['python', 'manage.py', 'collectstatic', '--noinput'] )

	installDir = 'RaceDB'

	zfname = os.path.join('install', 'RaceDB-Install-{}.zip'.format(version))
	zf = zipfile.ZipFile( zfname, 'w' )

	# Write all important source files to the install zip.
	suffixes = {
		'py',
		'txt', 'md',
		'html', 'css', 'js',
		'png', 'gif', 'jpg',
		'xls', 'xlsx',
		'gz',
	}
	for root, dirs, files in os.walk( '.' ):
		for f in files:
			fname = os.path.join( root, f )
			if any( d in fname for d in ['EV', 'GFRR'] ):
				continue
			if os.path.splitext(fname)[1][1:] in suffixes:
				print( 'writing: {}'.format(fname) )
				zf.write( fname, os.path.join(installDir, fname) )

	zf.write( '../../CrossMgr/CrossMgrImpinj/pyllrp/pypi/dist/' + pyllrp, os.path.join(installDir, pyllrp) )
	zf.close()
	
	googleDrive = r"c:\GoogleDrive\Downloads\All Platforms\RaceDB"
	
	# Delete any existing releases (for the moment).
	for root, dirs, files in os.walk( googleDrive ):
		for f in files:
			fname = os.path.join( root, f )
			if os.path.splitext(fname)[1] == '.zip' and os.path.basename(fname) != os.path.basename(zfname):
				print( 'removing: {}'.format(fname) )
				os.remove( fname )
	
	for fname in [zfname, 'Install-Readme.txt']:
		print( 'releasing: {}'.format(fname) )
		shutil.copy( fname, googleDrive )

if __name__ == '__main__':
	pypi()