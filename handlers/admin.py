from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db as db
from keyboards import client_kb

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()
    stream = State()
    number = State()

async def cm_start(message: types.Message):
    await FSMAdmin.photo.set()
    await message.reply('Upload a photo\nTo cancel, type "Cancel"', reply_markup=client_kb.main_menu2)

async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Registration cancelled')

async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.reply('Now enter the category')

async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.reply('Enter a description')

async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.reply('Indicate the price')

async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = float(message.text)
    await FSMAdmin.next()
    await message.reply('Indicate the monthly stream')

async def load_god_stream(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['stream'] = message.text
    await FSMAdmin.next()
    await message.reply('Enter your phone number')

async def load_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
    await message.answer('Your property is registered', reply_markup=client_kb.main_menu)
    await db.sql_add_command(state)
    await state.finish()

def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, text='Sell', state=None)
    dp.register_message_handler(cancel_handler, state="*", commands='cancel')
    dp.register_message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state="*")
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(load_god_stream, state=FSMAdmin.stream)
    dp.register_message_handler(load_number, state=FSMAdmin.number)
