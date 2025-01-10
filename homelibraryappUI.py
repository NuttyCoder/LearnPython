import isbnlib
import tkinter as tk
from tkinter import messagebox

def fetch_book_details(isbn):
    try:
        book = isbnlib.meta(isbn)
        if book:
            return {
                'Title': book['Title'],
                'Authors': ", ".join(book['Authors']),
                'Publisher': book['Publisher'],
                'Year': book['Year']
            }
        else:
            return None
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        return None

def on_scan():
    isbn = isbn_entry.get()
    genre = genre_entry.get()
    details = fetch_book_details(isbn)
    if details:
        result_text = f"Title: {details['Title']}\nAuthors: {details['Authors']}\nPublisher: {details['Publisher']}\nYear: {details['Year']}\nGenre: {genre}"
        result_label.config(text=result_text)
    else:
        result_label.config(text="No details found for this ISBN.")

# UI setup
app = tk.Tk()
app.title("Home Library App")

tk.Label(app, text="Enter ISBN:").grid(row=0, column=0, padx=10, pady=10)
isbn_entry = tk.Entry(app)
isbn_entry.grid(row=0, column=1)

tk.Label(app, text="Enter Genre:").grid(row=1, column=0, padx=10, pady=10)
genre_entry = tk.Entry(app)
genre_entry.grid(row=1, column=1)

scan_button = tk.Button(app, text="Scan & Fetch", command=on_scan)
scan_button.grid(row=2, columnspan=2, pady=10)

result_label = tk.Label(app, text="", wraplength=300)
result_label.grid(row=3, columnspan=2, pady=10)

app.mainloop()
