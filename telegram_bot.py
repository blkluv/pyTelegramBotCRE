from aiogram.utils import executor
from create_bot import dp
from handlers import client, admin
from data_base import sqlite_db as db


async def on_startup(_):
    print('Бот запущен\nЕго ключ: 1656629638:AAGbYjZJ8cuS5JBoNJOPQvEkjtx_U54m5Xo\n@HaoBot')
    db.sql_start()

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)