import tkinter as tk
from tkinter import ttk
import sqlite3


# Функция создания\зиполнение таблици
def add(name, tel, meil, zp):
    
    # Установка соединения с базой данных
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # Создание таблицы
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            number TEXT,
            email TEXT,
            zp INT
        )
    ''')
    # Заполнение таблицы данными
    cursor.execute('INSERT INTO contacts (name, number, email, zp) VALUES (?, ?, ?, ?)', (name, tel, meil, zp)) 
    # Сохранение изменений и закрытие соединения
    conn.commit()
    conn.close()


# Функция удоляюшая удоления запеси из таблици
def delete(name):
    # Подключение к базе данных
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # Запрос на удаление записи
    cursor.execute("DELETE FROM contacts WHERE name = ?", (name,))
    # Сохранение изменений и закрытие соединения
    conn.commit()
    conn.close()


# Функция выводяшяя информацию о объекте
def info(name):
    # Подключение к базе данных
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # запрос
    cursor.execute("SELECT * FROM contacts WHERE  name = ?", (name,))
    results = cursor.fetchall()
    # закрываем соединение
    conn.close()
    # возрашаем картеж с даными по запросу
    return results
    

# Функция обновляюшая даные о объекте
def update(name, tel, emeil, zp):
    # Удоляем старуюю запись
    delete(name)
    # Подключение к базе данных
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO contacts (name, number, email, zp) VALUES (?, ?, ?, ?)', (name, tel, emeil, zp))
    # Сохранение изменений и закрытие соединения
    conn.commit()
    conn.close


# Функция выводяшию информацию о всех оъектах
def info_full():
    # Подключение к базе данных
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # запрос
    cursor.execute("SELECT * FROM contacts")
    results = cursor.fetchall()
    # закрываем соединение
    conn.close()
    # возрашаем картеж с даными по запросу
    return results


# Функция обновление таблици
def table_updation():
    # Очишаем таблиу
    tree.delete(*tree.get_children())

    # Добавляем данные определяем данные для отображения
    employee = info_full()

    # Заполняем таблицу
    for person in employee:
        tree.insert("", tk.END, values=person)


# Создание окна
root = tk.Tk()
# Название окна
root.title("Список сотрудников компании")
# Размер окна
root.geometry("965x450")


# Функция запускаемая при нажатии на кнопку добавить
def btn1_clicked():
    # Функция оброботки данных
    def handler():  
        # Получаем данные и обробатываем данные    
        name = input_name.get()
        tel = input_tel.get()
        emeil = input_emeil.get()
        # zp на входе мы получаем str а в базе даных используется int
        zp = int(input_zp.get())
    
        # Записаваем в таблицу (бд)
        add(name, tel, emeil, zp)
        # Обновление таблици
        table_updation()
        # Закрыть всплываюшее окно
        top_level.destroy()
    

    top_level = tk.Toplevel(root)
    # Параметр окна
    top_level.geometry("300x200")
    top_level.title("Создать запись")

    # Надпесь
    label_name = tk.Label(top_level, text="ФИО")
    label_name.pack()
    # Input
    input_name = tk.Entry(top_level)
    input_name.pack()

    # Надпесь
    label_tel = tk.Label(top_level, text="Номер")
    label_tel.pack()
    # Input
    input_tel = tk.Entry(top_level)
    input_tel.pack()

    # Надпесь
    label_emeil = tk.Label(top_level, text="Emeil")
    label_emeil.pack()
    # Input
    input_emeil = tk.Entry(top_level)
    input_emeil.pack()

    # Надпесь
    label_zp = tk.Label(top_level, text="Зарплата")
    label_zp.pack()
    # Input
    input_zp = tk.Entry(top_level)
    input_zp.pack()

    # Кнопка
    button = tk.Button(top_level, text="Сохранить", command=handler)
    button.pack()


# Функция запускаемая при нажатие на кнопку удолить
def btn2_clicked():
    # Функция оброботки данных
    def handler():
        # Получаем данные и обробатываем данные
        name = input_name.get()
        # Удоление записи из таблици (бд)
        delete(name) 
        # Обновление таблици  
        table_updation()   
        # Закрыть всплываюшее окно
        top_level.destroy()


    top_level = tk.Toplevel(root)
    # Параметр окна
    top_level.geometry("300x200")
    top_level.title("Удалить запись")

    # Надпесь
    label_name = tk.Label(top_level, text="ФИО")
    label_name.pack()
    # Input
    input_name = tk.Entry(top_level)
    input_name.pack()

    # Кнопка
    button = tk.Button(top_level, text="Удолить", command=handler)
    button.pack()


# Функция запускаемая при нажатие на кнопку найти
def btn3_clicked():
    # Функция оброботки данных
    def handler():
        # Получаем данные и обробатываем данные
        name = input_name.get() 
       
        # Очишаем таблиу
        tree.delete(*tree.get_children())
        # Добавляем данные определяем данные для отображения
        employee = info(name)
        # Заполняем таблицу
        for person in employee:
            tree.insert("", tk.END, values=person)  

        # Закрыть всплываюшее окно
        top_level.destroy()


    top_level = tk.Toplevel(root)
    # Параметр окна
    top_level.geometry("300x200")
    top_level.title("Найти запись")

    # Надпесь
    label_name = tk.Label(top_level, text="ФИО")
    label_name.pack()
    # Input
    input_name = tk.Entry(top_level)
    input_name.pack()

    # Кнопка
    button = tk.Button(top_level, text="Найти", command=handler)
    button.pack()


# Фунция запускаемая при нажатие на кнопку изменить
def btn4_clicked():
    # Функция оброботки данных
    def handler():
        # Получаем данные и обробатываем данные    
        name = input_name.get()
        tel = input_tel.get()
        emeil = input_emeil.get()
        # zp на входе мы получаем str а в базе даных используется int
        zp = int(input_zp.get())
        # Изменение таблици (бд)
        update(name, tel, emeil, zp)
        # Очишаем таблиу
        tree.delete(*tree.get_children())
        # Обновление таблици  
        table_updation() 
        # Закрыть всплываюшее окно
        top_level.destroy() 
        

    top_level = tk.Toplevel(root)
    # Параметр окна
    top_level.geometry("300x200")
    top_level.title("Изменить запись")

    # Надпесь
    label_name = tk.Label(top_level, text="ФИО")
    label_name.pack()
    # Input
    input_name = tk.Entry(top_level)
    input_name.pack()

    # Надпесь
    label_tel = tk.Label(top_level, text="Номер")
    label_tel.pack()
    # Input
    input_tel = tk.Entry(top_level)
    input_tel.pack()

    # Надпесь
    label_emeil = tk.Label(top_level, text="Emeil")
    label_emeil.pack()
    # Input
    input_emeil = tk.Entry(top_level)
    input_emeil.pack()

    # Надпесь
    label_zp = tk.Label(top_level, text="Зарплата")
    label_zp.pack()
    # Input
    input_zp = tk.Entry(top_level)
    input_zp.pack()

    # Кнопка
    button = tk.Button(top_level, text="Сохранить изменения", command=handler)
    button.pack()


# Картинка для кнопки
update_img_1 = tk.PhotoImage(file="./img/add.png")
update_img_2 = tk.PhotoImage(file="./img/delete.png")
update_img_3 = tk.PhotoImage(file="./img/search.png")
update_img_4 = tk.PhotoImage(file="./img/update.png")
update_img_5 = tk.PhotoImage(file="./img/refresh.png")

# Создаем кнопак:
# Добавить сотрудника
append = tk.Button(root, bg="#d7d8e0", image=update_img_1, bd=0, command=btn1_clicked)
# Удолить сотрудника
delit = tk.Button(root, bg="#d7d8e0", image=update_img_2, bd=0, command=btn2_clicked)
# Писк сотрудника
search = tk.Button(root, bg="#d7d8e0", image=update_img_3, bd=0, command=btn3_clicked)
# Редоктировение сотрудника
edit = tk.Button(root, bg="#d7d8e0", image=update_img_4, bd=0, command=btn4_clicked)
# Обновить
updat = tk.Button(root, bg="#d7d8e0", image=update_img_5, bd=0, command=table_updation)

append.place(x=0, y=0)
delit.place(x=80, y=0)
search.place(x=160, y=0)
edit.place(x=240, y=0)
updat.place(x=320, y=0)

# определяем столбцы
columns = ("id", "name", "tel", "email", "zp")

# определяем данные для отображения
employee = info_full()

tree = ttk.Treeview(columns=columns, show="headings")
tree.pack(expand=1)
tree.delete(*tree.get_children())

# определяем заголовки
tree.heading("id", text="id")
tree.heading("name", text="ФИО")
tree.heading("tel", text="Номер")
tree.heading("email", text="Email")
tree.heading("zp", text="Зарплата")
 
# добавляем данные
for person in employee:
    tree.insert("", tk.END, values=person)
 
# запуск цикла
root.mainloop()