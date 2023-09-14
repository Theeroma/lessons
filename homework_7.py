import requests
import random
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram .dispatcher.filters.state import State, StatesGroup
from config import token
import os, time, logging, requests
from bs4 import BeautifulSoup

bot = Bot(token = token)
storage = MemoryStorage()
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer(f"привет {message.from_user.full_name}")

@dp.message_handler(commands='info')
async def info(message: types.Message):
    await message.answer("Подождите немного...")
    get_id_video = message.text.split('?')
    current_id = get_id_video[0].split('/')[5]
    
    # Fetch video information from TikTok API
    video_api = requests.get(f'https://api16-normal-c-useast1a.tiktokv.com/aweme/v1/feed/?aweme_id={current_id}').json()
    
    if 'aweme_list' in video_api:
        aweme = video_api['aweme_list'][0]
        desc_video = aweme.get('desc', 'Описание отсутствует')
        author = aweme.get('author', 'Автор неизвестен')
        
        # Send video description and author information
        await message.answer(f"Описание: {desc_video}")
        await message.answer(f"Автор: {author}")
    else:
        await message.answer("Не удалось получить информацию о видео.")

@dp.message_handler()
async def dowload_send_video(message:types.Message):
    await message.answer("Скачиваю видео...")
    get_id_video = message.text.split('?')
    current_id = get_id_video[0].split('/')[5]
    video_api = requests.get(f'https://api16-normal-c-useast1a.tiktokv.com/aweme/v1/feed/?aweme_id={current_id}').json()
    video_url = video_api.get('aweme_list')[0].get('video').get('play_addr').get('url_list')[0]
    if video_url:
        title_video = video_api.get('aweme_list')[0].get('desc')
        print("скачиваем видео...")
        try:
            with open(f'video/{title_video}.mp4','wb') as video_file:
                video_file.write(requests.get(video_url).content)
            print('Видео успешно скачан в шапку video')
        except Exception as error:
            print(f'Error: {error}')
            #отправляем видео тик ток в телеграм
        try:
            with open(f'video/{title_video}.mp4', 'rb') as send_file:
                await message.answer_video(send_file)
        except Exception as error:
            await message.answer(f"Ошибка: {error}")

        author_video = video_api.get("aweme_list")[0].get("author").get("nickname")
        id_video = video_api.get("aweme_list")[0].get('aweme_id')

        sta_id = video_api.get("aweme_list")[0].get('statistics').get('aweme_id')
        comment = video_api.get("aweme_list")[0].get('statistics').get('comment_count')
        digg = video_api.get("aweme_list")[0].get('statistics').get('digg_count')
        dowload = video_api.get("aweme_list")[0].get('statistics').get('download_count')
        play = video_api.get("aweme_list")[0].get('statistics').get('play_count')
        share = video_api.get("aweme_list")[0].get('statistics').get('share_count')
        if title_video != ' ':
            title_video = random.randint(1111, 22222)
            await message.answer(' Описание видео отсутствует')
        else:
            await message.answer(f"описание:{title_video}")
        await message.answer(f"автор видео: {author_video}")
        await message.answer(f"id:{id_video}")
        await message.answer(f'''статистика:
                             статический id: {sta_id},
                             количество комментариев: {comment},
                             количество копеек: {digg},
                             скачанные: {dowload},
                             количество игр: {play},
                             количество поделенных: {share}''')

        
        print("error")
    await message.finish()

import requests, sqlite3
from datetime import datetime, timezone



connect = sqlite3.connect('Laptops.db')
cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS laptops(
               id INTEGER PRIMARY KEY,
               title TEXT,
               price INTEGER,
               created TEXT
               
)''')

connect.commit()

def parsing_sulpak():
    n = 0
    for i in range(1, 21):
        url = f'https://www.sulpak.kg/f/noutbuki?page={i}'
        response = requests.get(url=url)
        soup = BeautifulSoup(response.text, 'lxml')
        # print(response)
        laptops = soup.find_all('div', class_="product__item-name")
        prices = soup.find_all('div', class_="product__item-price")
        # print(laptops)
        for name, price in zip(laptops, prices):
            n += 1
            current_price = "".join(price.text.split())
            print(n, name.text, current_price)
            
            data = datetime.now()
            l = name.text, current_price, data

            cursor.execute('INSERT INTO laptops(title, price, created) VALUES (?, ?, ?)', l)
        connect.commit()
        cursor.execute("SELECT * FROM laptops")



        
parsing_sulpak()