# from aiogram import Bot, Dispatcher, types, executor
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.dispatcher.storage import FSMStorageWarning
# from aiogram.dispatcher.filters.state import State, StatesGroup
# from config import token
# import logging

# bot = Bot(token=token)
# storage = MemoryStorage()
# dp = Dispatcher(bot, storage=storage)
# logging.basicConfig(level=logging.INFO) #Логирование телеграм бота

# direction_button = [
#     types.KeyboardButton('Backend'),
#     types.KeyboardButton('Frontend'),
#     types.KeyboardButton('UX/UI'),
#     types.KeyboardButton('Android'),
#     types.KeyboardButton('IOS'),
#     types.KeyboardButton('Наш адрес'),
#     types.KeyboardButton('Записаться на курсы')
# ]
# direction_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*  direction_button)

# @dp.message_handler(commands='start')
# async def start(message:types.Message):
#     await message.answer(f'Привет{message.from_user.full_name}!\n Выбери направление которое тебя интересует'
# ,reply_markup=direction_keyboard)

# @dp.message_handler(text='Backend')
# async def backend(message:types.Message):
#     await message.reply(""" Backend — это внутренняя часть продукта, 
# которая находится на сервере и скрыта от пользователей.
#  Для ее разработки могут использоваться самые разные языки, 
# например, Python, PHP, Go, JavaScript, Java, С#.""")


# @dp.message_handler(text='Frontend')
# async def frontend(message:types.Message):
#     await message.reply("""FrontEnd разработчик создает видимую для пользователя часть 
# веб-страницы и его главная задача – точно передать в верстке то, что создал дизайнер, 
# а также реализовать пользовательскую логику.
#     Длительность: 7 месяцев  
                        

#     Оплата 10000 """)




# @dp.message_handler(text='UX/UI')
# async def ux(message:types.Message):
#     await message.reply("""UX/UI-дизайнер ― одна из самых востребованных сегодня профессий на рынке.
#  В этом материале мы подробно разбираем,
#  кто такой UX/UI-дизайнер и почему UX/UI-дизайн ― не только про графику.""")




# @dp.message_handler(text='UX/UI')
# async def ux(message:types.Message):
#     await message.reply("""Он создает и поддерживает приложения на операционной системе Android. 
# На ней работают не только смартфоны, 
# но и планшеты, умные часы, а также Smart TV. Именно от разработчика зависит,
#  насколько удобным и функциональным будет приложение""")


# @dp.message_handler(text='IOS')
# async def ios(message:types.Message):
#     await message.reply("""iOS-разработчик создает приложения для устройств Apple.
#  Это не только iPhone, но и iPad, Apple Watch и другие гаджеты,
#      входящие в экосистему. Он не только пишет код и работает над интерфейсом,
#  но и занимается поддержкой приложения, адаптацией его под разные модели устройств, 
#     тестированием и исправлением багов.""")

# @dp.message_handler(text='Наш адрес')
# async def get_adress(nessage:types.Message):
#     await message.answer("Наш адрес: г.Ош Аматова 1Б (БЦ Томирис)/n+996557018090 - Рома")
#     await message.answer_location(40.51926624788319, 72.80300022670745)
#     await message.answer_photo('https://vg-stroy.com/wp-content/uploads/2022/01/2022-02-09-14.22.54.jpg')

# class EnrollState(StatesGroup):
#     name = State()
#     phone = State()
#     email = State()
#     course = State()

# @dp.message_handler(text='Записаться на курсы')
# async def enroll_courses(message:types.Message):
#     await message.reply("Оставьте свои данные для записи курсов и наши менеджера вам позвонят")
#     await message.answer("Ваше имя:")
#     await EnrollState.name.set()

# @dp.message_handler(state=EnrollState.name)
# async def get_phone_number(message:types.Message, state:FSMContext):
#     await message.answer("Ваш телефонный номер:")
#     await EnrollState.phone.set()

# @dp.message_handler(state=EnrollState.phone)
# async def get_email(message:types.Message, state:FSMContext):
#     await state.update_data(phone=message.text)
#     await message.answer("Какой курс вы выбрали?")
#     await EnrollState.course.set()

# @dp.message_handler(state=EnrollState.course)
# async def get_all_enroll(message:types.Message, state:FSMContext):
#     await state.update_data(course=message.text)
#     await message.answer("Данные были успешно записано")

# executor.start_polling(dp)

