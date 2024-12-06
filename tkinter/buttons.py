import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.title ('buttons')
window.geometry('600x400')

#button
def button_func():
    print('a basic button')
    print(radio_var.get())

button_string = tk.StringVar(value = 'A button with string var ')
button = ttk.Button(window, text = 'A simple button', command = button_func, textvariable = button_string)
button.pack()

#checkbutton
check_var = tk.IntVar(value = 10)
check = ttk.Checkbutton(
    window,
    text = 'checkbox 1',
    command = lambda: print(check_var.get()),
    variable = check_var,
    onvalue = 10,
    offvalue = 5)
check.pack()

#radio buttons
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(
    window,
    text = 'radiobutton 1',
    variable = radio_var,
    value = 1,
    command = lambda: print(radio_var.get()))
radio1.pack()

radio2 = ttk.Radiobutton(window, text = 'radiobutton 2', variable = radio_var, value = 2)
radio2.pack()

# create another checkbutton and 2 radio buttons

# radio button:
    # values for the radio button are A and B
    # ticking  either prints the value of the checkbutton
    # ticking the radio button unchecks the checkbutton

# check button:
    # ticking the checkbutton prints the value of the radio button value
    # use tkinter var for Booleans!

# exercise radios

def radio_func():
    print(check_bool.get)

#data
radio_string = tk.StringVar()
check_bool = tk.BooleanVar()
#widgets
exercise_radio1 = ttk.Radiobutton(window, text = 'Radio A', command = radio_func, value = 'A', variable = radio_string)
exercise_radio2 = ttk.Radiobutton(window, text = 'Radio B', command = radio_func, value = 'B', variable = radio_string)
exercise_check = ttk.Checkbutton(window, text = 'exercise check', variable = check_bool)

#layout
exercise_radio1.pack()
exercise_radio2.pack()
exercise_check.pack()
#run
window.mainloop()



