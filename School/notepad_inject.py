import school_inject, inject
program="""
import time, os
time.sleep(120)
for x in range(0,10):
    os.startfile('notepad.exe')
"""
a=input()
if a=='0':
    school_inject.run(program)
else:
    inject.run(program)
a=input()
