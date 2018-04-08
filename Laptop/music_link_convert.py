import requests
import json
from bs4 import BeautifulSoup
from pprint import pprint
user_input = input()
get_url = 'https://songlink.io/{}'.format(user_input)
response = requests.get(get_url)
page = response.text
soup = BeautifulSoup(page, 'lxml')
raw_json = str(soup.find_all("script")[4])
raw_json = raw_json.replace('<script id="initialState" type="application/json">','')
raw_json = raw_json.replace('</script>','')
parsed_json = json.loads(raw_json)
try:
    deezer_url = parsed_json['songlink']['deezer_url']
except:
    deezer_url = None
try:
    google_url = parsed_json['songlink']['google_url']
except:
    google_url = None
try:
    itunes_url = parsed_json['songlink']['itunes_url']
except:
    itunes_url = None
try:
    spotify_url = parsed_json['songlink']['spotify_url']
except:
    spotify_url = None
try:
    youtube_url = parsed_json['songlink']['youtube_url']
except:
    youtube_url = None
urldict = {'deezer':deezer_url,'google':google_url,'itunes':itunes_url,'spotify':spotify_url,'youtube':youtube_url}

pprint(urldict)
