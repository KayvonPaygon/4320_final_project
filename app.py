from flask import Flask, render_template
from methods import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/admin')
def admin():
    seats_array = get_seats()
    cost_matrix = get_cost_matrix()
    total_sales = calculate_total_sales(seats_array, cost_matrix)

    header = "Administrator Login"
    subheader = "Printing Seating Chart"
    return render_template('admin.html', header=header, subheader=subheader, seats_array=seats_array, total_sales=total_sales)

@app.route('/reservations')
def reservations():
    return render_template('reservations.html')

if __name__ == '__main__':
    app.run(debug=True, port=5002)
