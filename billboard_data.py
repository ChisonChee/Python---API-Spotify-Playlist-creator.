import requests
from bs4 import BeautifulSoup
import pandas as pd


class BillboardData:
    def __init__(self, year_request):
        billboard_url = f"https://www.billboard.com/charts/hot-100/{year_request}"
        response = requests.get(url=billboard_url)
        soup = BeautifulSoup(response.text, "html.parser")
        get_label = soup.findAll(name="span", class_="c-label a-font-primary-bold-l u-font-size-32@tablet u-letter-spacing-0080@tablet")
        pre_song_title = soup.findAll(name="h3", id="title-of-a-story", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet")
        post_song_title = soup.findAll(name="h3", id="title-of-a-story", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
        song_list_compilation = pre_song_title + post_song_title
        formatted_label = [label.text.replace("\n", "").replace("\t", "") for label in get_label]
        formatted_song_list = [song.text.replace("\n", "").replace("\t", "") for song in song_list_compilation]
        song_dict = {
            "list": formatted_label,
            "songs": formatted_song_list
        }

        df = pd.DataFrame(song_dict)
        df.to_csv(path_or_buf="song_list.csv", index=False)
        self.song_data = None


