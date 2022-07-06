from flask import Flask, render_template

app = Flask(__name__)


# おみくじアプリルーティング
@app.route("/omikuji")
def omikuji():
    # 変数を作成
    result = "大吉!!"
    # テンプレートでresult変数を使用する
    return render_template("omikuji.html", result=result)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
