# def say_hello():                                   # функция кнопки
#    print('Hello!')

def add_lebel():  # функция кнопки
    lebel = tk.Label(win, text='new')
    lebel.pack()


def counter():  # функция кнопки счетчика
    global count
    count += 1
    btn4['text'] = f'Счетчик: {count}'
    return count


count = 0
import tkinter as tk

win = tk.Tk()  # создание главного окна

photo = tk.PhotoImage(file='ugol.png')  # icons png fun   # загрузка фото в переменную photo
win.iconphoto(False, photo)  # в углу окна иконка

win.config(bg='#843636')  # цвет фона окна  или в rgb online (код цвета)

win.title('Мое первое окно')  # название окна
win.geometry(f'500x600+20+20')  # размер окна + расположение
win.resizable(True, True)  # возможность изменять размер окна во время работы (ширина высота
win.minsize(500, 600)  # минимально допустимый размер окна
win.maxsize(1000, 1000)  # максимально допустимый размер окна

# btn1 = tk.Button(win, text = 'Hello',                   # создание кнопки
#                 command = say_hello,
#
#
#                 )

btn2 = tk.Button(win, text='New',  # создание кнопки
                 command=add_lebel,

                 )

# btn3 = tk.Button(win, text = 'New lebel',                   # создание кнопки
#                 command = lambda: tk.Label(win, text = 'new lambda').pack()
#                 )


btn4 = tk.Button(win, text=f'Счетчик: {count}',  # кнопка счетчик
                 command=counter,
                 activebackground='blue',  # цвет кнопки при нажатии
                 # state = tk.DISABLED,                       # деактивация кнопки
                 bg='red',
                 )

# btn1.pack()                                             # инициализация и размещение кнопки
btn2.pack()
# btn3.pack()
btn4.pack()

# label_1 = tk.Label(win, text = 'Hello!',               # создание лэйблы
#                   bg = 'red',                         # цвет фона лэйблы
#                   fg = 'white',                       # цвет букв текста
#                   font = ('Arial', 20, 'bold'),      # свойства ('шрифт', размер, 'тип: обычный, жирный, наклонный...)
#                   padx = 10,                         # отступы по оси Х от текста цветным фоном (в пикселях)
#                   pady = 10,                          # ..............У................
#                   width = 10,                        #.............Х........ (в количестве символов)
#                   height = 10,                        # ............У...........(в символах)
#                   anchor = 'n',                  # размещение текста (n, s, w, e, sw,...) в фоне (работает только при размещении через width и height)
#                   relief = tk.RAISED,            # границы (по умолчанию 2 пикселя)
#                   bd = 20,                       # ширина границы
#                   justify = tk.LEFT              # прижимает (выравнивает) текст к границе
#                   )
# label_1.pack()                                         # вызов лэйблы


win.mainloop()  # главный цикл
