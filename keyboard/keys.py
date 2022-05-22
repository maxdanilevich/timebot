from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


button_menu = KeyboardButton("Меню")
button_order = KeyboardButton("Сделать заказ")
button_feedback = KeyboardButton("Оставить отзыв")
button_rm_kb = KeyboardButton('Скрыть клавиатуру')

kb_main = ReplyKeyboardMarkup(resize_keyboard=True)
kb_main.row(button_menu, button_order).row(button_feedback)
cancel_button = KeyboardButton("Отменить заказ")
kb_cancel = ReplyKeyboardMarkup(resize_keyboard=True)
kb_cancel.add(cancel_button)