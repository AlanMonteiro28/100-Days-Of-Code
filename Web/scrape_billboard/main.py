from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SP_CLIENT_ID = "YOUR API ID"
SP_CLIENT_SECRET = "YOUR CLIENT SECRET"
SP_URI = "http://example.com"

# 2015 
URL = "https://www.billboard.com/charts/hot-100/"

#input 
user_input = input("Which year do you want to travel to?\nType the date in this format YYYY-MM-DD: ")
NEW_URL= f"{URL}{user_input}"

r = requests.get(url=NEW_URL)
billboard_web_page = r.text

# h3 id=title-of-a-story class=c-title
soup = BeautifulSoup(billboard_web_page, "html.parser")
song_titles = soup.select("li ul li h3")
song_titles = [song.getText().strip() for song in song_titles]
    
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
            client_id=SP_CLIENT_ID,
            client_secret=SP_CLIENT_SECRET,
            redirect_uri=SP_URI, 
            scope="playlist-modify-private playlist-modify-public",
            cache_path="token.txt",
            show_dialog=True,
            )
        )

user_id = sp.current_user()["id"]

song_uris = []
year = user_input.split("-")[0]
for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        pass
        print(f"The song: {song} not found!")
        

print("Song URIs:", song_uris)

playlist = sp.user_playlist_create(user=user_id,
                                   name=f"{user_input} Billboard 100", 
                                   public=True,
                                )

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)