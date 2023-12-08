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

@app.route('/reservations', methods=['GET', 'POST'])
def reservations():
    header = "Reserve Your Seat"
    subheader = "Seating Chart"
    seat_legend = "X = Reserved Seat | O = Available Seat"
    seats_array = get_seats()
    num_rows = len(seats_array)
    num_seats = len(seats_array[0])

    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        selected_row = int(request.form['row'])
        selected_column = int(request.form['seat'])


        if seats_array[selected_row][selected_column] == 'O':
            code = reserve_seat(selected_row, selected_column, first_name, last_name)

            seats_array = get_seats()

            return render_template('successfulReservation.html',first_name=first_name, last_name=last_name, row=selected_row, seat=selected_column, ticket_number=code,header=header, subheader=subheader, seat_legend=seat_legend, seats_array=seats_array, num_rows=num_rows, num_seats=num_seats)
        
        flash('Seat is not available.', 'error')

    return render_template('reservations.html', header=header, subheader=subheader, seat_legend=seat_legend, seats_array=seats_array, num_rows=num_rows, num_seats=num_seats)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
