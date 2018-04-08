import time, os

DUD = False
def current():
    return time.strftime("%Y-%m-%d %H:%M")
def cls():
    a=os.system("cls")

print("Shutdown Timer")
print()
print("Enter a timestring in the format %Y-%m-%d %H:%M")
print("The current time is", current())
print()
while True:
    print("20YY-MM-DD HH:MM")
    settime = input()
    if len(settime) == 16:
        try:
            settime_raw = time.strptime(settime, "%Y-%m-%d %H:%M")
            break
        except ValueError:
            print("Cannot parse timestring")
            print()
    elif settime == "dud":
        print("Set to dud shutdown")
        DUD = True
        print()
    else:
        print("Timestring of incorrect length")
        print()
    

while current()!=settime:
    cls()
    print(" === SHUTDOWN TIMER === ".center(30))
    print()
    print("CURRENT TIME".center(30))
    print(current().center(30))
    print()
    print(settime.center(30))
    print("SET TIME".center(30))
    print()
    time.sleep(1)

if not DUD:
    os.system("shutdown /h")
else:
    input("splat")
    
    
