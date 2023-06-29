from billboard_data import BillboardData
from spotify_manager import SpotifyManager
import pandas

billboard_date = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ')
song_list = BillboardData(billboard_date)
spotify_request = SpotifyManager()
spotify_request.get_user_id()
client_id = spotify_request.client_id

song_data = pandas.read_csv("song_list.csv").to_dict(orient="list")['songs']
yrs = billboard_date.split("-")[0]
spotify_request.track_query(song_list=song_data, year=yrs)
spotify_request.search_track(query_list=spotify_request.query_list)
spotify_request.track_info_list()
track_data = spotify_request.track_info
spotify_request.add_to_playlist(client_id=client_id, track_uri_list=track_data, billboard_date=billboard_date)
