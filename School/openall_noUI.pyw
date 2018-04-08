import os, random, time
top = '\\\\[redacted]\\Shared'
all_files = []
for root, dirs, files in os.walk(top, topdown=False):
    for name in files:
        if name[0]!='.' and name[len(name)-4]!='.xls':
            all_files.append(os.path.join(root, name))
random.shuffle(all_files)
time.sleep(random.randint(30,60))
for file in all_files:
    try:
        os.startfile(file)
    except:
        pass
