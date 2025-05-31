import tkinter as tk
from tkinter import ttk
import math
#calculator


class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        
        self.equation = tk.StringVar()
        self.entry = ttk.Entry(root, textvariable=self.equation, font=("Arial", 20))
        self.entry.grid(row=0, column=0, columnspan=6)
        
        self.create_buttons()
    
    def create_buttons(self):
        button_text = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3), ("C", 1, 4), ("(", 1, 5),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3), ("%", 2, 4), (")", 2, 5),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3), ("^", 3, 4), ("log", 3, 5),
            ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3), ("sin", 4, 4), ("cos", 4, 5), ("tan", 4, 6)
        ]
        
        for (text, row, col) in button_text:
            button = ttk.Button(self.root, text=text, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
        
        for i in range(6):
            self.root.grid_columnconfigure(i, weight=1)
        
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
    
    def on_button_click(self, char):
        if char == "=":
            self.calculate()
        elif char == "C":
            self.equation.set("")
        else:
            self.equation.set(self.equation.get() + char)
    
    def calculate(self):
        try:
            expression = self.equation.get()
            expression = expression.replace("^", "**")
            expression = expression.replace("log", "math.log10")
            expression = expression.replace("sin", "math.sin")
            expression = expression.replace("cos", "math.cos")
            expression = expression.replace("tan", "math.tan")
            self.equation.set(eval(expression))
        except Exception as e:
            self.equation.set("Error")

if __name__ == "__main__":
    root = tk.Tk()
    calc = ScientificCalculator(root)
    root.mainloop()
