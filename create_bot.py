from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot

storage = MemoryStorage()


bot = Bot(token='1656629638:AAGbYjZJ8cuS5JBoNJOPQvEkjtx_U54m5Xo')
dp = Dispatcher(bot, storage=storage)
