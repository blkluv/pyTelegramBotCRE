from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, \
    ReplyKeyboardMarkup, KeyboardButton

bt1 = KeyboardButton('Купить')
bt2 = KeyboardButton('Продать')
# bt3 = KeyboardButton('Помощь')
bt5 = KeyboardButton('Как рассчитывается рентабельность?')
bt6 = KeyboardButton('Отмена')

main_menu = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True).add(bt1, bt2, bt5)
main_menu2 = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True).add(bt1, bt2, bt5, bt6)

Backint1 = InlineKeyboardButton(text='Вернуть клавиатуру', callback_data='back_kb')

backinbt = InlineKeyboardMarkup().add(Backint1)



# main_menu = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True).add(bt1, bt2, bt3, bt5)
# main_menu2 = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True).add(bt1, bt2, bt3, bt5, bt6)
# ibt1 = InlineKeyboardButton('Как рассчитывается рентабельность?', callback_data='kak_rentab')
# ibt2 = InlineKeyboardButton('Есть вопросы? нажмите меня', url='https://t.me/Flauler')
# il = InlineKeyboardMarkup(row_width=1).add(ibt1, ibt2)
