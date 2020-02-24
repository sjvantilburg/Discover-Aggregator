
"""
Steps to write this program

1. Connect to the Spotify client

2. Find my saved songs

3. Save the most recently liked songs

4. move the most recently liked songs to the discovered 2020 playlist


"""

#####


import spotipy

from spotipy.oauth2 import SpotifyClientCredentials

clientID = '2f6d5f7facc640bf984f39313fdf4342'
clientsecret = 'f95c221e551c4d558be4733b49b04483'
username = '129270258'
redirect_uri = 'http://localhost:8888'

client_credentials_manager = SpotifyClientCredentials(clientID,clientsecret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

scope = 'user-library-read playlist-modify-private user-library-modify playlist-modify-public'
token = spotipy.util.prompt_for_user_token(username,
                           scope,
                           clientID,
                           clientsecret,
                           redirect_uri)



token

if token:
    sp = spotipy.Spotify(auth=token)
else:
    print("Can't get token for", username)



spotify.current_user()
#spotify.artist_albums(artist_id, album_type=None, country=None, limit=20, offset=0)
