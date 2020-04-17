
"""
Steps to write this program

1. Connect to the Spotify client

2. Find my saved songs

3. Find target playlist

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



#####################################################################################
'''
2. Find my saved songs
'''
#Get all users playlists
playlists = sp.user_playlists(username, limit = 50, offset=0)


#find saved songs
liked_songs = sp.current_user_saved_tracks(limit = 50)


#format date to find recently liked songs
def convert_spotify_date(dte):
    return datetime.datetime.strptime(dte,"%Y-%m-%dT%H:%M:%SZ")

year = datetime.datetime.now().year
spring_start = datetime.datetime.strptime(str(year)+'-03-01T00:00:00Z',"%Y-%m-%dT%H:%M:%SZ")
summer_start = datetime.datetime.strptime(str(year)+'-06-01T00:00:00Z',"%Y-%m-%dT%H:%M:%SZ")
fall_start = datetime.datetime.strptime(str(year)+'-09-01T00:00:00Z',"%Y-%m-%dT%H:%M:%SZ")
winter_start = datetime.datetime.strptime(str(year)+'-12-01T00:00:00Z',"%Y-%m-%dT%H:%M:%SZ")
last_winter_start = datetime.datetime.strptime(str(year-1)+'-12-01T00:00:00Z',"%Y-%m-%dT%H:%M:%SZ")



#Collect recent songs
song_collection = []

for i in range(0, len(liked_songs['items'])):
    if (convert_spotify_date(liked_songs['items'][i]['added_at']).date() > spring_start.date()):
        song_collection.append(liked_songs['items'][i]['track']['uri'])

####################################################################################
''' 3. Find the target playlist '''


#target playlist to add songs into
target_playlist_name = 'Spring 2020'
target_playlist_uri = ''

#get target playlist uri
for i in range(0,len(playlists['items'])):
    if playlists['items'][i]['name'] == target_playlist_name:
        target_playlist_uri = playlists['items'][i]['uri']

#Get target playlist tracks
target_playlist_tracks = sp.playlist_tracks(target_playlist_uri)
listof_target_playlist_tracks = []
for i in range(0, len(target_playlist_tracks['items'])):
    listof_target_playlist_tracks.append(target_playlist_tracks['items'][i]['track']['uri'])



###########################
###make sure that I add the correct ones. 
### 

songs_to_add = [i for i in song_collection if i not in listof_target_playlist_tracks]



#####################################################################################
''' 4. Add new songs to playlist '''

#Add collection to playlist
if len(songs_to_add) > 0:
    sp.user_playlist_add_tracks(username, target_playlist_uri, songs_to_add)     # It worked!
    print("Time is: " + str(datetime.datetime.now()) + ', added --- ' + str(songs_to_add))
    
else:
    print("Time is: "+ str(datetime.datetime.now()) + ' --- added no songs')





