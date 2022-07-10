# requestとredirectのインポート

from flask import Flask, render_template, request, redirect, url_for
from config import Customer
import os
import tweepy
from dotenv import load_dotenv
from apiclient.discovery import build


# env読み込み
load_dotenv()
# クライアント変数を作成
bearer_token = os.environ.get("BEARER_TOKEN")
consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_token = os.environ.get("ACCESS_KEY")
access_token_secret = os.environ.get("ACCESS_SECRET_KEY")

# Twitter接続
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# youtube接続
API_KEY = os.environ["API_KEY"]  # .envからAPIキーを取得
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)


app = Flask(__name__)

# トップページ
@app.route("/")
def index():
    customers = Customer.select()
    return render_template("index.html", customers=customers)


# 結果の表示ページ
@app.route("/result")
def result():
    customer = Customer.select().order_by(Customer.id.desc()).get()
    # customer = Customer.select().order_by(Customer.id.desc()).get()
    if customer.bip >= 20000000:
        picture = "ss_god"
    elif customer.bip >= 2000000:
        picture = "s_lion"
    elif customer.bip >= 1500000:
        picture = "a_monky"
    elif customer.bip >= 1000000:
        picture = "b_sheep"
    elif customer.bip >= 750000:
        picture = "c_dog"
    elif customer.bip >= 500000:
        picture = "d_chicken"
    elif customer.bip >= 100000:
        picture = "e_chick"
    elif customer.bip >= 10000:
        picture = "f_frog"
    elif customer.bip >= 0:
        picture = "g_insect"

    customer_bip = "{:,}".format(customer.bip)
    return render_template(
        "result.html", customer=customer, customer_bip=customer_bip, picture=picture
    )


# ランキングの表示ページ
@app.route("/ranking")
def ranking():
    customers = Customer.select()
    return render_template("ranking.html", customers=customers)


# ユーザー追加のルーティング(POSTでアクセス限定)
@app.route("/add", methods=["POST"])
def add_customer():
    """新規顧客を追加する関数"""
    # フォーム入力されたnameを値に受け取る
    name = request.form["name"]

    # Twitter情報
    if request.form["twitter_id"] != "":
        t_id = request.form["twitter_id"]
        user = api.get_user(screen_name=t_id)
        subscribers = user.followers_count
    else:
        t_id = ""
        user = ""
        subscribers = int(0)

    # Youtube情報
    if request.form["y_channel_id"] != "":
        y_channel_id = request.form["y_channel_id"]
        response = (
            youtube.channels()
            .list(part="snippet,statistics", id=y_channel_id)
            .execute()
        )
        subscribers2 = response["items"][0]["statistics"]["subscriberCount"]
    else:
        y_channel_id = ""
        subscribers2 = int(0)

    bip = int(subscribers2) + int(subscribers)

    Customer.create(
        name=name,
        # age=age,
        twitter_id=t_id,
        tw_subscribers=subscribers,
        youtube_id=y_channel_id,
        you_subscribers=subscribers2,
        bip=bip,
    )
    # google_sar = CharField()

    # resultにリダイレクトする
    return redirect(url_for("result"))


if __name__ == "__main__":
    app.run(port=5000, debug=True, host="0.0.0.0")
