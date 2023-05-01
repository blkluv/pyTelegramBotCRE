import sqlite3 as sq
from create_bot import bot


def sql_start():
    global base, cur
    base = sq.connect('dataCOMMER.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    base.execute('CREATE TABLE IF NOT EXISTS menu('
                 'img TEXT, '
                 'name TEXT , '
                 'description TEXT, '
                 'price INTEGER, '
                 'potok INTEGER, '
                 'nomer TEXT)'
                 )
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?, ?, ?, ?)', tuple(data.values()))
        base.commit()


async def sql_read(message):
    for ret in cur.execute('SELECT * FROM menu').fetchall():
        rentab = int(ret[4]*12*100/ret[3])
        if int(rentab) < 5:
            rentab2 = float(ret[4] * 12 * 100 / ret[3])
            rentab = "%.2f" % rentab2
            await bot.send_photo(message.from_user.id, ret[0],
                                 f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[3]}\nМесячный поток {ret[4]}\nНизкая рентабельность {rentab}' + '%')
        elif 5 <= rentab < 20:
            rentab2 = float(ret[4] * 12 * 100 / ret[3])
            rentab = "%.2f" % rentab2
            await bot.send_photo(message.from_user.id, ret[0],
                                 f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[3]}\nМесячный поток {ret[4]}\nСредняя рентабельность {rentab}' + '%')
        elif 20 <= rentab < 30:
            rentab2 = float(ret[4] * 12 * 100 / ret[3])
            rentab = "%.2f" % rentab2
            await bot.send_photo(message.from_user.id, ret[0],
                                 f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[3]}\nМесячный поток {ret[4]}\nВысокая рентабельность {rentab}' + '%')
        elif rentab >= 30:
            rentab2 = float(ret[4] * 12 * 100 / ret[3])
            rentab = "%.2f" % rentab2
            await bot.send_photo(message.from_user.id, ret[0],
                                 f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[3]}\nМесячный поток {ret[4]}\nСверхрентабельность {rentab}' + '%')
        else:
            await bot.send_message('Ошибка')