from __future__ import unicode_literals
from pydantic import HttpUrl
import youtube_dl
from datetime import date, datetime, timedelta


class TwitterVideoDownloader:
    """
    Base Twitter video downloader class.
    Configuration: https://github.com/ytdl-org/youtube-dl#embedding-youtube-dl
    """

    ydl_options = {"outtmpl": "%(id)s.%(ext)s"}
    size_sample = (
        "N/A"  # To be updated, as there is no clear method to find accurate video size.
    )

    def extract_tweet_media_resolutions(self, dict_formats) -> dict:
        """
        Extract resolution and direct download link from YTDL response['format']
        """
        m3u8_header = "hls-"  # hls- xxx header indicates a video with m3u8 format
        dict = {}
        index = 0
        for f in dict_formats:
            #
            if m3u8_header not in f["format_id"]:
                dict[index] = {}
                dict[index]["format"] = f["format"]
                dict[index]["width"] = f["width"]
                dict[index]["height"] = f["height"]
                dict[index]["resolution"] = f'{f["height"]} x {f["width"]}'
                dict[index]["url"] = f["url"]
                dict[index]["size"] = self.size_sample
                index += 1
        return dict

    def extract_tweet_meta_data(self, tweet_meta_data, tweet_url) -> dict:
        """
        Extract specificed data from ytdl response Tweet data
        """
        dict = {}
        dict["tweet_url"] = tweet_url
        dict["uploader_user_id"] = tweet_meta_data["uploader_id"]
        dict["uploader_display_name"] = tweet_meta_data["uploader"]
        dict["upload_date"] = self.format_date(tweet_meta_data["upload_date"])
        dict["duration"] = self.convert_seconds_to_minutes(tweet_meta_data["duration"])
        dict["thumbnail"] = tweet_meta_data["thumbnail"]
        dict["title"] = tweet_meta_data["title"]
        dict["description"] = tweet_meta_data["description"]
        return dict

    def format_date(self, date) -> date:
        """
        Return date in yyyy-mm-dd, given date in yyyymmddd
        """
        return datetime.strptime(date, "%Y%m%d").strftime("%d-%m-%Y")

    def convert_seconds_to_minutes(self, time_in_secs) -> str:
        """
        Return time in minutes without microseconds, given in seconds
        """
        return str(timedelta(seconds=time_in_secs)).split(".")[0]

    def extract_tweet_status_info(self, tweet_url: HttpUrl) -> dict:
        """
        Given a valid twitter status URL, it will return
        a media object containing tweet info:
        -  **tweet_meta_data**: Contain tweet meta data, author user name, upload_date etc.
        -  **tweet_medias**:  Contain tweet media direct link, resolution.
        """
        dict_tweet_data_extracted = {}
        try:
            with youtube_dl.YoutubeDL(self.ydl_options) as ydl:
                tweet_info_data = ydl.extract_info(tweet_url, download=False)
                tweet_media_formats = tweet_info_data.get("formats", [tweet_info_data])
        except:
            raise "There's no video in this tweet"
        try:
            dict_tweet_data_extracted["tweet_meta_data"] = self.extract_tweet_meta_data(
                tweet_info_data, tweet_url
            )
            dict_tweet_data_extracted["tweet_medias"] = self.extract_tweet_media_resolutions(
                tweet_media_formats
            )
        except:
            raise "There's no video in this tweet"
        return dict_tweet_data_extracted