import spotipy
from spotipy.oauth2 import SpotifyOAuth


class SpotifyManager:
    def __init__(self):
        self.track_info = []
        self.query_list = []
        self.client_id = None
        self.search_data = []
        scope = "playlist-modify-private"
        client_ID = "YOUR_CLIENT_ID"
        client_Secret = "YOUR_CLIENT_SECRET_KEY"
        redirect_url = "http://example.com"
        self.sp = SpotifyOAuth(client_id=client_ID, client_secret=client_Secret, redirect_uri=redirect_url,
                               scope=scope, cache_path="Token.txt")
        self.sp.get_access_token()
        self.client_response = spotipy.Spotify(oauth_manager=self.sp)

    def get_user_id(self):
        self.client_id = self.client_response.current_user()["id"]

    def track_query(self, song_list, year):
        for song in song_list:
            self.query_list.append(f"track:{song} year:{year}")

    def search_track(self, query_list):
        for query in query_list:
            track = self.client_response.search(q=query, limit=1)
            self.search_data.append(track)

    def track_info_list(self):
        for track_num in range(len(self.search_data)):
            try:
                uri = self.search_data[track_num]['tracks']['items'][0]['uri']
                self.track_info.append(uri)
            except IndexError:
                pass

    def add_to_playlist(self, client_id, track_uri_list, billboard_date):
        playlist_id = self.client_response.user_playlist_create(user=client_id, name=f"{billboard_date} Billboard 100",
                                                                public=False)['id']
        self.client_response.playlist_add_items(playlist_id=playlist_id, items=track_uri_list)
