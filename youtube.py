import urllib.request
import json
from dotenv import load_dotenv

# env読み込み
load_dotenv()

name = input("チャンネル名を入力してください >")
key = "API_KEY"  # たけしさんが取得したAPIKEYをここに入れてください。（.envに書いて参照してください。）
data = urllib.request.urlopen(
    f"https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername={key}"
    + name
    + "&key="
    + key
).read()
subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
print(subs)
