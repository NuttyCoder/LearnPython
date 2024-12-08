import tkinter as tk
from tkinter import messagebox
import sqlite3
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def create_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    username TEXT NOT NULL,
                    password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def add_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hash_password(password)))
    conn.commit()
    conn.close()

def verify_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, hash_password(password)))
    user = c.fetchone()
    conn.close()
    return user

def login():
    username = entry_username.get()
    password = entry_password.get()
    if verify_user(username, password):
        messagebox.showinfo("Login", "Login successful")
    else:
        messagebox.showerror("Login", "Invalid username or password")

def register():
    username = entry_username.get()
    password = entry_password.get()
    add_user(username, password)
    messagebox.showinfo("Register", "User registered successfully")

# GUI setup
app = tk.Tk()
app.title("Login System")

tk.Label(app, text="Username").grid(row=0)
tk.Label(app, text="Password").grid(row=1)

entry_username = tk.Entry(app)
entry_password = tk.Entry(app, show="*")

entry_username.grid(row=0, column=1)
entry_password.grid(row=1, column=1)

tk.Button(app, text="Login", command=login).grid(row=3, column=0)
tk.Button(app, text="Register", command=register).grid(row=3, column=1)

create_db()
app.mainloop()
