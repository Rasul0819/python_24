from aiogram import Dispatcher,Bot,types
from aiogram.utils import executor


token = '6839254043:AAHIkWfL_mNpC185tHiuWBK33PzstxpkmEw'
bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_hi(message:types.Message):
    await message.answer(f'{message.from_user.first_name},добро пожаловать в наш бот!')





@dp.message_handler()
async def send_error(message:types.Message):
    if message.text.isalpha():
        await message.reply('непонятный текст какой-то....')
    elif message.text.isnumeric():
        await message.reply('непонятное число какое-то ....')
    elif message.text.isalnum():
        await message.reply('непонятные буквы и числа...\nЗачем ты так делаешь???')
    else:
        await message.reply('Я тебя не понимаю(')



#/about , /start, 
#message


if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)