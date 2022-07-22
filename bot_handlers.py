import asyncio
import datetime

from aiogram.utils.markdown import hbold, hlink

from config import ADMIN_ID, GROUP_ID
from loader import bot
from news_parser import check_news


async def news_every_minute():
    while True:
        fresh_news = check_news()

        if len(fresh_news) >= 1:
            for k, v in sorted(fresh_news.items()):
                news = f"{hbold(datetime.datetime.fromtimestamp(v['article_date_timestamp']))}\n" \
                        f"{hbold(v['article_title'])}\n"\
                       f"{hlink(v['article_title'], v['article_url'])}\n\n" \
                       f"#{v['article_cat']}"
                await bot.send_message(GROUP_ID, news, disable_notification=True)
                #await asyncio.sleep(5)

        else:
            pass
            # await bot.send_message(ADMIN_ID, "Пока нет свежих новостей...", disable_notification=True)

        await asyncio.sleep(60)
