import tkinter as tk
from tkinter import ttk

def button_func():
    print(string_var.get())
    string_var.set(' button pressed')
# window
window = tk.Tk()
window.title('Tkinter Variables')

#tkinter variable
string_var = tk.StringVar()

# widgets
label = ttk.Label(master = window, text = 'label')
label.pack()

entry = ttk.Entry(master = window)
entry.pack()

button = ttk.Button(master = window, text = 'the button', command = button_func)
button.pack()

# exercise
# add another button that changes the text back to 'some text' and that enables entry

def reset_func():
    label['text'] = 'some text'
    entry['state'] = 'enabled'

exercise_button = ttk.Button(master = window, text = 'exercise button', command = reset_func)
exercise_button.pack()

# exercise
# create 2 entry fields and 1 label, they should all be connected via a StringVar
# set a start value of 'test'

exercise_var = tk.StringVar(value = 'test')

entry1 = ttk.Entry(master = window, textvariable = exercise_var)
entry1.pack()
entry2 = ttk.Entry(master = window, textvariable = exercise_var)
entry2.pack()
exercise_label = ttk.Label(master = window, text = 'exercise label')
exercise_label.pack()


#run
window.mainloop()

# Tkinter has inbuilt variables that are designed to work with widgets
# They are automatically updated by a widget and they update a widget
# Although they still store basic data like string, integers & Booleans

# Tkinter has inbuilt variables that are designed to work with widgets
# They are automatically updated by a widget and they update a widget
# Although they still store basic data like string, integers & Booleans
