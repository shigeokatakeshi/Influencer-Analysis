from flask import Flask, render_template
from config import Customer

app = Flask(__name__)

"""
書くこと
    /index で GETリクエスト がきたら
    index.html というテンプレートをレンダリングする
"""


@app.route("/index")
def index():
    # customers変数にCustomerモデルのデータすべてを代入
    customers = Customer.select()
    return render_template("index.html", customers=customers)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
