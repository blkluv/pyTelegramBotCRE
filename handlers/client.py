from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import client_kb
from data_base import sqlite_db

# @dp.message_handler(commands='start')
async def start_command(message: types.Message):
    await bot.send_message(
        message.from_user.id, 'Это бот для покупки-продажи коммерческой недвижимости',
        reply_markup=client_kb.main_menu
    )
    await bot.delete_message(message.from_user.id, message.message_id)

# @dp.message_handler(commands='test')
# async def test(message: types.message):
#     global button
#     global reply
#     #    создаем глобальные переменные
#     reply = message.chat.id
#     keyboard_markup = types.InlineKeyboardMarkup()
#     btn = types.InlineKeyboardButton('Button', callback_data='press')
#     keyboard_markup.add(btn)
#     button = await bot.send_message(reply, 'Test', reply_markup=keyboard_markup)
#     await bot.delete_message(message.from_user.id, message.message_id)

# @dp.callback_query_handler(lambda c: c.data == 'press')
# async def delete_test(call: types.CallbackQuery):
#     # types.CallbackQuery просто затычка, если нужна другая доп. функция, можно поставить вместо затычки
#     await button.delete()


# @dp.message_handler(commands='Купить')
async def buy_magazine(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer('Выберите фильтр')


# @dp.message_handler(commands='Продать')
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




'''КНОПКА НАЗАД В ИНЛАЙН'''
# from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
#
# start_text = "ЭтоТест"
# start_keyboard = InlineKeyboardMarkup().add(InlineKeyboardButton(text="Каталог", callback_data="Catalog"))
#
#
# @dp.message_handler(commands='Start2')
# async def start(message: types.Message):
#     await message.answer(start_text, reply_markup=start_keyboard)
#
#
# @dp.callback_query_handler(text="Start2")
# async def start_callback(query: types.CallbackQuery):
#     await query.message.edit_text(text=start_text, reply_markup=start_keyboard)
#
#
# @dp.callback_query_handler(text="Catalog")
# async def catalog(query: types.CallbackQuery):
#     keyboard12 = InlineKeyboardMarkup(row_width=1).add(
#         InlineKeyboardButton(text="Игры", callback_data="Games"),
#         InlineKeyboardButton(text="Фильмы", callback_data="Films"),
#         InlineKeyboardButton(text="Назад", callback_data="Start2")
#     )
#     await query.message.edit_text('Вот наш каталог Тест', reply_markup=keyboard12)
'''КНОПКА НАЗАД В ИНЛАЙН'''


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


# async def help(message: types.Message):
#     await message.answer('Ответы на вопросы. Вопросы будут дополняться', reply_markup=client_kb.il)
#
# @dp.callback_query_handler(lambda c: c.data == 'kak_rentab')
# async def help1(call: types.CallbackQuery):
#     await call.answer('Определяющий фактор будущей рентабельности — стоимость недвижимости.'
#                          ' В подсчёт входит только цена объекта, но есть услуга более подробного рассчёта, обращаться к @Flauler'
#                          '\n\nРассчёт арендной стоимости будет происходить по формуле:\n                                            N*100%/X=L%\nгде,'
#                          ' N - годовой арендный поток,\nX - стоимость объекта,\nL - "грязная" рентабельность вашего объекта,'
#                          ' без учета прочих расходов по эксплуатации объекта.')



def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands='start')
    dp.register_message_handler(back_main, text='Назад')
    dp.register_message_handler(delete_kb, text='Убрать')
    dp.register_callback_query_handler(backkb, text='back_kb')
    dp.register_message_handler(vernutkb, text='Отмена')
    dp.register_message_handler(rentabelnost, text='Как рассчитывается рентабельность?')
    dp.register_message_handler(menu, text='Купить')
    # dp.register_message_handler(help, text='Помощь')