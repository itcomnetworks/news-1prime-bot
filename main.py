async def on_startup(_):
    print("Bot get started!")


if __name__ == '__main__':
    from aiogram import executor
    from loader import dp, bot
    from bot_handlers import news_every_minute
    import asyncio

    loop = asyncio.get_event_loop()
    loop.create_task(news_every_minute())
    executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=on_startup)


