import asyncio
import logging
import configparser
from main_api import random_pers, search
from keyboard import Menu
from aiogram import Bot, Dispatcher, executor, types

config = configparser.ConfigParser()
config.read("config.ini")
token = config['Telegram']['token']


bot = Bot(token=token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands="start")
async def start_hand(message: types.Message):
    await message.answer(f"👋 Привет, <b>{message.from_user.first_name}</b>. "
                         f"Я бот навигатор по сериалу '<b>Рик и морти</b>' 👋",
                         parse_mode='html', reply_markup=Menu.markup)


@dp.message_handler()
async def random_pers_foo(message: types.Message):
    await message.answer(f"Идёт обработка подождите")
    try:
        if message.text == "♾Случайный персонаж♾":
            await message.answer(f"{random_pers()}", parse_mode='html')

        elif message.text == "🤷‍♀️Помощь🤷‍♀️":
            await message.answer(f"<b>Вывод</b> информации о персонаже: <b>'rick'</b>", parse_mode="html")

        else:
            await message.answer(f"{search(message.text)}", parse_mode="html")
    except:
        await message.answer(f"😔 Извините я не нашёл 😔")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)