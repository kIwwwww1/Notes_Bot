from aiogram import types, Router
from aiogram.filters import CommandStart, Command

user_router = Router()

@user_router.message()
async def command_start(message: types.Message):
    await message.answer(f'Hello {message.from_user.first_name}')