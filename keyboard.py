from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


class Menu():
    button1 = KeyboardButton("♾Случайный персонаж♾")
    button2 = KeyboardButton("🤷‍♀️Помощь🤷‍♀️")
    markup = ReplyKeyboardMarkup(resize_keyboard=True).add(button1).add(button2)