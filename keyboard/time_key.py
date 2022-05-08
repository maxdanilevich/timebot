from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


button_rm_kb = KeyboardButton('Remove keyboard')
button_contact = KeyboardButton('Send my contact', request_contact=True)
button_location = KeyboardButton('Send my location', request_location=True)


kb_main = ReplyKeyboardMarkup(resize_keyboard=True)

kb_main.row(button_location, button_contact).add(button_rm_kb)