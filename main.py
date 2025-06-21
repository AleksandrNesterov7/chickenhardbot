import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

goals_kb = ReplyKeyboardMarkup(resize_keyboard=True)
goals_kb.add(KeyboardButton("🔥 Набор массы"))
goals_kb.add(KeyboardButton("💪 Сушка"))
goals_kb.add(KeyboardButton("🧘‍♀️ Здоровье"))

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Привет! 👋 Давай подберём тебе спортивное питание. Какая у тебя цель?", reply_markup=goals_kb)

@dp.message_handler(lambda message: message.text in ["🔥 Набор массы", "💪 Сушка", "🧘‍♀️ Здоровье"])
async def choose_goal(message: types.Message):
    await message.answer(f"Отлично! Ты выбрал цель: *{message.text}*. Скоро мы предложим тебе подходящий бокс 💼", parse_mode="Markdown")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)