from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE = 'internet_history.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

@app.route('/')
def index():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM BrowsingHistory")
    history = cursor.fetchall()
    conn.close()
    return render_template('index.html', history=history)

@app.route('/add_entry', methods=['POST'])
def add_entry():
    website_address = request.form['website_address']
    device = request.form['device']
    time_of_day = request.form['time_of_day']
    date_of_visit = request.form['date_of_visit']

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO BrowsingHistory (website_address, device, time_of_day, date_of_visit) VALUES (?, ?, ?, ?)",
                   (website_address, device, time_of_day, date_of_visit))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete_entry/<int:id>')
def delete_entry(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM BrowsingHistory WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
