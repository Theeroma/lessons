from aiogram import Bot, Dispatcher, types, executor
from bs4 import BeautifulSoup
from config import token
import requests, logging

bot = Bot(token=token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer(f"Здравствуйте {message.from_user.full_name}")

@dp.message_handler(commands='news')
async def send_news(message:types.Message):
    await message.answer("Отправляю новости...")
    url = 'https://akipress.org/'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'lxml')
    all_news = soup.find_all('a', class_='newslink')
    n = 0
    for news in all_news:
        n += 1
        await message.answer(f'{n}) {news.text}')

executor.start_polling(dp, skip_updates=True)