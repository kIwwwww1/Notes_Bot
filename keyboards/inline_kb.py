from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

yes_or_no = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Да', callback_data='yes_add'), InlineKeyboardButton(text='Нет', callback_data='no_add')]
])

# detail_note = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='Посмотерть',callback_data='details')],
# [InlineKeyboardButton(text='Удалить',callback_data='delete_note')]
# ])

detail_note = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Посмотерть',callback_data='details'), InlineKeyboardButton(text='Удалить',callback_data='delete_note')],
])

new_detail_note = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Посмотерть',callback_data='details'), InlineKeyboardButton(text='Удалить',callback_data='delete_note')],
    [InlineKeyboardButton(text='Дальше',callback_data='continue_notes')],
])


