import os
import logging
from dotenv import load_dotenv
from default_button import menu_keyboard, menu_detail_keyboard
from aiogram import Bot, Dispatcher, executor, types

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    username = message.from_user.username
    await message.reply(f"Hello  @{username}", reply_markup=menu_keyboard)


@dp.message_handler(lambda message: message.txt == "Menu")
async def menu(message: types.Message):
    await message.reply("Select one of the products  >>> ", reply_markup=menu_detail_keyboard)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
