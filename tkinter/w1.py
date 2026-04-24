import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    kilojoules = entry_int.get()
    calories = kilojoules / 4.19
    output_string.set(f'{calories:.2f}')

# window
window = ttk.Window(title = 'My cute app', themename = 'minty', size = (500, 200))

# widget
title_label = ttk.Label(master = window, text = 'Kilojoules to Calories', font = 'Calibri 24 bold')
title_label.pack()

# input field
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int, bootstyle = 'secondary')
button = ttk.Button(master = input_frame, text = 'Converte', command = convert, bootstyle = 'secondary')
entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')
input_frame.pack(pady = 10)

# output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

# run
window.mainloop()