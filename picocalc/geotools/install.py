#
#  Run this on the first time using the picocalc
#

print('Running Installer')

#  Python Imports
import os
import sys

#  Project internal to libs
#import libs

#  Check if /lib exists
try:
    print('Creating /lib')
    os.mkdir('/lib')
except OSError:
    print('/lib already exists')

#------------------------------------------#
#-          Temporary os.path APIs        -#
#------------------------------------------#
def temp_split(path):
    if path == "":
        return ("", "")
    r = path.rsplit("/", 1)
    if len(r) == 1:
        return ("", path)
    head = r[0] #.rstrip("/")
    if not head:
        head = "/"
    return (head, r[1])

def temp_dirname(path):
    return temp_split(path)[0]

def temp_basename(path):
    return temp_split(path)[1]

def temp_isdir(path):
    import stat
    try:
        mode = os.stat(path)[0]
        return stat.S_ISDIR(mode)
    except OSError:
        return False


#---------------------------------------------------#
#-        Simple Script for a Python "rsync"       -#
#---------------------------------------------------#
def temp_sync_dirs( input_dir, dest_dir, dry_run = False ):

    #  Walk through the folders
    print('From: ', input_dir, ', to: ', dest_dir )
    for x,y,z in libs.os.walk( input_dir ):
        print( x, y, z )


#  I'm frankly too frustrated with micropython's limitations to do this
#  correctly.  For now, I'll keep the old code on top, so I can fix it later
#  when I'm less discouraged. 

manifest = [ ( './libs/os/path.py',     '/lib/os/path.py' ),
             ( './libs/os/walk.py',     '/lib/os/walk.py' ),
             ( './libs/colors.py',      '/lib/colors.py' ),
             ( './libs/stat.py',        '/lib/stat.py' ) ]

for tup in manifest:
    
    #  Determine destination path
    path_in  = tup[0]
    path_out = tup[1]

    #  Open destination file
    print('copying from ', path_in, ' to ', path_out )
    with open( path_in,  'rb' ) as fin:

        #  Make sure destination folder exists
        try:
            temp_dir = temp_dirname( path_out )
            print( 'creating directory: ', temp_dir )
            os.mkdir( temp_dir )
        except OSError:
            pass
        
        with open( path_out, 'wb' ) as fout:
            
            bytes = fin.read()
            fout.write( bytes )


print('Installation Completed')
