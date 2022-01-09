# Библиотеки
from tkinter import *
from tkinter import scrolledtext

# Текст
text = ""
my_list = []

# Комманды
command_list = [
    [],
    [],
    [],
    []
]

# Фундаментальные переменные
q = 1
pointer = 0
step = 0
for letter in text:
    my_list.append(letter)
result = ""


# Интерфейс
def window1():
    def test():
        global my_list
        global result
        my_list = []
        result = ""

        for letter in text:
            my_list.append(letter)

    def command(string):
        global my_list
        global pointer
        global q
        global step
        step += 1

        # Текст под "Шаг | Яч. | Было | Стало"
        temporary = ('{:>3}'.format(str(step)) + " | "'{:>3}'.format(str(pointer))
                     + " | " '{:>4}'.format("'" + my_list[pointer] + "'") + " | " '{:>5}'.format("'" + string[0] + "'")
                     + " | " '{:>5}'.format(string[1]))
        tf.insert(INSERT, f'{temporary}\n')

        # На что менять
        if pointer >= 0:
            my_list.pop(pointer)
            my_list.insert(pointer, string[0])

        # Куда двигать
        if string[1] == ">":
            pointer += 1
        else:
            pointer -= 1

        # На какое состояние менять
        q = int(string[2])

    def calculate():
        global pointer
        global my_list
        global text
        global q
        global result
        global step

        q = 1
        pointer = 0
        step = 0

        while q != 0:
            try:
                if q == 1:
                    if my_list[pointer] == "0":
                        command(command_list[0][0])
                    if my_list[pointer] == "1":
                        command(command_list[0][1])
                    if my_list[pointer] == " ":
                        command(command_list[0][2])
                elif q == 2:
                    if my_list[pointer] == "0":
                        command(command_list[1][0])
                    if my_list[pointer] == "1":
                        command(command_list[1][1])
                    if my_list[pointer] == " ":
                        command(command_list[1][2])
                elif q == 3:
                    if my_list[pointer] == "0":
                        command(command_list[2][0])
                    if my_list[pointer] == "1":
                        command(command_list[2][1])
                    if my_list[pointer] == " ":
                        command(command_list[2][2])
                elif q == 4:
                    if my_list[pointer] == "0":
                        command(command_list[3][0])
                    if my_list[pointer] == "1":
                        command(command_list[3][1])
                    if my_list[pointer] == " ":
                        command(command_list[3][2])
            except IndexError:
                tf.insert(INSERT, f'Указатель вышел за пределы ленты\n')
                q = 0

        tf.insert(INSERT, f'Указатель остановился на яч. - {str(pointer)}\n')

        for character in my_list:
            result += character

        lb_3.configure(text=result)

    def clicked_1():
        global command_list
        global text

        text = ""
        text = str(en_1.get())

        command_list = [[], [], [], []]
        command_list[0].append(str(en_11.get()))
        command_list[0].append(str(en_21.get()))
        command_list[0].append(str(en_31.get()))

        command_list[1].append(str(en_12.get()))
        command_list[1].append(str(en_22.get()))
        command_list[1].append(str(en_32.get()))

        command_list[2].append(str(en_13.get()))
        command_list[2].append(str(en_23.get()))
        command_list[2].append(str(en_33.get()))

        command_list[3].append(str(en_14.get()))
        command_list[3].append(str(en_24.get()))
        command_list[3].append(str(en_34.get()))

        tf.delete(1.0, END)
        tf.insert(INSERT, f'{"Шаг | Яч. | Было | Стало | Сдвиг"}\n')
        test()
        calculate()

    # Окно
    window = Tk()
    window.title("Машина Тьюринга")

    # Лента
    lb_1 = Label(window, text="Лента")
    lb_1.grid(column=0, row=1, pady=(20, 5), padx=(20, 5), sticky=W)

    en_1 = Entry(window, width=35)
    en_1.grid(column=1, row=1, columnspan=4, pady=(20, 5), padx=(5, 20), sticky=W)

    # Результат
    lb_2 = Label(window, text="Результат")
    lb_2.grid(column=0, row=2, pady=(5, 20), padx=(20, 5), sticky=W)

    lb_3 = Label(window, text="-")
    lb_3.grid(column=1, row=2, columnspan=4, pady=(5, 20), padx=(5, 20), sticky=W)

    # Таблица
    # Строка 1
    lb_01 = Label(window, text="Q1")
    lb_01.grid(column=1, row=3, pady=(20, 5), padx=5, sticky=N + S + W + E)

    lb_02 = Label(window, text="Q2")
    lb_02.grid(column=2, row=3, pady=(20, 5), padx=5, sticky=N + S + W + E)

    lb_03 = Label(window, text="Q3")
    lb_03.grid(column=3, row=3, pady=(20, 5), padx=5, sticky=N + S + W + E)

    lb_03 = Label(window, text="Q4")
    lb_03.grid(column=4, row=3, pady=(20, 5), padx=(5, 20), sticky=N + S + W + E)

    # Строка 2
    lb_10 = Label(window, text="0")
    lb_10.grid(column=0, row=4, pady=5, padx=(20, 5), sticky=N + S)

    en_11 = Entry(window, width=4)
    en_11.grid(column=1, row=4, pady=5, padx=5, sticky=N + S)

    en_12 = Entry(window, width=4)
    en_12.grid(column=2, row=4, pady=5, padx=5, sticky=N + S)

    en_13 = Entry(window, width=4)
    en_13.grid(column=3, row=4, pady=5, padx=5, sticky=N + S)

    en_14 = Entry(window, width=4)
    en_14.grid(column=4, row=4, pady=5, padx=(5, 20), sticky=N + S)

    # Строка 3
    lb_20 = Label(window, text="1")
    lb_20.grid(column=0, row=5, pady=5, padx=(20, 5), sticky=N + S)

    en_21 = Entry(window, width=4)
    en_21.grid(column=1, row=5, pady=5, padx=5, sticky=N + S)

    en_22 = Entry(window, width=4)
    en_22.grid(column=2, row=5, pady=5, padx=5, sticky=N + S)

    en_23 = Entry(window, width=4)
    en_23.grid(column=3, row=5, pady=5, padx=5, sticky=N + S)

    en_24 = Entry(window, width=4)
    en_24.grid(column=4, row=5, pady=5, padx=(5, 20), sticky=N + S)

    # Строка 4
    lb_30 = Label(window, text="Пробел")
    lb_30.grid(column=0, row=6, pady=(5, 20), padx=(20, 5), sticky=N + S)

    en_31 = Entry(window, width=4)
    en_31.grid(column=1, row=6, pady=(5, 20), padx=5, sticky=N + S)

    en_32 = Entry(window, width=4)
    en_32.grid(column=2, row=6, pady=(5, 20), padx=5, sticky=N + S)

    en_33 = Entry(window, width=4)
    en_33.grid(column=3, row=6, pady=(5, 20), padx=5, sticky=N + S)

    en_34 = Entry(window, width=4)
    en_34.grid(column=4, row=6, pady=(5, 20), padx=(5, 20), sticky=N + S)

    # Поле
    lb_4 = Label(window, text="Консоль")
    lb_4.grid(column=0, row=7, columnspan=5, pady=(20, 5), padx=20, sticky=N + S + W + E)

    tf = scrolledtext.ScrolledText(window, width=32, height=20)
    tf.grid(column=0, row=8, columnspan=5, pady=(5, 20), padx=20)

    # Кнопки
    bt_1 = Button(window, text="Старт", width=15, command=clicked_1, bg="red", fg="white")
    bt_1.grid(column=0, row=9, columnspan=5, pady=20, padx=20, sticky=N + S + W + E)

    window.mainloop()


window1()
