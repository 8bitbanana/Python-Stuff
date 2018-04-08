import subprocess, time, ctypes
info=subprocess.check_output(["wmic","cpu","get", "name"],shell=True)
info = str(info)
old_speed = info.split('@')[1].split(' ')[1]
print(old_speed)
while True:
    info=subprocess.check_output(["wmic","cpu","get", "name"],shell=True)
    info = str(info)
    new_speed = info.split('@')[1].split(' ')[1]
    if old_speed!=new_speed:
        print(new_speed)
        break
now = time.asctime(time.localtime(time.time()))
f = open('RESULTS.txt','w')
f.write(now + '\n' + old_speed + ' - ' + new_speed)
f.close()
ctypes.windll.user32.MessageBoxW(0, 'From ' + old_speed + ' to ' + new_speed, "CPU SPEED CHANGED", 1)
#input()
