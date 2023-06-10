from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

bt1 = KeyboardButton('🏢 Buy')
bt2 = KeyboardButton('🏦 Sell')
bt5 = KeyboardButton('📊 How is profitability calculated?')
bt6 = KeyboardButton('🚫 Cancel')

main_menu = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True).add(bt1, bt2, bt5)
main_menu2 = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True).add(bt1, bt2, bt5, bt6)

Backint1 = InlineKeyboardButton(text='Return keyboard', callback_data='back_kb')

backinbt = InlineKeyboardMarkup().add(Backint1)
