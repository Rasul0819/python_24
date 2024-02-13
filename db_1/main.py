import sqlite3


db = sqlite3.connect('my_first_db.db')

cursor = db.cursor()


# cursor.execute('''
# 	CREATE TABLE IF NOT EXISTS students(
# 		num INTEGER NOT NULL,
# 		name TEXT NOT NULL,
# 		surname TEXT,
# 		age INTEGER,
# 		phone_num TEXT 
# 		)

# 	''')

# db.commit()
# number = int(input('num='))
# name = input('name=')
# familiyasi = input('surname=')
# age = int(input('age='))
# phone = input('phon=')
# cursor.execute('''
# 	INSERT INTO students(num,name,surname,age,phone_num)

# 	VALUES(?,?,?,?,?)


# 	''',(number,name,familiyasi,age,phone))

# db.commit()

cursor.execute('''
	CREATE TABLE IF NOT EXISTS books(
		id INTEGER NOT NULL,
		name TEXT NOT NULL,
		author TEXT,
		price INTEGER,
		year_realised TEXT,
		pages INTEGER,
		ganres TEXT, 
		)

	''')