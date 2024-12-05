import tkinter as tk
from tkinter import ttk

def button_func():
    print("Button clicked")

def button2_func():
    print("Hello")

# create a window
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x500')

# ttk label
label = ttk.Label(master = window, text = 'This is a test')
label.pack()

# tk text
text = tk.Text(master = window)
text.pack()

# ttk entry
entry = ttk.Entry(master = window)
entry.pack()


# ttk label
label = ttk.Label(master = window, text = 'my label')
label.pack()

#ttk button
#button2 = ttk.Button(master = window, text = 'Button2', command = button2_func)
#button2.pack()

#ttk button lambda:  Function
button2 = ttk.Button(master = window, text = 'Button2', command = lambda: print('hello'))
button2.pack()

#ttk button
button = ttk.Button(master = window, text = 'A button', command = button_func)
button.pack()


# exercise
# add one more text label and a button with a function  that prints 'hello'
# the label should say "my label" and be between the entry widget and the button
# run
window.mainloop()
# exercise
# add one more text label and a button with a function  that prints 'hello'
# the label should say "my label" and be between the entry widget and the button
# run
window.mainloop()
