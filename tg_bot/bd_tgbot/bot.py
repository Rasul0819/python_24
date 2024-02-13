from aiogram import Dispatcher,Bot,types,executor
from keyboards import registeration,send_phone,admins_menu
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from db import db_start,add_user,get_users


str = MemoryStorage()
API = '6400005701:AAEj2lL4-b829Es1yTttCWNQ1BnUguoBpDQ'
bot = Bot(token=API)
dp = Dispatcher(bot=bot,storage=str)

class RegistrationState(StatesGroup):
    name = State()
    phone = State()
    address = State()

async def on_startup(_):
    await db_start()
    await bot.send_message(chat_id='5570471897',text='Botqa start berildi')

@dp.message_handler(commands=['start'])
async def send_hi(message:types.Message):
    admins_id = 5570471897
    users_id = message.from_user.id
    if users_id == admins_id:
        await message.answer(f'Salem admin!',reply_markup=admins_menu)
        @dp.message_handler(text='Users')
        async def show_users(message:types.Message):
            users = await get_users()
            for i in users:
                await message.answer(text=f'name:{i[0]}, phone:{i[1]}')

    else:
        user = message.from_user.first_name
        await message.answer(f'salem {user}, Magazinizmizge xosh kelipsiz',reply_markup=registeration)

@dp.message_handler(text='📱Registration📱')
async def ordering(message:types.Message, state:FSMContext):
    await message.answer('OO jana zakaz.\n Zakaz qiliw ushin oz atinizdi kiritin')
    await RegistrationState.name.set()

@dp.message_handler(state=RegistrationState.name)
async def name(message:types.Message, state:FSMContext):
    async with state.proxy() as info:
        info['name'] = message.text
    await message.answer('endi telefon nomerinizdi kiritin',reply_markup=send_phone)
    await RegistrationState.phone.set()

@dp.message_handler(state=RegistrationState.phone,content_types=types.ContentTypes.CONTACT)
async def phone(message:types.Contact,state:FSMContext,):
    async with state.proxy() as info:
        info['phone'] = message.contact.phone_number
    await message.answer('endi addresinizdi kiritin')
    await RegistrationState.address.set()
@dp.message_handler(state=RegistrationState.address)
async def address(message:types.Message, state:FSMContext):
    async with state.proxy() as info:
        info['address'] = message.text
        info['id'] = message.from_user.id
    await bot.send_message(chat_id=message.from_user.id,text=f'Registraciya juwmaqlandi')
    await add_user(state)

if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True,on_startup=on_startup)