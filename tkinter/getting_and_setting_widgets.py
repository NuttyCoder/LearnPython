import tkinter as tk
from tkinter import ttk

def button_func():
    # get the content of the entry
    entry_text = entry.get

    # update the label
    # label.configure(text =  'some other text')
    label['text'] = entry_text
    entry['state'] = 'disabled'
    print(label.configure())

# window
window = tk.Tk()
window.title('Getting and setting widgets')

# widgets
label = ttk.Label(master = window, text = 'Some text')
label.pack()

entry = ttk.Entry(master = window)
entry.pack()

button = ttk.Button(master = window, text = 'The button', command = button_func)
button.pack()
# checkbutton
check_var = tk.IntVar()
check = ttk.Checkbutton(
    window,
    text = 'checkbox 1',
    command = lambda : print(check_var.get()),
    variable = check_var)
check.pack()


# run
window.mainloop()
