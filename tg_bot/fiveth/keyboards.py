#oop
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
order_btn = KeyboardButton(text='Buyirtpa beriw')
about_btn = KeyboardButton(text='Biz haqqimizda')
feed_back_btn = KeyboardButton(text='Bizge xabar jollaw')
my_orders_btn = KeyboardButton(text="Menin' buyirtpalarim")

main_menu.add(order_btn)
main_menu.add(my_orders_btn,about_btn)
main_menu.add(feed_back_btn)


