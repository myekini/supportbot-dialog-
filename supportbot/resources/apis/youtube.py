import json
import requests

from decouple import config
from googleapiclient.discovery import build

api_key = config("api_key")
youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.search().list(
    part= "snippet",
    channelId = config("channel_id"),
    q = "COA",
    type = "video",
    order = "title"
    )

response = request.execute()



if __name__ == "__main__":
    full_res = response['items']
    for f in full_res:
        print(f['snippet']['title'])