import glob, os
files = glob.glob('*.jpg')
for image in files:
    original = image
    image = image.replace('.jpg','')
    if len(image) == 1:
        image = '000' + image
    elif len(image) == 2:
        image = '00' + image
    elif len(image) == 3:
        image = '0' + image
    image += '.jpg'
    os.rename(original, image)
