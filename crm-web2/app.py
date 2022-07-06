from flask import Flask

app = Flask(__name__)

"""
書くこと
    /index で GETリクエスト がきたら
    index.html というテンプレートをレンダリングする
"""

if __name__ == '__main__':
    app.run(port=5000, debug=True)