from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot

storage = MemoryStorage()


bot = Bot(token='6126829707:AAG7JSPYFw0_2x4IqbIAgxHe75Dr4d_sUbA')
dp = Dispatcher(bot, storage=storage)
