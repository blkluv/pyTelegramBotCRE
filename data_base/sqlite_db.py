import sqlite3 as sq
from create_bot import bot

def sql_start():
    global base, cur
    base = sq.connect('dataCOMMER.db')
    cur = base.cursor()
    if base:
        print('Database connected OK!')
    base.execute('CREATE TABLE IF NOT EXISTS menu('
                 'img TEXT, '
                 'name TEXT , '
                 'description TEXT, '
                 'price INTEGER, '
                 'stream INTEGER, '
                 'number TEXT)'
                 )
    base.commit()

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?, ?, ?, ?)', tuple(data.values()))
        base.commit()

async def sql_read(message):
    for ret in cur.execute('SELECT * FROM menu').fetchall():
        profitability = int(ret[4]*12*100/ret[3])
        if int(profitability) < 5:
            profitability2 = float(ret[4] * 12 * 100 / ret[3])
            profitability = "%.2f" % profitability2
            await bot.send_photo(message.from_user.id, ret[0],
                                 f'{ret[1]}\nDescription: {ret[2]}\nPrice {ret[3]}\nMonthly stream {ret[4]}\nLow profitability {profitability} %')
        elif 5 <= profitability < 20:
            profitability2 = float(ret[4] * 12 * 100 / ret[3])
            profitability = "%.2f" % profitability2
            await bot.send_photo(message.from_user.id, ret[0],
                                 f'{ret[1]}\nDescription: {ret[2]}\nPrice {ret[3]}\nMonthly stream {ret[4]}\nAverage profitability {profitability} %')
        elif 20 <= profitability < 30:
            profitability2 = float(ret[4] * 12 * 100 / ret[3])
            profitability = "%.2f" % profitability2
            await bot.send_photo(message.from_user.id, ret[0],
                                 f'{ret[1]}\nDescription: {ret[2]}\nPrice {ret[3]}\nMonthly stream {ret[4]}\nHigh profitability {profitability} %')
        elif profitability >= 30:
            profitability2 = float(ret[4] * 12 * 100 / ret[3])
            profitability = "%.2f" % profitability2
            await bot.send_photo(message.from_user.id, ret[0],
                                 f'{ret[1]}\nDescription: {ret[2]}\nPrice {ret[3]}\nMonthly stream {ret[4]}\nSuper profitability {profitability} %')
        else:
            await bot.send_message('Error')
