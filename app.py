from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# ✅ MySQL connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Use your MySQL password here
    database="hello"
)
cursor = mydb.cursor()

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

    sql = "INSERT INTO bookings (name, product, size, address) VALUES (%s, %s, %s, %s)"
    values = (name, product, size, address)
    cursor.execute(sql, values)
    mydb.commit()

    return redirect('/booking.html')  # Redirect back to booking page or confirmation page

if __name__ == '__main__':
    app.run(debug=True)
