import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time


def get_first_news():
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62"
    }

    url = "https://1prime.ru/News/"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    articles_cards = soup.find_all("article", class_="rubric-list__article rubric-list__article_default")

    news_dict = {}
    for article in articles_cards:
        article_header = article.find("h2", class_="rubric-list__article-title")
        article_title = article_header.find('a').text.strip()
        article_url = f'https://1prime.ru{article.find("a").get("href")}'

        article_date_time = article.find('time').get('datetime')
        date_from_iso = datetime.fromisoformat(article_date_time)
        date_time = datetime.strftime(date_from_iso, "%Y-%m-%d %H:%M:%S")
        article_date_timestamp = time.mktime(datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S").timetuple())

        arr_url = article_url.split("/")
        article_cat = arr_url[3]
        article_id = arr_url[-1]
        article_id = article_id[:-5]

        print(f"{article_title} | {article_url} | {article_cat} | {article_id} | {article_date_timestamp}")

        news_dict[article_id] = {
            "article_date_timestamp": article_date_timestamp,
            "article_title": article_title,
            "article_cat": article_cat,
            "article_url": article_url
        }
    with open("news_dict.json", "w") as file:
        json.dump(news_dict, file, indent=4, ensure_ascii=False)


def check_news():
    with open('news_dict.json') as file:
        news_dict = json.load(file)

    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62"
    }

    url = "https://1prime.ru/News/"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    articles_cards = soup.find_all("article", class_="rubric-list__article rubric-list__article_default")

    fresh_news = {}
    for article in articles_cards:
        article_url = f'https://1prime.ru{article.find("a").get("href")}'

        arr_url = article_url.split("/")
        article_cat = arr_url[3]
        article_id = arr_url[-1]
        article_id = article_id[:-5]

        if article_id in news_dict:
            continue
        else:
            article_header = article.find("h2", class_="rubric-list__article-title")
            article_title = article_header.find('a').text.strip()

            article_date_time = article.find('time').get('datetime')
            date_from_iso = datetime.fromisoformat(article_date_time)
            date_time = datetime.strftime(date_from_iso, "%Y-%m-%d %H:%M:%S")
            article_date_timestamp = time.mktime(datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S").timetuple())

            news_dict[article_id] = {
                "article_date_timestamp": article_date_timestamp,
                "article_title": article_title,
                "article_cat": article_cat,
                "article_url": article_url
            }

            fresh_news[article_id] = {
                "article_date_timestamp": article_date_timestamp,
                "article_title": article_title,
                "article_cat": article_cat,
                "article_url": article_url
            }

    with open('news_dict.json', 'w') as file:
        json.dump(news_dict, file, indent=4, ensure_ascii=False)

    return fresh_news
