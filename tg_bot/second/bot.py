from aiogram import Dispatcher,Bot,types
from aiogram.utils import executor

token = '6705655737:AAFn0915iiEriEWY9MYAhBgj3SWG8TMa1gM'
bot = Bot(token)
dp = Dispatcher(bot)


@dp.message_handler(text=['/start'])
async def send_hi(message:types.Message):
	await message.answer(text=f'Salem {message.from_user.first_name}')

@dp.message_handler(text=['Привет'])
async def send_hi(message:types.Message):
	await message.asnwer(text=f'Привет {message.from_user.first_name}')

@dp.message_handler(text=['/info'])
async def send_hi(message:types.Message):
	user = message.from_user
	info_text = f'Имя{user.first_name}\nID:{user.id}\nSurname:{user.last_name}\nUsername:{user.username}'
	await message.reply (info_text)


@dp.message_handler()
async def send_error(message:types.Message):
	number = message.text
	int_num = int(number)
	if int_num%2==0:
		await message.reply(text='jibergen saniniz jup san')



if __name__=='__main__':
	executor.start_polling(dp,skip_updates=True)
