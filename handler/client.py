from aiogram import types, Dispatcher
from keyboard import kb_main


async def send_welcome(message: types.Message):
    await message.reply("Hello", reply_markup=kb_main)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=["start"])