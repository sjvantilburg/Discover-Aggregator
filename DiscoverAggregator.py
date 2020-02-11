
"""
Steps to write this program

1. Connect to the Spotify client

2. Find my saved songs

3. Save the most recently liked songs

4. move the most recently liked songs to the discovered 2020 playlist


"""


#####3 Birdy song list
import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials

clientID = '2f6d5f7facc640bf984f39313fdf4342'
clientsecret = 'f95c221e551c4d558be4733b49b04483'


client_credentials_manager = SpotifyClientCredentials(clientID,clientsecret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

if len(sys.argv) > 1:
    name = ' '.join(sys.argv[1:])
else:
    name = 'Radiohead'

results = spotify.search(q='artist:' + name, type='artist')
items = results['artists']['items']
if len(items) > 0:
    artist = items[0]
    print(artist['name'], artist['images'][0]['url'])