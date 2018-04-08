import spotipy, os
import spotipy.util as util
from pprint import pprint

oauth = spotipy.oauth2.SpotifyClientCredentials(
    client_id="[redacted]",
    client_secret="[redacted]"
    )

spotify = spotipy.Spotify(client_credentials_manager=oauth)

while True:
    os.system("cls")
    keywords = input("Enter an artist - ")
    results = spotify.search(keywords, type='artist')
    try:
        pprint(results['artists']['items'][0])
    except IndexError:
        print("No Results")
    input()
