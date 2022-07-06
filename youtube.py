from googleapiclient.discovery import build
import requests
import time


id = 0


def main():
    id = input("You TubeIDを入力して下さい:")
    print(id)
    response = requests.get(
        "https://www.googleapis.com/youtube/v3/channels?part=statistics&id={id}&key=AIzaSyBDCx3PIGQQnXlJ_qSTtjAs6omJ1svWXVk"
    )
    # you_tube_data = response.json()
    print(response.json())
    time.sleep(1)  # ここで1秒止まる

    # dic = response.json()
    # number_d = input("Hacker Newsトップのニュースをいくつ表示しますか？:")
    # for top_page_news in range(0, int(number_d)):
    #     # print(dic[newstopics])
    #     news_id = dic[top_page_news]
    #     contents = requests.get(
    #         f"https://hacker-news.firebaseio.com/v0/item/{news_id}.json?print=pretty"
    #     )
    #     data = contents.json()
    #     print("'title': '", data.get("title"), "', 'Link':", data.get("url", None))

    #     time.sleep(1)  # ここで1秒止まる


if __name__ == "__main__":
    main()
