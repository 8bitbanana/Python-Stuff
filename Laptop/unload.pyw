import os
from pprint import pprint

top = 'C:\\Program Files (x86)\\Steam\\steamapps\\common\\Nuclear Throne\\mods\\'
all_mods = []
for root, dirs, files in os.walk(top):
    for name in files:
        st = os.path.splitext
        extension = st(st(name)[0])[1]
        if extension == '.mod' or extension == '.wep': 
            all_mods.append(os.path.join(root,name).replace(top,'').lower())

os.chdir(top)
pprint(all_mods)
towrite = ''
for mod in all_mods:
    towrite += '/unloadmod {}\n'.format(mod)
towrite += '/checkmods'
f = open('unload.txt','w')
f.write(towrite)
f.close()
