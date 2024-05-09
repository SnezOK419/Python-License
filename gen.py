import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_license_key():
    key = '-'.join([''.join(random.choices(string.ascii_uppercase + string.digits, k=4)) for _ in range(4)])
    key_label.config(text=f"{key}")

root = tk.Tk()
root.geometry('330x200')
root.title("Генератор лицензионного ключа")

generate_button = tk.Button(root, text="Генерировать ключ", command=generate_license_key)
generate_button.pack()

def copy_to_clipboard():
    root.clipboard_clear()  # Очистить буфер обмена
    root.clipboard_append(key_label['text'])  # Добавить текст в буфер обмена

generate_button = tk.Button(root, text="Скопировать", command=copy_to_clipboard)
generate_button.pack()

key_label = tk.Label(root, text="")
key_label.pack()

root.mainloop()