import tkinter as tk
from tkinter import messagebox
import hashlib

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to save username and hashed password
def save_credentials(username, password):
    with open('credentials.txt', 'a') as file:
        file.write(f'{username}:{hash_password(password)}\n')

# Function to handle the submission of credentials
def submit_credentials():
    username = username_entry.get()
    password = password_entry.get()
    if username and password:
        save_credentials(username, password)
        messagebox.showinfo("Success", "Credentials saved successfully!")
    else:
        messagebox.showwarning("Input Error", "Please enter both username and password.")

# Create the main window
root = tk.Tk()
root.title("Login System")

# Create and place the username label and entry
username_label = tk.Label(root, text="Username:")
username_label.pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

# Create and place the password label and entry
password_label = tk.Label(root, text="Password:")
password_label.pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

# Create and place the submit button
submit_button = tk.Button(root, text="Submit", command=submit_credentials)
submit_button.pack(pady=20)

# Run the main event loop
root.mainloop()
