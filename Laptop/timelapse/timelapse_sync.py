import os, glob, time
from pprint import pprint

dir1 = '\\\\192.168.0.120\\pihome\\timelapse\\'
dir2 = 'C:\\Users\\8bitb\\Desktop\\timelapse\\'

os.chdir(dir1)
while True:
    try:
        images = glob.glob('*.jpg')
    except Exception as e:
        print 'Error - ' + str(e)
        print 'Restarting...'
        continue
    for image in images:
        print 'Moving {}...'.format(image),
        if os.path.exists(dir2 + image):
            os.remove(dir2+image)
        try:
            os.rename(image, dir2 + image)
        except Exception as e:
            print 'Error - ' + str(e)
            print 'Restarting...'
            break
        print 'done'
    time.sleep(1)
