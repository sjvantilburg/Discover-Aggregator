
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
liked_songs = sp.current_user_saved_tracks(limit=50)

#Collect recent songs
def convert_spotify_date(dte):
    return datetime.datetime.strptime(dte,"%Y-%m-%dT%H:%M:%SZ")


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

print(song_collection)

####################################################################################
''' 3. Find the target playlist '''


#target playlist to add songs into
target_playlist_name = 'Winter 2020 (2)'
target_playlist_uri = ''

#get target playlist uri
for i in range(0,len(playlists['items'])):
    if playlists['items'][i]['name'] == target_playlist_name:
        target_playlist_uri = playlists['items'][i]['uri']

#Get target playlist tracks
target_playlist_tracks = sp.playlist_tracks(target_playlist_uri)






#####################################################################################
''' 4. Add new songs to playlist '''

#Add collection to playlist

#sp.user_playlist_add_tracks(username, target_playlist_uri, song_collection)     # It worked!





#######################################################################################3
''' 5. Remove duplicates from target playlist '''

#def remove_duplicate_songs(usernme, playlist):
    #find the dupes
track_positions = {}
track_list_to_be_deleted = []
for i in range(0, len(target_playlist_tracks['items'])-1):
    print ('i is ' + str(i))
    for j in range(1, len(target_playlist_tracks['items'])-i):
        print('j is '+str(j))
        if target_playlist_tracks['items'][i]['track']['uri'] == target_playlist_tracks['items'][j+i]['track']['uri']:
            uri = target_playlist_tracks['items'][i]['track']['uri'].rsplit(':',1)
            track_positions['uri'] = uri[-1]
            track_positions['positions']= i+j
            print(track_positions)
            #sp.user_playlist_remove_specific_occurrences_of_tracks(username, 
             #                                                      target_playlist_tracks, 
              #                                                   str(track_positions))
            track_list_to_be_deleted.append(track_positions.copy())
    
    #print(temp_positions)            
print(track_list_to_be_deleted)        
            
track_list_to_be_deleted = [str(i) for i in track_list_to_be_deleted]

target_playlist_tracks['href'] = str(target_playlist_tracks['href'])

target_playlist_tracks

sp.user_playlist_remove_specific_occurrences_of_tracks(username, target_playlist_uri, track_list_to_be_deleted)

target_playlist_tracks

#remove_duplicate_songs(username, target_playlist)
{'uri': 'spotify:track:70o9lZxBe86XLvQCywNdJ9', 'positions': [8]}



# target_playlist_tracks['items'][0]['track']['uri']




