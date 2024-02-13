import sqlite3

async def db_start():
    global db , cursor
    db = sqlite3.connect('my_db.db')
    cursor = db.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
                   id INTEGER AUTO INCREMENT,
                   name TEXT,
                   phone TEXT,
                   address TEXT,
                   chat_id INTEGER 
        )
''')
    
async def add_user(state):
    async with state.proxy() as info:
        name = info['name']
        phone = info['phone']
        address = info['address']
        chat_id = info['id']

    cursor.execute('''
        INSERT INTO users(name,phone,address,chat_id)
        VALUES(?,?,?,?)
''',(name,phone,address,chat_id))
    db.commit()


async def get_users():
    cursor.execute('SELECT name,phone  FROM users')
    users = cursor.fetchall()
    return users