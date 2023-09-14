import schedule
import time
import requests

def perform_request(url):
    try:
        response = requests.get(url).json()
        price = round(float(response['price']), 2)
        
        with open('log.txt', 'a') as log_file:
            log_file.write(f"Текущая цена биткоина: {price} $\n")

    except requests.exceptions.RequestException as e:
        with open('log.txt', 'a') as log_file:
            log_file.write(f'Ошибка при выполнении запроса: {e}\n')
        
    except Exception as e:
        with open('log.txt', 'a') as log_file:
            log_file.write(f'Неожиданная ошибка: {e}\n')

def main():
    url = 'https://api.binance.com/api/v3/avgPrice?symbol=BTCUSDT'
    
    schedule.every(3).seconds.do(perform_request, url) 
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

import requests
import random
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram .dispatcher.filters.state import State, StatesGroup
from config import token
import os, time, logging, requests

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