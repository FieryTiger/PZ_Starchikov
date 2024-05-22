"""Дан целочисленный список A размера N (< 15). Переписать в новый целочисленный
список B все элементы с нечетными порядковыми номерами (1,3,...) и вывести
размер полученного списка B и его содержимое. Условный оператор не использовать.
Реализовать с помощью библиотеки Tkinter"""
from tkinter import *
from tkinter import ttk
import random
root = Tk()
root.title("Случайные числа")
root.geometry("500x300")


def button_clicked():
    N = random.randint(1, 14)
    A = [random.randint(-100, 100) for i in range(N)]
    B = A[::2]
    label_A_size.config(text=f"Размер списка A: {len(A)}")
    label_A.config(text=f"Список A: {A}")
    label_B_size.config(text=f"Размер списка B: {len(B)}")
    label_B.config(text=f"Список B: {B}")


def close():
    root.destroy()
    root.quit()


button = ttk.Button(root, text="Сгенерировать списки", command=button_clicked)
button.pack(fill=BOTH)

label_A_size = ttk.Label(root, text="")
label_A_size.pack(fill=BOTH)

label_A = ttk.Label(root, text="")
label_A.pack(fill=BOTH)

label_B_size = ttk.Label(root, text="")
label_B_size.pack(fill=BOTH)

label_B = ttk.Label(root, text="")
label_B.pack(fill=BOTH)

root.protocol("WM_DELETE_WINDOW", close)
root.mainloop()
