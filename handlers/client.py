from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import client_kb
from data_base import sqlite_db


async def start_command(message: types.Message):
    await bot.send_message(
        message.from_user.id, 'This is a bot for buying and selling commercial real estate',
        reply_markup=client_kb.main_menu
    )
    await bot.delete_message(message.from_user.id, message.message_id)


async def buy_magazine(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer('Select a filter')


async def sell_magazine(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer('Select a filter', reply_markup=client_kb.Kbt)


async def back_main(message: types.Message):
    if 'Back' in message.text:
        await message.answer("You are back in the main menu", reply_markup=client_kb.main_menu)


async def delete_kb(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer('Keyboard removed', reply_markup=types.ReplyKeyboardRemove())
    await message.answer('Return?', reply_markup=client_kb.backinbt)


async def backkb(query: types.CallbackQuery):
    await query.message.answer('Keyboard returned', reply_markup=client_kb.main_menu)
    await query.answer()


async def vernutkb(message: types.Message):
    await message.answer('Returned', reply_markup=client_kb.main_menu)


async def profitability(message: types.Message):
    await message.answer('The determining factor for future profitability is the cost of real estate.'
                         ' Only the price of the object is included in the count, but there is a more detailed calculation service, contact @Flauler'
                         '\n\nThe rental cost will be calculated according to the formula:\n                                            N*100%/X=L%\nwhere,'
                         ' N - annual rental flow,\nX - the cost of the object,\nL - "dirty" profitability of your object,'
                         ' without taking into account other operating expenses.')


async def menu(message: types.Message):
    await sqlite_db.sql_read(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands='start')
    dp.register_message_handler(back_main, text='Back')
    dp.register_message_handler(delete_kb, text='Remove')
    dp.register_callback_query_handler(backkb, text='back_kb')
    dp.register_message_handler(vernutkb, text='Cancel')
    dp.register_message_handler(profitability, text='How is profitability calculated?')
    dp.register_message_handler(menu, text='Buy')


# Register the handlers with the dispatcher
def register_handlers(dp: Dispatcher):
    register_handlers_client(dp)
