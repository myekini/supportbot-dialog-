from decouple import config
from googleapiclient.discovery import build



def youtube(title):
    api_key = config("api_key")
    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.search().list(
        part= "id",
        channelId = config("channel_id"),
        q = title,
        type = "video",
        order = "title"
        )

    response = request.execute()
    video_link_array = [f"https://www.youtube.com/watch?v={video['id']['videoId']}" \
                for video in response['items']]
    print(video_link_array)
        
