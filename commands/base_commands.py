from email import message
from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
from sqlalchemy.orm import Session
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from datetime import datetime
# 
from config.db_config import engine, User, Note
from keyboards.reply_kb import keyboard_add_note, keyboard_text
from keyboards.inline_kb import yes_or_no, detail_note, new_detail_note

user_router = Router()

note_for_add = []
all_user_notes = []

class AwaitNote(StatesGroup):
    user_note = State()


@user_router.message(CommandStart())
async def command_start(message: types.Message):
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    try:
        with Session(engine) as session:
            user = session.query(User).filter_by(tg_id=user_id).first()
        if user is None:
            user = session.add(User(tg_id=user_id, first_name=user_first_name))
            session.commit()
            await message.answer(f'Привет {user_first_name}!', reply_markup=keyboard_add_note)
        else:
            await message.answer(f'И сново привет {user_first_name}', reply_markup=keyboard_add_note)
    except Exception as e:
        await message.answer('Произошла ошибка')

@user_router.message(F.text == keyboard_text.ADD_NOTE)
async def command_add_note(message: types.Message, state: FSMContext):
    await message.answer('Введите заметку')
    await state.set_state(AwaitNote.user_note)

@user_router.message(AwaitNote.user_note)
async def user_note_command(message: types.Message, state: FSMContext):
    note_for_add.clear()
    note_for_add.append(message.text)
    await message.answer('Добавить заметку?', reply_markup=yes_or_no)
    await state.clear()


@user_router.callback_query(F.data == 'yes_add')
async def await_yes_add(callback: types.CallbackQuery):
    try:
        with Session(engine) as session:
            session.add(Note(tg_id=callback.from_user.id, note=note_for_add[0]))
            await callback.answer('Ваша заметка добавлена')
            await callback.message.chat.delete_message(message_id=callback.message.message_id)
            note_for_add.clear()
    except Exception as e:
        await callback.message.answer(f'Произошла ошибка {e}')
        

@user_router.callback_query(F.data == 'no_add')
async def await_no_add(callback: types.CallbackQuery):
    note_for_add.clear()
    await callback.answer('Заметка удалена')
    await callback.message.chat.delete_message(message_id=callback.message.message_id)

@user_router.message(F.text == keyboard_text.MY_NOTES)
async def user_notes(message: types.Message):
    try:
        with Session(engine) as session:
            user = session.query(User).filter_by(tg_id=message.from_user.id).first()
            user_notes = [i for i in user.notes]
        print('Сессия закрыта')
        len_page = 3
        start_index = 0
        while True:
            end_index = start_index + len_page
            for user_note in user_notes[start_index:end_index]:
                user_note_message = f'{user_note.note[:15].strip()} . . .\n\n{user_note.adding_time.strftime(f'%H:%M | %Y-%m-%d')}'
                await message.answer(user_note_message, reply_markup=detail_note)
                if end_index >= len(user_notes):
                    await message.answer('Все заметки!')
                    break
                start_index += end_index
            break
    except Exception as e:
        await message.answer(f'Произошла ошибка {e}')






    
@user_router.message()
async def other_command(message: types.Message):
    await message.answer('Не понимаю твою команду')