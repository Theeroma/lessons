# from aiogram import Bot, Dispatcher, types, executor

# bot = Bot(token='6623455907:AAECxwfH8Twj0xMBnEFRFeW6DrBi8l2d6EE')
# dp = Dispatcher(bot)

# @dp.message_handler(commands='start')
# async def start(message:types.Message):
#     await message.answer('hello Geeks!')

# @dp.message_handler(commands='go')
# async def command_go(message:types.Message):
#     await message.answer('Комманда go сработала')

# @dp.message_handler(text='Привет')
# async def hello(message:types.Message):
#     await message.answer('Привет, как дела?')

# @dp.message_handler(commands='test')
# async def testing(message:types.Message):
#     await message.reply('message.answer выделяет текст и отвечает вот так')
#     await message.answer_dice()
#     await message.answer_location(40.527666, 72.835742)
#     await message.answer_photo('https://www.google.com/imgres?imgurl=https%3A%2F%2Fstatic.tildacdn.com%2Ftild3863-3635-4138-b133-613431396662%2F230124-237_2.jpg&tbnid=WP-2iRUPd3WNDM&vet=12ahUKEwjr6dHd6uiAAxXWgSoKHZOnBkMQMygAegQIARBI..i&imgrefurl=https%3A%2F%2Fgeeks.edu.kg%2F&docid=XjR6MQDhXkt7rM&w=1680&h=1120&q=geeks&client=safari&ved=2ahUKEwjr6dHd6uiAAxXWgSoKHZOnBkMQMygAegQIARBI')
#     await message.answer_contact('0501404074', 'Roma', 'Kadyrov')
#     with open('voice.m4a', 'rb') as voice:
#          await message.answer_voice


# executor.start_polling(dp) 