from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram import types
main_menu = ReplyKeyboardMarkup(resize_keyboard=True)

order = KeyboardButton(text='Order',)
contacts = KeyboardButton(text='Contacts')
main_menu.add(order,contacts)

send_contact = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton(text='Contact jiberiw',request_contact=True))
send_location = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton(text='Address jiberiw',request_location=True))

async def send_name(name):
    return ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton(text=name))

