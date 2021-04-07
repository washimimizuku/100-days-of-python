import io
from bs4 import BeautifulSoup
import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

SPOTIFY_CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')

BASE_URL = "https://www.billboard.com/charts/hot-100/"

LOCATION = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
TOKEN_FILE = os.path.join(LOCATION, "token.txt")

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(f"{BASE_URL}{date}")
response.raise_for_status()
html = response.text

soup = BeautifulSoup(html, "html.parser")
songs = [song.getText() for song in soup.find_all(name="span", class_="chart-element__information__song")]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri="https://example.com/callback/'",
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path=TOKEN_FILE
    )
)

user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
