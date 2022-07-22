from config import WEBHOOK_URL, WEBAPP_HOST, WEBAPP_PORT, WEBHOOK_PATH
from aiogram import executor
from loader import dp, bot
from bot_handlers import news_every_minute
import asyncio


async def on_startup(dp):
    print("Bot get started!")
    await bot.set_webhook(WEBHOOK_URL)


async def on_shutdown(dp):
    print('Shutting down..')
    await bot.delete_webhook()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(news_every_minute())

    executor.start_webhook(dispatcher=dp,
                           webhook_path=WEBHOOK_PATH,
                           skip_updates=True,
                           on_startup=on_startup,
                           on_shutdown=on_shutdown,
                           host=WEBAPP_HOST,
                           port=WEBAPP_PORT)

