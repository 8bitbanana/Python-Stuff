import os, glob

nuclear_dir = 'C:\\Program Files (x86)\\Steam\\steamapps\\common\\Terraria'

os.chdir(nuclear_dir)
pathdump = glob.glob('*.exe')

TERRA = False
TERRA_MOD = False
TERRA_VAN = False

for exe in pathdump:
    if exe == 'Terraria.exe':
        TERRA = True
    elif exe == 'Terraria_tmod.exe':
        TERRA_MOD = True
    elif exe == 'Terraria_vanilla.exe':
        TERRA_VAN = True
    elif exe.startswith('Terraria_v1') and not TERRA_VAN and not TERRA_MOD:
        print ('{} found'.format(exe))
        print ('Hit enter to rename it to Terraria_vanilla.exe so this program works')
        input()
        os.rename(exe,'Terraria_vanilla.exe')
        TERRA = True
        TERRA_VAN = True

print()
print ('==================================')
print ('NUCLEAR THRONE EXECUTABLE SWITCHER')
print ('==================================')
print()

MODE = None
if not TERRA:
    print ('Terraria EXE not found!')
    print()
elif TERRA_MOD:
    print ('Terraria state set to VANILLA')
    print()
    print ('Hit enter to switch to TMODLOADER')
    print()
    mode = 'vanilla'
elif TERRA_VAN:
    print ('Terraria state set to TMODLOADER')
    print()
    print ('Hit enter to switch to VANILLA')
    mode = 'tmod'
else:
    print ('Terraria EXE not found!')
    print ()

input()
if mode == 'vanilla':
    os.rename('Terraria.exe','Terraria_vanilla.exe')
    os.rename('Terraria_tmod.exe','Terraria.exe')
    print ('State set to TMODLOADER')
    input()
elif mode == 'tmod':
    os.rename('Terraria.exe','Terraria_tmod.exe')
    os.rename('Terraria_vanilla.exe','Terraria.exe')
    print ('State set to VANILLA')
    input()
