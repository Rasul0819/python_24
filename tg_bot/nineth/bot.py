from aiogram import Dispatcher,Bot,types,executor
from insta_download import insta_video

API = '6979529695:AAEfHLBq_RCX4Vnqt7DtmlEgPGg1crDRFOc'
bot = Bot(API)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_hi(message:types.Message):
    users_name = message.from_user.first_name
    await message.answer(f'Salem {users_name},\nSen bizge ssilka\nAl biz sagan videondi jiberemiz)')
@dp.message_handler()
async def send_video(message:types.Message):
    video = await insta_video(message.text)
    await bot.send_video(chat_id=message.from_user.id,video=video,caption='Videoniz tayin')

if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)

