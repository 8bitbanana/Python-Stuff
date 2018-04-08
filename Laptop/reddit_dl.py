# TODO - Imgur support

import praw, requests, os, time, unicodedata, bs4
import prawcore.exceptions

image_formats = [".jpeg",".jpg",".png",".bmp",".tiff",".svg",".hdr",".gif",".webp",".bpg"]

client_id = '[redacted]'
client_secret = '[redacted]'
user_agent = '[redacted]'

def getImgur(url):
    if not "imgur.com" in url: return url # Idiot proofing
    if "/a/" in url: # Album
                
    elif "i.imgur.com" in url: # Direct image
        pass
    else: # Single image page
        pass

# Get the images to download
reddit = praw.Reddit(client_id=client_id,client_secret=client_secret,user_agent=user_agent)
while True:
    username = input("Enter a Redditor - ")
    user = reddit.redditor(username)
    try:
        # Use user.fullname to test if the user exists, if they don't reddit 404s
        a = user.fullname
    except prawcore.exceptions.NotFound:
        print("User doesn't exists or is deleted/banned")
        continue
    raw_posts = list(user.submissions.top())
    posts = []
    for post in raw_posts:
        # 1) is it not a selfpost? 2) is the file extension in image formats?
        if not post.is_self and post.url[post.url.rfind("."):].lower() in image_formats:
            posts.append(post)
    if len(posts) == 0:
        print("User doesn't have any image posts")
        continue
    # All is good, break out of the loop
    break

# Download the images
try:
    os.mkdir(username)
except FileExistsError:
    # TODO double folder handling
    pass
os.chdir(username)
for image in posts:
    url = image.url
    image_dl = requests.get(url, stream=True)
    filename = os.path.split(url)[1]
    print("Downloading {}...".format(filename))
    with open(filename, "wb") as fd:
        for chunk in image_dl.iter_content(chunk_size=128)):
            fd.write(chunk)
print("\nDone")
