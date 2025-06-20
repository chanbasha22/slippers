from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

# ✅ Function to connect to SQLite database
def get_db_connection():
    conn = sqlite3.connect('database/hello.db')  # Use your own .db file
    conn.row_factory = sqlite3.Row
    return conn

# ✅ Home Page
@app.route('/')
def index():
    return render_template("index.html")

# ✅ Static Pages
@app.route('/about.html')
def about():
    return render_template("about.html")

@app.route('/contact.html')
def contact():
    return render_template("contact.html")

@app.route('/shopping.html')
def shopping():
    return render_template("shopping.html")

@app.route('/casual.html')
def casual():
    return render_template("casual.html")

@app.route('/indoor.html')
def indoor():
    return render_template("indoor.html")

@app.route('/summer.html')
def summer():
    return render_template("summer.html")

@app.route('/winter.html')
def winter():
    return render_template("winter.html")

# ✅ Booking Page
@app.route('/booking.html')
def booking():
    return render_template("booking.html")

# ✅ Booking form submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    product = request.form['product']
    size = request.form['size']
    address = request.form['address']

    conn = get_db_connection()
    conn.execute("INSERT INTO bookings (name, product, size, address) VALUES (?, ?, ?, ?)",
                 (name, product, size, address))
    conn.commit()
    conn.close()

    return render_template("booking.html", message="Booking successful!")

if __name__ == '__main__':
    os.makedirs("database", exist_ok=True)
    app.run(debug=True)
