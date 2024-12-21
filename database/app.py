from flask import Flask, request, jsonify, render_template
import datetime
import database

app = Flask(__name__)
database.init_db()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_website', methods=['POST'])
def add_website():
    website_address = request.form['website_address']
    device = request.form['device']
    date_of_visit = datetime.datetime.now().strftime('%Y-%m-%d')
    time_of_visit = datetime.datetime.now().strftime('%H:%M:%S')
    database.add_website(website_address, device, date_of_visit, time_of_visit)
    return jsonify({"message": "Website added successfully!"})

@app.route('/get_websites', methods=['GET'])
def get_websites():
    websites = database.get_websites()
    return jsonify(websites)

if __name__ == '__main__':
    app.run(debug=True)
