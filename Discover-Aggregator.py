
"""
Steps to write this program

1. Connect to the Spotify client

2. Find my saved songs

3. Save the most recently liked songs

4. move the most recently liked songs to the discovered 2020 playlist


"""

#####


import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials

<<<<<<< HEAD
clientID = '#'
clientsecret = '#'
=======


with open('key.json', 'rb') as f:
        keychain = json.load(f)
        clientID = keychain['clientID']
        clientsecret = keychain['clientsecret']
        username = keychain['username']
        
redirect_uri = 'http://localhost:8888'


'''
1. Connect to the spotify client
'''
>>>>>>> like_mover


client_credentials_manager = SpotifyClientCredentials(clientID,clientsecret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

scope = 'user-modify-playback-state user-read-playback-state user-read-currently-playing user-top-read user-read-recently-played user-library-modify user-library-read user-follow-modify user-follow-read playlist-read-private playlist-modify-public playlist-modify-private playlist-read-collaborative user-read-private user-read-email app-remote-control'
token = spotipy.util.prompt_for_user_token(username,
                           scope,
                           clientID,
                           clientsecret,
                           redirect_uri)

#Check
if token:
    sp = spotipy.Spotify(auth=token)
else:
    print("Can't get token for", username)

'''
2. Find my saved songs
'''
seasonal_playlist = 'Winter 2020'




spotify.user_playlists(username, limit = 1, offset=0)
    


spotify.current_user_saved_tracks(limit = 10)
#