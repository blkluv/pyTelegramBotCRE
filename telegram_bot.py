from aiogram.utils import executor
from create_bot import dp
from handlers import client, admin
from data_base import sqlite_db as db


async def on_startup(_):
    print('Bot started\nIts key: 6126829707:AAG7JSPYFw0_2x4IqbIAgxHe75Dr4d_sUbA\nCREBrokerBot')
    db.sql_start()

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)