import tkinter as tk
from tkinter import messagebox
import sqlite3
import hashlib

# hash functions are used for:
# Data Integrity: Verifying that the data has not been altered
# Password hashing: Securely storing passwords by hashing them before saving.
# Digital signatures and certificates: Ensuring authenticity and integrity.



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

def retrieve_users():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users')
    users = c.fetchall()
    conn.close()
    return users

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

def decrypt_and_display():
    decryption_password = entry_decrypt_password.get()
    if decryption_password == "your_encryption_password":  # Replace with actual decryption password logic
        users = retrieve_users()
        user_data = "\n".join([f"Username: {user[0]}, Password: {user[1]}" for user in users])
        text_display.delete('1.0', tk.END)
        text_display.insert(tk.END, user_data)
    else:
        messagebox.showerror("Error", "Incorrect decryption password")

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

tk.Label(app, text="Decryption Password").grid(row=4)
entry_decrypt_password = tk.Entry(app, show="*")
entry_decrypt_password.grid(row=4, column=1)

tk.Button(app, text="Decrypt and Display", command=decrypt_and_display).grid(row=5, column=1)

text_display = tk.Text(app, height=10, width=50)
text_display.grid(row=6, column=0, columnspan=2)

create_db()
app.mainloop()
