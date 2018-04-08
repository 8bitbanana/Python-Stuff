import school_inject, inject
program="""
import webbrowser, time
time.sleep(120)
webbrowser.open('http://eelslap.com')
"""
a=input()
if a=='0':
    school_inject.run(program)
else:
    inject.run(program)
a=input()
