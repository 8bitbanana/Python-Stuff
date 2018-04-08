import os
try:
    f=open('filestore.txt','r')
except:
    print('filestore.txt fail')
    a=input()
    exit()
okdir=f.read()
print(okdir)
f.close()
try:
    os.chdir(okdir)
except:
    print('chdir fail')
    a=input()
    exit()
try:
    f=open('a.pyw','r')
except:
    print('a.pyw fail')
    a=input()
    exit()
program = f.read()
f.close()
print(os.path.join(okdir,'a.pyw') + ' exists')
print('Printing contents...')
print(program)
a=input('Hit enter to delete a.pyw')
os.remove('a.pyw')
