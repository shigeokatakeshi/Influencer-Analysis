from apiclient.discovery import build
import os
from dotenv import load_dotenv

load_dotenv()

CHANNEL_ID = ("HikakinTV")
API_KEY = os.environ["API_KEY"]  # ここたけしさんのAPI KEYに書き換えてください。
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)
response = youtube.channels().list(part="snippet,statistics", id=CHANNEL_ID).execute()

print(response['items'][0]['statistics']['subscriberCount'])

# for item in response.get("items", []):
#     print(item["statistics"]["subscriberCount"])
