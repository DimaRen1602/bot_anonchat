import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import register_handlers

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Регистрация обработчиков
    register_handlers(dp)

    # Запуск бота
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
