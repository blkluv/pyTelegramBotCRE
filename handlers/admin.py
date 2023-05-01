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
    potok = State()
    nomer = State()


# @dp.message_handler(commands='Загрузить', state=None)
async def cm_start(message: types.Message):
    await FSMAdmin.photo.set()
    await message.reply('Загрузите фото\nЧтобы вернуться пропишите "Отмена"', reply_markup=client_kb.main_menu2)


async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Отмена регистрации')


# @dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.reply('Теперь введите категорию')


# @dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.reply('Введи описание')


# @dp.message_handler(state=FSMAdmin.description)
async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.reply('Укажи цену')


# @dp.message_handler(state=FSMAdmin.price)
async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = float(message.text)
    await FSMAdmin.next()
    await message.reply('Укажи месячный поток')


async def load_god_potok(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['potok'] = message.text
    await FSMAdmin.next()
    await message.reply('Введите ваш номер телефона')

async def load_nomer(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['nomer'] = message.text
    await message.answer('Ваше помещение зарегистрировано', reply_markup=client_kb.main_menu)
    await db.sql_add_command(state)
    await state.finish()


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, text='Продать', state=None)
    dp.register_message_handler(cancel_handler, state="*", commands='отмена')
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(load_god_potok, state=FSMAdmin.potok)
    dp.register_message_handler(load_nomer, state=FSMAdmin.nomer)

