import os
import tkinter as tk
from tkinter import messagebox
import json

filename = 'nama.json'

# Check if the file exists and load data, otherwise initialize with default values
if os.path.exists(filename):
    with open(filename, 'r') as f:
        data = json.load(f)

    if 'level' not in data:
        data['level'] = ''

else:
    data = {'name': '', 'level': ''}
    with open(filename, 'w') as f:
        json.dump(data, f)

# Create the main window
window = tk.Tk()

# Add a label and entry for the name
tk.Label(window, text='Masukkan Nama Anda').pack()
name_entry = tk.Entry(window)
name_entry.insert(tk.INSERT, data['name'])
name_entry.pack()

# Add a label and entry for the level
tk.Label(window, text='Masukkan Level Anda').pack()
level_entry = tk.Entry(window)
level_entry.insert(tk.INSERT, data['level'])
level_entry.pack()

# Define the save command function
def save_command():
    name = name_entry.get()
    level = level_entry.get()
    data = {'name': name, 'level': level}
    with open(filename, 'w') as f:
        json.dump(data, f)
    messagebox.showinfo('Info: ', f'Selamat Datang {name}, Anda adalah Level : {level}')

# Add a save button
tk.Button(window, text='Simpan', command=save_command).pack()

# Run the main loop
window.mainloop()