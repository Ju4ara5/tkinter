# метод упаковки  'grid' (расположение кнопок или виджетов)


import tkinter as tk

win = tk.Tk()  # создание главного окна

photo = tk.PhotoImage(file='ugol.png')  # icons png fun   # загрузка фото в переменную photo
win.iconphoto(False, photo)  # в углу окна иконка

win.config(bg='#843636')  # цвет фона окна  или в rgb online (код цвета)

win.title('Мое первое окно')  # название окна
win.geometry(f'500x600+20+20')  # размер окна + расположение
win.resizable(True, True)  # возможность изменять размер окна во время работы (ширина высота
win.minsize(500, 600)  # минимально допустимый размер окна
# win.maxsize(1000, 1000)                                  # максимально допустимый размер окна

# btn1 = tk.Button(win, text = 'Hello 1')
# btn2 = tk.Button(win, text = 'Hello 2')
# btn3 = tk.Button(win, text = 'Hello 3')
# btn4 = tk.Button(win, text = 'Hello world 4')
# btn5 = tk.Button(win, text = 'Hello 5')
# btn6 = tk.Button(win, text = 'Hello 6')
# btn7 = tk.Button(win, text = 'Hello 7')
# btn8 = tk.Button(win, text = 'Hello 8')
#
#
# btn1.grid(row=0, column=0)
# btn2.grid(row=0, column=1, stick = 'w')
# btn3.grid(row=1, column=0, stick = 'we')
# btn4.grid(row=1, column=1)
# btn5.grid(row=2, column=0)
# btn6.grid(row=2, column=1, stick = 'e')
# btn7.grid(row=3, column=0,columnspan = 2, stick = 'we')
# btn8.grid(row=0, column=2,rowspan = 4, stick = 'ns')
#
# win.grid_columnconfigure(0,minsize = 200)
# win.grid_columnconfigure(1,minsize = 100)

for i in range(5):
    for j in range(2):
        tk.Button(win, text=f'Hello {i} {j}').grid(row=i, column=j, stick='we')

win.grid_columnconfigure(0, minsize=200)
win.grid_columnconfigure(1, minsize=100)

win.mainloop()
