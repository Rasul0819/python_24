from aiogram.types import KeyboardButton,ReplyKeyboardMarkup


main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
registeration = ReplyKeyboardMarkup(resize_keyboard=True)
reg = KeyboardButton(text='📱Registration📱')
registeration.add(reg)


send_phone = ReplyKeyboardMarkup(resize_keyboard=True)
phone = KeyboardButton(text="📱Share contact📱",request_contact=True)
send_phone.add(phone)


admins_menu=ReplyKeyboardMarkup(resize_keyboard=True)
show_users = KeyboardButton(text='Users')
admins_menu.add(show_users)

