import sqlite3

def init_db():
    conn = sqlite3.connect('home_network.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS website_info (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            website_address TEXT NOT NULL,
            device TEXT NOT NULL,
            date_of_visit DATE NOT NULL,
            time_of_visit TIME NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_website(website_address, device, date_of_visit, time_of_visit):
    conn = sqlite3.connect('home_network.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO website_info (website_address, device, date_of_visit, time_of_visit)
        VALUES (?, ?, ?, ?)
    ''', (website_address, device, date_of_visit, time_of_visit))
    conn.commit()
    conn.close()

def get_websites():
    conn = sqlite3.connect('home_network.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM website_info')
    websites = cursor.fetchall()
    conn.close()
    return websites
