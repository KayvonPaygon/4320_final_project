from flask import Flask, render_template, request, flash
from methods import *
import secrets

app = Flask(__name__)

app.secret_key = secrets.token_hex(16)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        entered_username = request.form['username']
        entered_password = request.form['password']

        if check_credentials(entered_username, entered_password):
            seats_array = get_seats()
            cost_matrix = get_cost_matrix()
            total_sales = calculate_total_sales(seats_array, cost_matrix)

            header = "Administrator Login"
            subheader = "Printing Seating Chart"
            return render_template('loggedInAdmin.html', header=header, subheader=subheader, seats_array=seats_array, total_sales=total_sales)

        flash('Wrong username or password.', 'error')

    header = "Administrator Login"
    subheader = "Please Login"
    
    return render_template('admin.html', header=header, subheader=subheader)

@app.route('/reservations')
def reservations():
    return render_template('reservations.html')

if __name__ == '__main__':
    app.run(debug=True, port=5002)
