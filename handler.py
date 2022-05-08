from aiogram import types, Dispatcher
from do_time import not_time
from keyboard import kb_main
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove


async def send_welcome(message: types.Message):
    await message.reply("Hello!", reply_markup=kb_main)


async def rm_kb(message: types.Message):
    await message.reply("Keyboard has been removed.", reply_markup=ReplyKeyboardRemove())


async def date(message: types.Message):
    try:
        parsed_message = message.text.split('.')
        await message.reply(not_time.day_of_week(parsed_message))
    except Exception:
        await message.reply("Некорректное сообщение.")


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=["start"])
    dp.register_message_handler(rm_kb, Text(equals="Remove keyboard", ignore_case=True))
    dp.register_message_handler(date)