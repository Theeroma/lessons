from aiogram import Bot, Dispatcher, types, executor
from config import token 
import logging

bot = Bot(token=token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO) 

direction_buttons = [
    types.KeyboardButton('О нас'),
    types.KeyboardButton('Объекты'),
    types.KeyboardButton('Контакты') 
] 

direction_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*direction_buttons)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer(f"Здравствуйте {message.from_user.full_name}!\nВыберите что вы хотите узнать", reply_markup=direction_keyboard) 

@dp.message_handler(text='О нас') 
async def backend(message:types.Message):
    await message.reply("""Мы - развивающаяся компания, которая предлагает своим клиентам широкий выбор квартир в объектах расположенных во всех наиболее
 привлекательных районах городов Ош и Джалал-Абад. У нас максимально выгодные условия, гибкий (индивидуальный) подход при реализации жилой и коммерческой недвижимости.
 Мы занимаем лидирующие позиции по количеству объектов по югу Кыргызстана. Наша миссия: Мы обеспечиваем население удобным жильем для всей семьи, проявляя лояльность и индивидуальный подход и обеспечивая высокий уровень обслуживания.
 Мы обеспечиваем бизнес подходящим коммерческим помещением, используя современные решения и опыт профессионалов своего дела.""") 
  
@dp.message_handler(text='Объекты')
async def backend(message:types.Message):
    await message.reply("""Наши завершенные объекты""") 
    await message.answer_photo('https://sp-ao.shortpixel.ai/client/to_webp,q_glossy,ret_img,w_1260,h_708/https://vg-stroy.com/wp-content/uploads/2022/01/dji_0392-scaled-1.jpeg')

@dp.message_handler(text='Контакты')
async def backend(message:types.Message):
    await message.reply("""г.Ош, ул.Аматова 1, Бизнес центр Томирис

contact@vg-stroy.com
+996 709 620088
+996 772 620088
+996 550 620088""") 
    
executor.start_polling(dp)