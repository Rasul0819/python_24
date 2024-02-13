from aiogram import Dispatcher,Bot,types
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from keyboards import main_menu,send_contact,send_location,send_name
from aiogram.types import ReplyKeyboardRemove

from geopy.geocoders import Nominatim

str = MemoryStorage()
token = '6882252431:AAFYe1IxmPl4MCyHOejQRjWs6DhQfRI4bEA'
bot = Bot(token)
dp = Dispatcher(bot,storage=str)
class OrderingState(StatesGroup):
    name = State()
    phone = State()
    address = State()


@dp.message_handler(commands=['start'])
async def send_hi(message:types.Message):
    image = open(file='images/logo.jpg',mode='rb')
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=image,
        caption=f'Salem {message.from_user.first_name}.\nMagazinimizge xosh keldiniz!',
        reply_markup=main_menu
        )
    
@dp.message_handler(text='Order')
async def ordering(message:types.Message, state:FSMContext):
    users_name = await send_name(message.from_user.first_name)
    await message.answer('OO jana zakaz.\n Zakaz qiliw ushin oz atinizdi kiritin',reply_markup=users_name)
    await OrderingState.name.set()

@dp.message_handler(state=OrderingState.name)
async def name(message:types.Message, state:FSMContext):
    async with state.proxy() as info:
        info['name'] = message.text
    await message.answer('endi telefon nomerinizdi kiritin',reply_markup=send_contact)
    await OrderingState.phone.set()

@dp.message_handler(state=OrderingState.phone,content_types=types.ContentTypes.CONTACT)
async def phone(message:types.Contact,state:FSMContext,):
    async with state.proxy() as info:
        info['phone'] = message.contact.phone_number
    await message.answer('endi addresinizdi kiritin',reply_markup=send_location)
    await OrderingState.address.set()
@dp.message_handler(state=OrderingState.address,content_types=types.ContentTypes.LOCATION)
async def address(message:types.Location, state:FSMContext):
    location = geolocator.reverse((message.latitude, message.longitude), language='ru')
    address_string = location.address if location else "Не удалось определить адрес"
    async with state.proxy() as info:
        info['address'] = message.
    await message.answer(f'''Zakaz alindi!,
zakazchik ati:{info['name']},
zakazchiktin nomeri : {info['phone']},
zakazchiktin addresi :{info['address']}
''')
    await state.finish()
    







if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)