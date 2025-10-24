import asyncio
from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from logging import basicConfig, INFO
# 
from config.db_config import create_database
from commands.base_commands import user_router

load_dotenv()

TOKEN=getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    basicConfig(level=INFO)
    create_database()
    dp.include_router(user_router)    
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())