from aiogram import Bot, types, Dispatcher, executor
from config import token
import random

bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer('Я загадал число от 1 до 3 угадайте')

@dp.message_handler(text = ['1', '2', '3'])
async def command_user(message:types.Message):
    user = int(message.text)
    random_bot = random.randint(1, 3)
    if user == random_bot:
        await message.answer('Поздравляю! Вы угадали')
        await message.answer_photo('https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg')
    elif user != random_bot:
        await message.answer('Вы не угадали')
        await message.answer_photo('https://media.makeameme.org/created/sorry-you-lose.jpg')

executor.start_polling(dp)
 
