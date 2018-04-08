from tqdm import tqdm
from bs4 import BeautifulSoup
import requests, time, os, shutil


img_url = "http://www.textures.com/freebieTodayDownload" # URL of the freebie image
page_url = "http://www.textures.com"                     # URL of the textures.com page

page = requests.get(page_url) # Get the page
img = requests.get(img_url, stream=True) # Get the image

# Get the <div> to find the image filename of the freebie image
page_div = str(BeautifulSoup(page.text, "html.parser").find(id="freebieOfTheDayTexture"))

# Get the location of the background image url
bg_img_index = page_div.find("background-image:url('") + 22

# Extract that url
img_filename = ""
for x in page_div[bg_img_index:]:
    if x == "'":
        break
    img_filename += x

# Get the filename from the path ([1] selecting the tail)
img_filename = os.path.split(img_filename)[1]

print("Fetching {}...".format(img_filename))
# Fetch the image (now including fancy progress bars!
#with open(img_filename, 'wb') as fd:
  #  for chunk in tqdm(img.iter_content(chunk_size=128)):
    #    fd.write(chunk)

# Crappy non progress bar boringness (as it doesn't work as a .pyw)
with open(img_filename, 'wb') as fd:
    for chunk in img.iter_content(chunk_size=128):
        fd.write(chunk)
print("Fetched.\n")

print("Copying to OneDrive folder...")
shutil.copyfile(img_filename, "C:\\Users\\8bitb\\OneDrive - Suffolk One\\textures.com\\"+img_filename)
print("Copied")
