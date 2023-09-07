# # from aiogram import Bot, Dispatcher, types, executor
# # from aiogram.contrib.fsm_storage.memory import MemoryStorage
# # from aiogram.dispatcher.storage import FSMContext
# # from aiogram.dispatcher.filters.state import State, StatesGroup
# # from config import token
# # import logging

# # bot = Bot(token=token)
# # storage = MemoryStorage()
# # dp = Dispatcher(bot, storage=storage)
# # logging.basicConfig(level=logging.INFO) #Логирования телеграм бота

# # direction_buttons = [
# #     types.KeyboardButton('Backend'),
# #     types.KeyboardButton('Fronted'),
# #     types.KeyboardButton('UX/Ui'),
# #     types.KeyboardButton('IOS'),
# #     types.KeyboardButton('Android'),
# #     types.KeyboardButton('наш адрес'),
# #     types.KeyboardButton('Записаться на курсы'),
# # ]
# # direction_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*direction_buttons)

# # @dp.message_handler(commands='start')
# # async def start(meesage:types.Message):
#     await meesage.answer(f'Привет!{message.from_user.full_name}!\nВыбери напровление который тебя интересует', reply_markup=direction_keyboard)

# # @dp.message_handler(text='Backend')
# # async def backend(message:types.Message):
# #     await message.answer("""Backend — это внутренняя часть продукта, которая находится на сервере и скрыта от пользователей. 
# # Для ее разработки могут использоваться самые разные языки, например, Python, PHP, Go, JavaScript, Java, С#.

# # Длительноть: 5 месяцев
                         
# # Оплата: 10000 сом в месяц""")
                         
# # @dp.message_handler(text='Fronted')
# # async def fronted(message:types.Message):
# #     await message.answer("""FrontEnd разработчик создает видимую для пользователя часть веб-страницы и его главная задача – точно передать в верстке то, что создал дизайнер,
# #  а также реализовать пользовательскую логику.
                         
# # Длительность: 7 мксяцев
                         
# # Оплата: 10000 сом в месяц""")
                         
# # @dp.message_handler(text='IOS')
# # async def ios(message:types.Message):
# #     await message.answer("""Разработка приложений для Apple – это то, что кажется чем-то закрытым и недоступным.
# #  Действительно, программисты соответствующего направления представляют собой «закрытый клуб». 
# # Попасть туда можно, только если человек владеет «яблочной» продукцией.
                         
# # Длительность: 7 месяцев
                         
# # Оплата: 100000 сом в месяц""")
                         
# # @dp.message_handler(text='UX/UI')
# # async def uxui(message:types.Message):
# #     await message.reply("""UI ― это user interface, пользовательский интерфейс, проще говоря ― оформление сайта: сочетания цветов, шрифты, иконки и кнопки. 
# # UX ― это функционал интерфейса, UI ― его внешний вид
                        
# # Длительность: 3 месяца
                        
# # Оплата: 10000 сом в месяц""")
                        
# # @dp.message_handler(text='Android')
# # async def android(message:types.Message):
# #     await message.reply("""
# # Какой язык основной для создания приложений Android? Порядка 90% приложений, представленных на Play Market, 
# # разработаны на языке программирования Java.
                        
# # Длительность: 7 месяцев
                        
# # Оплата: 10000 сом в месяц""")
                        
# # class EnrollState(StatesGroup):
# #     name = State()
# #     phone = State()
# #     email = State()
# #     course = State()

# # @dp.message_handler(text='Записаться на курсы')
# # async def enroll_courses(message:types.Message):
# #     await message.reply("Оставьте свои данные для записи курсов и наши менеджера вам позвонят")
# #     await message.answer("Ваше имя:")
# #     await EnrollState.name.set()

# # @dp.message_handler(state=EnrollState.name)
# # async def get_phone_number(message:types.Message, state:FSMContext):
# #     await state.update_data(name=message.text)
# #     await message.answer("Ваш телефонный номер:")
# #     await EnrollState.phone.set()

# # @dp.message_handler(state=EnrollState.phone)
# # async def get_emaill(message:types.Message, state:FSMContext):
# #     await state.update_data(phone=message.text)
# #     await message.answer("Ваша почта:")
# #     await EnrollState.email.set()

# # @dp.message_handler(state=EnrollState.email)
# # async def get_course(message:types.Message, state:FSMContext):
# #     await state.update_data(email=message.text)
# #     await message.answer("Какой курс вы выбрали?:")
# #     await EnrollState.course.set()

# # @dp.message_handler(state=EnrollState.course)
# # async def get_all_enroll(message:types.Message, state:FSMContext):
# #     await state.update_data(course=message.text)
# #     await message.answer("Данные были успешно записаны, скоро с вами свяжутся :) ")

# # executor.start_polling(dp) 