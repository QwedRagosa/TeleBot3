 # Import library
import aiogram
from main import bot, dp
from aiogram import types
from aiogram.types import Message

keyboard_markup = types.ReplyKeyboardMarkup(row_width=3)
array_keyboard = ['Кнопочка', 'Съесть почку']


# Send message to admin
async def send_to_admin(dp):
	await bot.send_message(chat_id=admin_id, text="Bot start")
 # Start bot using func
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
        keyboard_markup.add(*(types.KeyboardButton(text) for text in array_keyboard))
        await message.answer(text='Здрасть',reply_markup=keyboard_markup)

