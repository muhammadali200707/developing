from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

product_menu = InlineKeyboardMarkup(resize_keyboard=True)
product_menu.add(InlineKeyboardButton(text="➖"), InlineKeyboardButton(text="count"), InlineKeyboardButton(text="➕"))
