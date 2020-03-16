
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
import datetime


with open('key.json', 'rb') as f:
        keychain = json.load(f)
        clientID = keychain['clientID']
        clientsecret = keychain['clientsecret']
        username = keychain['username']
        
redirect_uri = 'http://localhost:8888'


'''
1. Connect to the spotify client
'''


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
#Get all users playlists
playlists = sp.user_playlists(username, limit = 50, offset=0)


#check target playlist season


#target playlist to add songs into
target_playlist_name = 'Winter 2020'
target_playlist_uri = ''
#get target playlist uri
for i in range(0,len(playlists['items'])):
    if playlists['items'][i]['name'] == target_playlist_name:
        target_playlist_uri = playlists['items'][i]['uri']

#find saved songs
liked_songs = sp.current_user_saved_tracks(limit=50)


def convert_spotify_date(dte):
    return datetime.datetime.strptime(dte,"%Y-%m-%dT%H:%M:%SZ")


#Collect recent songs
year = datetime.datetime.now().year
spring_start = datetime.datetime.strptime(str(year)+'-03-01T00:00:00Z',"%Y-%m-%dT%H:%M:%SZ")
summer_start = datetime.datetime.strptime(str(year)+'-06-01T00:00:00Z',"%Y-%m-%dT%H:%M:%SZ")
fall_start = datetime.datetime.strptime(str(year)+'-09-01T00:00:00Z',"%Y-%m-%dT%H:%M:%SZ")
winter_start = datetime.datetime.strptime(str(year)+'-12-01T00:00:00Z',"%Y-%m-%dT%H:%M:%SZ")
last_winter_start = datetime.datetime.strptime(str(year-1)+'-12-01T00:00:00Z',"%Y-%m-%dT%H:%M:%SZ")

song_collection = []

for i in range(0, len(liked_songs['items'])):
    if (convert_spotify_date(liked_songs['items'][i]['added_at']).date() > last_winter_start.date()):
        song_collection.append(liked_songs['items'][i]['track']['uri'])



#Add collection to playlist

sp.user_playlist_add_tracks(username, target_playlist_uri, song_collection)     



# It worked!
## Need to remove duplicates 














