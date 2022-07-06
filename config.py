import os
from playhouse.db_url import connect
from dotenv import load_dotenv

# .envの読み込み
load_dotenv()

# データベースへの接続設定
db = connect(os.environ.get('DATABASE'))  # 環境変数に合わせて変更する場合

# 接続NGの場合はメッセージを表示
if not db.connect():
    print("接続NG")
    exit()