from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, \
    ReplyKeyboardMarkup, KeyboardButton

bt1 = KeyboardButton('Купить')
bt2 = KeyboardButton('Продать')
bt5 = KeyboardButton('Как рассчитывается рентабельность?')
bt6 = KeyboardButton('Отмена')

main_menu = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True).add(bt1, bt2, bt5)
main_menu2 = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True).add(bt1, bt2, bt5, bt6)

Backint1 = InlineKeyboardButton(text='Вернуть клавиатуру', callback_data='back_kb')

backinbt = InlineKeyboardMarkup().add(Backint1)
