import pprint

import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

SPOTIPY_CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.environ.get("SPOTIPY_REDIRECT_URI")

SPOTIFY_USER_ID = "11128217121"
SPOTIFY_ENDPOINT_URL = f"https://api.spotify.com/v1/users/{SPOTIFY_USER_ID}/playlists"

travel_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD ")
BILLBOARD_URL = f"https://www.billboard.com/charts/hot-100/{travel_date}/"

response = requests.get(BILLBOARD_URL)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

print(song_names)

scope = "playlist-modify-private"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                              client_secret=SPOTIPY_CLIENT_SECRET,
                              redirect_uri=SPOTIPY_REDIRECT_URI,
                              scope="playlist-modify-private",
                              username=SPOTIFY_USER_ID,
                              show_dialog=True,
                              cache_path="token.txt"))

spotify_songs = [f"track:{song} year:{travel_date.split('-')[0]}" for song in song_names]

song_uris = []
for spot_song in spotify_songs:
    result = sp.search(spot_song, type="track")
    # pprint.pprint(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{spot_song} doesn't exist in Spotify. Skipped.")


playlist = sp.user_playlist_create(SPOTIFY_USER_ID,
                                   name=f"{travel_date} Billboard 100",
                                   description=f"Playlist with top hundred songs for the date: {travel_date}",
                                   public=False)

sp.playlist_replace_items(playlist_id=playlist["id"], items=song_uris)
