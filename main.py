import tkinter as tk
from tkinter import messagebox

# Симулированная база данных с лицензионными ключами и информацией
database = {
    "ABCD-EFGH-IJKL-MNOP": "Лицензия А",
    "L8JK-BM0I-YQ87-UK7D": "Лицензия B",
    "UDYF-15B4-7PI5-DA3F": "Лицензия C",
    "C3G4-UC83-QD79-WTNH": "Лицензия D",
    "E0GV-B21X-NDKP-YRN1": "Лицензия E",
    "TGR6-B0VV-GMOJ-683Z": "Лицензия F",
}

def check_license_key():
    license_key = entry.get()
    
    if license_key in database:
        messagebox.showinfo("Результат", f"Лицензия найдена: {database[license_key]}")
    else:
        messagebox.showerror("Результат", "Лицензионный ключ не найден в базе данных")

root = tk.Tk()
root.geometry('330x200')
root.title("Проверка лицензионного ключа по базе данных")

label = tk.Label(root, text="Введите лицензионный ключ:")
label.pack()

entry = tk.Entry(root)
entry.pack()

check_button = tk.Button(root, text="Проверить ключ", command=check_license_key)
check_button.pack()

root.mainloop()