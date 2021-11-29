import tkinter as tk


def select_all():
    for check in [over_18, commercial, follow]:
        check.select()


def deselect_all():
    for check in [over_18, commercial, follow]:
        check.deselect()


def switch_all():
    for check in [over_18, commercial, follow]:
        check.toggle()


# def show():
#    print('Флажок 18', over_18_value.get())


# over_18_value = tk.StringVar()
# over_18_value.set('No')
# commercial_value = tk.IntVar()  # создание переменной инт типа

win = tk.Tk()  # создание главного окна

win.config(bg='#843636')  # цвет фона окна  или в rgb online (код цвета)
win.title('ВИДЖЕТ')  # название окна
win.geometry(f'500x500+100+200')  # размер окна + расположение

over_18 = tk.Checkbutton(win, text='Вам исполнилось 18 лет?',
                         # variable=over_18_value,
                         # offvalue='No',
                         # onvalue='Yes',
                         )  # создание виджета с галочкой(флажком)
commercial = tk.Checkbutton(win, text='Хотите получать рекламу?')
follow = tk.Checkbutton(win, text='Хототе подписаться на канал?', indicatoron=0)  # в виде кнопки

over_18.pack()
commercial.pack()
follow.pack()

tk.Button(win, text='select_all', command=select_all).pack()  # кнопка выбрать все
tk.Button(win, text='deselect_all', command=deselect_all).pack()  # кнопка снять выбор всего
tk.Button(win, text='switch_all', command=switch_all).pack()  # кнопка меняет выбор всего
# tk.Button(win, text='show', command=show).pack()  # кнопка меняет выбор всего

win.mainloop()
