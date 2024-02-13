from aiogram import Dispatcher,Bot,types
from aiogram.utils import executor

token = '6705655737:AAFn0915iiEriEWY9MYAhBgj3SWG8TMa1gM'
bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler(text=['/start','/baslaw','/bastaw'])
async def send_hi(message:types.Message):
	await message.answer(text=f'Salem {message.from_user.first_name}')

@dp.message_handler()
async def send_error(message:types.Message):
	await message.reply(text='Ne degenindi tusinbedim bratan')



if __name__=='__main__':
	executor.start_polling(dp,skip_updates=True)