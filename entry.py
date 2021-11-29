import tkinter as tk


def get_entry():  # функция кнопки
    value = name.get()  # обращение к виджету name(Entry), получаем значение с помощью get()
    if value:  # если value есть:
        print(value)  # вывести значение value
    else:
        print('Empty Entry')


def delete_entry():
    name.delete(0, tk.END)  # удаление всех элементов набраной строки(по индексу)


def submit():
    print(name.get())
    print(password.get())
    delete_entry()  # удаляет текст ввода
    password.delete(0, tk.END)  # удаляет текст пароля


win = tk.Tk()  # создание главного окна

photo = tk.PhotoImage(file='ugol.png')  # icons png fun   # загрузка фото в переменную photo
win.iconphoto(False, photo)  # в углу окна иконка

win.config(bg='#843636')  # цвет фона окна  или в rgb online (код цвета)

win.title('Мое первое окно')  # название окна
win.geometry(f'500x600+20+20')  # размер окна + расположение
win.resizable(True, True)  # возможность изменять размер окна во время работы (ширина высота
win.minsize(500, 600)  # минимально допустимый размер окна

tk.Label(win, text='Имя').grid(row=0, column=0, stick='w')
tk.Label(win, text='Пароль').grid(row=1, column=0, stick='w')
name = tk.Entry(win)  # создание грыфы ввода текста
password = tk.Entry(win, show='*')  # создание грыфы ввода текста (скрывать символы)

name.grid(row=0, column=1, stick='w')  # размещение. инициализация графы
password.grid(row=1, column=1, stick='w')  # размещение. инициализация графы

tk.Button(win, text='get', command=get_entry).grid(row=2, column=0, stick='we')
tk.Button(win, text='delete', command=delete_entry).grid(row=2, column=1, stick='we')
tk.Button(win, text='Submit', command=submit).grid(row=3, column=0, stick='we')
tk.Button(win, text='insert Hello', command=lambda: name.insert(0, 'Hello')) \
    .grid(row=2, column=2, stick='we')  # кнопка вноса в графу готового текста

win.grid_columnconfigure(0, minsize=100)
win.grid_columnconfigure(1, minsize=100)

win.mainloop()

# \ символ переоса строки стоб избежать длинных строк
