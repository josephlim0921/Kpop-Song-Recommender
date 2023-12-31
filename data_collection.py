from spotipy.oauth2 import SpotifyClientCredentials #To access authorised Spotify data
from tqdm import tqdm_notebook
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

# Obtaining client id and client secret from env
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) 

def get_tracks(artist_name):
    query = f"?q={artist_name}&type=artist&limit=1"
    for item in sp.search(query,type='track')['tracks']['items']:
        print(item['name'])
    

