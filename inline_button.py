from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

product_menu = InlineKeyboardMarkup()
product_menu.add(InlineKeyboardButton(text="➖"), InlineKeyboardButton(text="count"), InlineKeyboardButton(text="➕"))
