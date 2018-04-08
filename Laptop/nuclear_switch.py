import os, glob

# This program switches the vanilla and NTT executables so you don't have to
# /u/8bitbananaEC

# CHANGE TO THE DIRECTORY OF NUCLEAR THRONE
nuclear_dir = 'C:\\Program Files (x86)\\Steam\\steamapps\\common\\Nuclear Throne'

os.chdir(nuclear_dir)
pathdump = glob.glob('*.exe') # Get all .exe files

NUCLEAR = False # Does nuclearthrone.exe exist?
NUCLEAR_MULTI = False # Does nuclearthrone_multi.exe exist?
NUCLEAR_SINGLE = False # Does nuclearthrone_single.exe exist?

for exe in pathdump: # Search for all the exes
    if exe == 'nuclearthrone.exe':
        NUCLEAR = True
    elif exe == 'nuclearthrone_multi.exe':
        NUCLEAR_MULTI = True
    elif exe == 'nuclearthrone_single.exe':
        NUCLEAR_SINGLE = True
    elif exe.startswith('nuclearthrone-original') and not NUCLEAR_SINGLE and not NUCLEAR_MULTI:
        print ('{} found'.format(exe)) # An NTT backup has been found
        print ('Hit enter to rename it to nuclearthrone_single.exe so this program works')
        input()
        os.rename(exe,'nuclearthrone_single.exe')
        NUCLEAR = True
        NUCLEAR_SINGLE = True

print()
print ('==================================')
print ('NUCLEAR THRONE EXECUTABLE SWITCHER')
print ('==================================')
print()

MODE = None # 'single' means SINGLEPLAYER
            # 'multi' means MULTIPLAYER
            # None means something went wrong

if not NUCLEAR:
    print ('Nuclear Throne EXE not found!')
    print()
elif NUCLEAR_MULTI:
    print ('Nuclear Throne state set to SINGLEPLAYER')
    print()
    print ('Hit enter to switch to MULTIPLAYER')
    print()
    mode = 'single'
elif NUCLEAR_SINGLE:
    print ('Nuclear Throne state set to MULTIPLAYER')
    print()
    print ('Hit enter to switch to SINGLEPLAYER')
    mode = 'multi'
else:
    print ('Nuclear Throne Together EXE not found!')
    print ()

input()
if mode == 'single':
    os.rename('nuclearthrone.exe','nuclearthrone_single.exe')
    os.rename('nuclearthrone_multi.exe','nuclearthrone.exe')
    print ('State set to MULTIPLAYER')
    input()
elif mode == 'multi':
    os.rename('nuclearthrone.exe','nuclearthrone_multi.exe')
    os.rename('nuclearthrone_single.exe','nuclearthrone.exe')
    print ('State set to SINGLEPLAYER')
    input()
