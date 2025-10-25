from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

yes_or_no = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Да', callback_data='yes_add'), InlineKeyboardButton(text='Нет', callback_data='no_add')]
])