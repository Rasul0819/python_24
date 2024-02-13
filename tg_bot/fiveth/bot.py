from aiogram import Dispatcher,Bot,types
from aiogram.utils import executor
from keyboards import main_menu
token = '6887962309:AAE_xOKGG7gY7PhmrjBYacFwpjPa94YCeCs'
bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler(text='/start')
async def start_func(message:types.Message):
	user = message.from_user
	admin_id = 5570471897
	if user.id ==admin_id:
		await message.answer(text=f'Salem admin :{user.first_name}')
	else:
		await message.answer(text=f'Salem {user.first_name}',reply_markup=main_menu)
		await bot.send_sticker(chat_id=user.id,sticker='CAACAgIAAxkBAANzZbIzR-_R9qLeM8p-CbB65ezrs2gAAoABAAIlA1IPu0fP7zbb65o0BA')

@dp.message_handler(text='Biz haqqimizda')
async def send_photo(message:types.Message):
	file = open(file='images/my_photo.jpg',mode='rb')
	await bot.send_photo(chat_id=message.from_user.id,photo=file,caption='Assalamu aleykum.\nBul menin portfolio ushin jaratqan botim.\nhttps://t.me/RasulAbdikerimov - usi akkauntqa xabarlassaniz boladi')
# @dp.message_handler(content_types=["sticker"])
# async def send_sticker(message:types.Message):
# 	sticker_id = message.sticker.file_id
# 	await message.answer(text=sticker_id)
		
# @dp.message_handler(content_types=["animation"])
# async  def send_animation(message:types.Message):
# 	animation_id = message.animation.file_id

# 	await message.answer(text=animation_id)

if __name__=='__main__':
	executor.start_polling(dp,skip_updates=True)

