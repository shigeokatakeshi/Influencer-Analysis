import os
import tweepy
from dotenv import load_dotenv

# env読み込み
load_dotenv()
# クライアント変数を作成
bearer_token = os.environ.get("BEARER_TOKEN")
consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_token = os.environ.get("ACCESS_KEY")
access_token_secret = os.environ.get("ACCESS_SECRET_KEY")


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def main():
    screen_name = input("twitterIDを入れて下さい")
    user = api.get_user(screen_name=screen_name)
    user_info = [
        # user.id_str,
        # user.screen_name,
        # user.name,
        user.followers_count,
        # user.description,
    ]
    print(user_info)


if __name__ == "__main__":
    main()
