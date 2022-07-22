from config import WEBHOOK_URL, WEBAPP_HOST, WEBAPP_PORT


async def on_startup(dp):
    print("Bot get started!")
    await bot.set_webhook(WEBHOOK_URL)


if __name__ == '__main__':
    from aiogram import executor
    from loader import dp, bot
    from bot_handlers import news_every_minute
    import asyncio

    loop = asyncio.get_event_loop()
    loop.create_task(news_every_minute())

    executor.start_webhook(dispatcher=dp,
                           webhook_path=WEBHOOK_URL,
                           skip_updates=True,
                           on_startup=on_startup,
                           host=WEBAPP_HOST,
                           port=WEBAPP_PORT)

