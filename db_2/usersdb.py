import sqlite3

def add_data():
	name = name_e.get()
	surname = surname_e.get()
	course = course_c.get()
	phone_num = phonr_e.get()
	con_time = lang.get()

	cursor.execute('''
		INSERT INTO users(
			name,surname,course,phone_number,con_time)
		VALUES(?,?,?,?,?)

		''',(name,surname,course,phone_num,con_time))
	db.commit()

	

db = sqlite3.connect('my_db.db')

cursor = db.cursor()

cursor.execute('''

	CREATE TABLE IF NOT EXISTS users(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT NOT NULL,
		surname TEXT NOT NULL,
		course TEXT NOT NULL,
		phone_number TEXT NOT NULL,
		con_time TEXT NOT NULL,
		age  INTEGER)

	''')
db.commit()




from tkinter import * 
from tkinter import ttk
window = Tk()
window.geometry("600x300")
window.resizable(False,False)
window.title("TexnoPos")
name_l=Label(window,text="Name:").place(x=5,y=5)
name_e=Entry(window,width=15)
name_e.place(x=60,y=5)
surname_l=Label(window,text="Surname:").place(x=5,y=40)
surname_e=Entry(window,width=15)
surname_e.place(x=60,y=40)
course_l=Label(window,text="Course:").place(x=160,y=5)
course_c= ttk.Combobox(values=["Python", "Rus tili", "C++", "Python Basic"])
course_c.place(x=210,y=5)
phone_l=Label(window,text="Phone:").place(x=160,y=40)
phonr_e=Entry(window,width=23)
phonr_e.place(x=210,y=40)
con_time_l=Label(window,text="Con time:").place(x=360,y=5)
eleven = "11:00"
nine = "09:00"
two = "14:00"
lang = StringVar(value=two) 
header = ttk.Label(textvariable=lang)
eleven = ttk.Radiobutton(text=eleven, value=eleven, variable=lang)
eleven.place(x=410,y=40)
two = ttk.Radiobutton(text=two, value=two, variable=lang)
two.place(x=460,y=40)
nine = ttk.Radiobutton(text=nine, value=nine, variable=lang)
nine.place(x=360,y=40)
b=Button(window,text="Записовать",command=add_data).place(x=250,y=80)
window.mainloop()