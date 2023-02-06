from decouple import config
from googleapiclient.discovery import build



def youtube():
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
    full_res = response['items']
    for f in full_res:
        print(f['snippet']['title'])