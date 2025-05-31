import path

import uos
files=[]
dirs=[]
def S_ISDIR(fname):
    try:
        f = open(fname, "r")
        exists = True
        f.close()
    except OSError:
        exists = False
    return(exists)
def walk(top):
    for dirent in uos.ilistdir(top):
        #print(dirent)
        mode = dirent[1] << 12
        fname = dirent[0]
        if S_ISDIR(fname):
            dirs.append(fname)
        else:
            files.append(fname)
    yield top, dirs, files
    for d in dirs:
        yield from walk(top + "/" + d)
for top, dirs, files in walk('/sd'):
    print(dirs,files)