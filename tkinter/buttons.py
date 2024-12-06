import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.title ('buttons')
window.geometry('600x400')

#button
def button_func():
    print('a basic button')

button_string = tk.StringVar(value = 'A button with string var ')
button = ttk.Button(window, text = 'A simple button', command = button_func, textvariable = button_string)
button.pack()

#run
window.mainloop()
