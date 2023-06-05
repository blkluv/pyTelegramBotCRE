from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import client_kb
from data_base import sqlite_db


async def start_command(message: types.Message):
    await bot.send_message(
        message.from_user.id, 'Это бот для покупки-продажи коммерческой недвижимости',
        reply_markup=client_kb.main_menu
    )
    await bot.delete_message(message.from_user.id, message.message_id)


async def buy_magazine(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer('Выберите фильтр')


async def sell_magazine(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer('Выберите фильтр', reply_markup=client_kb.Kbt)


async def back_main(message: types.Message):
    if 'Назад' in message.text:
        await message.answer("Ты вернулся в главное меню", reply_markup=client_kb.main_menu)


async def delete_kb(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer('Клавиатура убрана', reply_markup=types.ReplyKeyboardRemove())
    await message.answer('Вернуть?', reply_markup=client_kb.backinbt)


async def backkb(query: types.CallbackQuery):
    await query.message.answer('Вернули клавиатуру', reply_markup=client_kb.main_menu)
    await query.answer()


async def vernutkb(message: types.Message):
    await message.answer('Вернулись', reply_markup=client_kb.main_menu)


async def rentabelnost(message: types.Message):
    await message.answer('Определяющий фактор будущей рентабельности — стоимость недвижимости.'
                         ' В подсчёт входит только цена объекта, но есть услуга более подробного рассчёта, обращаться к @Flauler'
                         '\n\nРассчёт арендной стоимости будет происходить по формуле:\n                                            N*100%/X=L%\nгде,'
                         ' N - годовой арендный поток,\nX - стоимость объекта,\nL - "грязная" рентабельность вашего объекта,'
                         ' без учета прочих расходов по эксплуатации объекта.')


async def menu(message: types.Message):
    await sqlite_db.sql_read(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands='start')
    dp.register_message_handler(back_main, text='Назад')
    dp.register_message_handler(delete_kb, text='Убрать')
    dp.register_callback_query_handler(backkb, text='back_kb')
    dp.register_message_handler(vernutkb, text='Отмена')
    dp.register_message_handler(rentabelnost, text='Как рассчитывается рентабельность?')
    dp.register_message_handler(menu, text='Купить')
