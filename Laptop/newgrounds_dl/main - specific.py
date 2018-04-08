
'''

Automatically download all of the audio from a newgrounds artist

requests - Get the files from the internet
os - Change directory
tqdm - Progress indercators
bs4 - To sort through the html
mutagen - To access .mp3 metadata

'''

import requests, os, time, glob
from tqdm import tqdm
from bs4 import BeautifulSoup
from mutagen.easyid3 import EasyID3
from pprint import pprint

# Get the user inputs for the artist name and album preferences
def getUserPrefs():
    print("Enter a Newgrounds artist to download music from")
    print("Format how you would like the artist to appear on the downloaded files")
    while True: # Loop to get artist name, breaks out if valid
        artist = input("Artist - ")
        if artist == "":
            print("Enter an artist name")
            continue
        # Does the artist name 404?
        if str(requests.get("http://{}.newgrounds.com".format(artist.lower()))) == "<Response [404]>":
            print("Artist {} does not exist".format(artist))
            continue
        break
    print()
    print("Enter the album name you would like to appear on the downloaded files")
    print("Default - \"NG Downloads\"")
    # Don't bother looping to get album name, as there are no invalid entries
    album = input("Album - ")
    if album == "":
        album = "NG Downloads"
    page_url = "https://{}.newgrounds.com/audio/".format(artist.lower())
    while True:
        # User confirmation
        print("Allow duplicate files?")
        user = input("(y/n) - ".lower())
        if user is "y":
            duplicate = True
            break
        elif user is "n":
            duplicate = False
            break
        else:
            print("Enter y or n")
    return artist, album, page_url, duplicate


# Fetch all the music titles and links
def fetchLinks(html, duplicate=True): # TODO fix duplicate removal
    music = []
    soup = BeautifulSoup(html, "html.parser")
    allTags = soup.find_all('a')
    for tag in allTags:
        if "www.newgrounds.com/audio/listen/" in str(tag) and not "<strong>" in str(tag):
            music.append([tag.get("href"), str(tag.contents[0]) + ".mp3"])
    return music


# Fetch all the music from a list of lists [track_id, track_title]
def fetchFiles(music, artist, album):
    print("Getting {} track(s) from {}".format(len(music), artist))
    index = 1
    for track in music:

        print("\nGetting {} [{}] [{}/{}]".format(track[1], track[0],index,len(music)))

        # Loop to download the music file, using tqdm's progress bar
        # while error is so it just loops if there is a crash
        while True:
            track_dl = requests.get("https://www.newgrounds.com/audio/download/{}".format(track[0]), stream=True)
            # Newgrounds will rate limit, wait a bit if there is a error 429 (too many requests)
            if str(track_dl) == "<Response [429]>":
                for _ in tqdm(range(30), leave=False, desc="RATELIMIT", ncols=60):
                    time.sleep(1)
                continue
            elif str(track_dl) != "<Response [200]>":
                print(str(track_dl) + " - Retrying...")
                time.sleep(1)
                continue
            with open(track[1], "wb") as fd:
                for chunk in tqdm(track_dl.iter_content(chunk_size=128), leave=False):
                    fd.write(chunk)
            tagFile(track[1], artist, album)
            break
        index+=1

def chooseLinks(music):
    pprint(music)
    chosen_music = []
    while True:
        print("{} tracks, Add a track".format(len(chosen_music)))
        toSearch = input(">>> ")
        index = 0
        results = []
        for track in music:
            if toSearch.lower() in track[1].lower():
                print("[{}] - {}".format(index, track))
                index+=1
                results.append(track)
        if index==0:
            print("None found")
        else:
            chosen = input(">>> ")
            if chosen == "quit":
                break
            try:
                chosen_music.append(results[int(chosen)])
            except:
                print("Error")
    return chosen_music
        
# Use mutagen to add metadata to the .mp3 files
def tagFile(track, artist, album):
    audiofile = EasyID3(track)
    audiofile["title"] = track[:-4]
    audiofile["artist"] = artist
    audiofile["album"] = album
    audiofile.save()


# Remove invalid chars from a track so it works as a filename
def formatTitle(oldStr):
    invalid_chars = "\\/:*?\"<>|"
    newStr = ""
    for char in oldStr:
        valid = True
        for test in invalid_chars:
            if char is test:
                valid = False
        if valid:
            newStr += char
    return newStr


def main():
    os.chdir("downloads")
    while True:
        artist, album, page_url, duplicate = ("Waterflame", "Waterflame", "http://waterflame.newgrounds.com/audio/", False)

        # User confirmation
        print("\nArtist = {}\nAlbum = {}\nURL = {}\nAllow Duplicates = {}".format(artist, album, page_url, duplicate))
        print("Is this OK?")
        print()
        user = input("(y/n) - ".lower())
        if user is "y":
            break
    print()
    chosen_music = fetchLinks(requests.get(page_url).text, duplicate)
    music = chooseLinks(chosen_music)

    # Format the links to download links
    for track in music:
        track[0] = track[0].rsplit("/", 1)[-1]

    # Format the track titles so they are valid filenames
    for track in music:
        track[1] = formatTitle(track[1])

    fetchFiles(music, artist, album)
    print("\nDone!")


if __name__ == "__main__":
    main()