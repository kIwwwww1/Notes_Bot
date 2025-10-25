from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

class keyboard_text():
    ADD_NOTE = 'Добавить заметку'
    MY_NOTES = 'Мои заметки'
    DELETE_NOTE = 'Удалить'

keyboard_add_note = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=keyboard_text.ADD_NOTE)],
    [KeyboardButton(text=keyboard_text.MY_NOTES)]
], resize_keyboard=True)
