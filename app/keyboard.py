import sqlite3

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

keyboard_reply = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Расписание')],
    [KeyboardButton(text='Посмотреть замены')],
    [KeyboardButton(text='Расписание экзаменов')]
],
    resize_keyboard=True,
    input_field_placeholder='Выберите действие в меню.'
)
