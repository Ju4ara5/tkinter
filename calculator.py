import tkinter as tk
from tkinter import messagebox


def make_digit_buttton(digit):  # создание кнопок функцией
    return tk.Button(win, text=digit, bd=5, font=('Arial', 13), activebackground='blue',
                     command=lambda: add_digit(digit))


def make_operation_buttton(operation):  # создание кнопок функцией
    return tk.Button(win, text=operation, bd=5, font=('Arial', 13), activebackground='yellow',
                     fg='red',  # цвет текста на кнопках (шрифта)

                     command=lambda: add_operation(operation))


def make_calc_buttton(operation):  # создание кнопок функцией
    return tk.Button(win, text=operation, bd=5, font=('Arial', 13), activebackground='green',
                     fg='red',  # цвет текста на кнопках (шрифта)

                     command=calculate)


def clear():
    calc.delete(0, tk.END)
    calc.insert(0, '0')


def make_clear_buttton(operation):  # создание кнопок функцией
    return tk.Button(win, text=operation, bd=5, font=('Arial', 13), activebackground='red',
                     fg='red',  # цвет текста на кнопках (шрифта)

                     command=clear)


def calculate():
    value = calc.get()
    if value[-1] in '+-*/':  # если последнее значение операция, тогда операция выполнится с предыдущим значением
        value = value + value[:-1]
    calc.delete(0, tk.END)
    try:  # при вводе других символов в калькулятор
        calc.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo('Внимание!', 'Нужно только цифры!!! Вы ввели другие символы!')
        clear()  # после сообщения об ошибки, очистит поле
    except ZeroDivisionError:
        messagebox.showinfo('Ошибка!!!', 'На ноль делить нельзя!')
        clear()


def add_digit(digit):
    value = calc.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    calc.delete(0, tk.END)  # очистка строки
    calc.insert(0, value + digit)  # пропись чисел в строку для набора


def add_operation(operation):
    value = calc.get()
    if value[-1] in "+-*/":  # заменяет знаки операции
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value:  # считает уже прописанную операцию при нажатии +-*/
        calculate()
        value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, value + operation)


def press_key(event):  # функция работы с клавиатуры
    print(repr(event.char))  # repr-проверка события при нажатии на клавишу
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-*/':
        add_operation(event.char)
    elif event.char == '\r':  # \r = Enter(клавиша) был определен с помощью repr
        calculate()


win = tk.Tk()  # создание главного окна

photo = tk.PhotoImage(file='calc.png')  # icons png fun   # загрузка фото в переменную photo
win.iconphoto(False, photo)  # в углу окна иконка

win.config(bg='#843636')  # цвет фона окна  или в rgb online (код цвета)

win.title('Калькулятор')  # название окна
win.geometry('240x270+100+200')  # размер окна + расположение
win.resizable(True, True)  # возможность изменять размер окна во время работы (ширина высота)

win.bind('<Key>', press_key)  # bind-привязать к окну событие-'<Key>' которое обрабатывает нажатие на клавишу\
# и выполняет функцию press_key


calc = tk.Entry(win,  # создание грыфы ввода текста
                justify=tk.RIGHT,  # прижать набор текста в право
                width=15,  # ширина

                )
calc.insert(0, '0')  # заранее набраный текст в окошке калькулятора
calc.grid(row=0, column=0, columnspan=4, stick="we", padx=5, pady=2)  # расположение графы ввода текста

# метод создания кнопок:
# tk.Button(win, text='1', bd=5, font=('Arial', 13), command=lambda: add_digit(1)).grid(row=1, column=0, stick='wens', padx=5, pady=5)
# tk.Button(win, text='2', bd=5, font=('Arial', 13), command=lambda: add_digit(2)).grid(row=1, column=1, stick='wens', padx=5, pady=5)
# tk.Button(win, text='3', bd=5, font=('Arial', 13), command=lambda: add_digit(3)).grid(row=1, column=2, stick='wens', padx=5, pady=5)
# tk.Button(win, text='4', bd=5, font=('Arial', 13), command=lambda: add_digit(4)).grid(row=2, column=0, stick='wens', padx=5, pady=5)
# tk.Button(win, text='5', bd=5, font=('Arial', 13), command=lambda: add_digit(5)).grid(row=2, column=1, stick='wens', padx=5, pady=5)
# tk.Button(win, text='6', bd=5, font=('Arial', 13), command=lambda: add_digit(6)).grid(row=2, column=2, stick='wens', padx=5, pady=5)
# tk.Button(win, text='7', bd=5, font=('Arial', 13), command=lambda: add_digit(7)).grid(row=3, column=0, stick='wens', padx=5, pady=5)
# tk.Button(win, text='8', bd=5, font=('Arial', 13), command=lambda: add_digit(8)).grid(row=3, column=1, stick='wens', padx=5, pady=5)
# tk.Button(win, text='9', bd=5, font=('Arial', 13), command=lambda: add_digit(9)).grid(row=3, column=2, stick='wens', padx=5, pady=5)
# tk.Button(win, text='0', bd=5, font=('Arial', 13), command=lambda: add_digit(0)).grid(row=4, column=0, stick='wens', padx=5, pady=5)
# вызов функций кнопок
make_digit_buttton('1').grid(row=1, column=0, stick='wens', padx=5, pady=5)
make_digit_buttton('2').grid(row=1, column=1, stick='wens', padx=5, pady=5)
make_digit_buttton('3').grid(row=1, column=2, stick='wens', padx=5, pady=5)
make_digit_buttton('4').grid(row=2, column=0, stick='wens', padx=5, pady=5)
make_digit_buttton('5').grid(row=2, column=1, stick='wens', padx=5, pady=5)
make_digit_buttton('6').grid(row=2, column=2, stick='wens', padx=5, pady=5)
make_digit_buttton('7').grid(row=3, column=0, stick='wens', padx=5, pady=5)
make_digit_buttton('8').grid(row=3, column=1, stick='wens', padx=5, pady=5)
make_digit_buttton('9').grid(row=3, column=2, stick='wens', padx=5, pady=5)
make_digit_buttton('0').grid(row=4, column=0, stick='wens', padx=5, pady=5)

make_operation_buttton('+').grid(row=1, column=3, stick='wens', padx=5, pady=5)
make_operation_buttton('-').grid(row=2, column=3, stick='wens', padx=5, pady=5)
make_operation_buttton('/').grid(row=3, column=3, stick='wens', padx=5, pady=5)
make_operation_buttton('*').grid(row=4, column=3, stick='wens', padx=5, pady=5)

make_calc_buttton('=').grid(row=4, column=2, stick='wens', padx=5, pady=5)
make_clear_buttton('C').grid(row=4, column=1, stick='wens', padx=5, pady=5)

win.grid_columnconfigure(0, minsize=60)  # конфигурация по колонам
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

win.grid_rowconfigure(1, minsize=60)  # конфигурация по рядам
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)

win.mainloop()
# ctrl+alt+L  =  отформатировать код (сформировать нормальную структуру)
# ctrl + наводим мышь на имя функции (там где ее вызов) + клик =
# = отправляемся к блоку функции
