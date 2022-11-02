import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

name = 'creep'
results = sp.search(q='track:' + name, type='track')
id = results['tracks']['items'][0]['id']

print(id)

print(sp.audio_features(tracks=id))

name = 'Strokes'

results = sp.search(q='artist:' + name, type='artist')

uri = results['artists']['items'][0]['uri']

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = spotify.artist_albums(uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'], type(album['release_date']))




