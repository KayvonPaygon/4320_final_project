from flask import Flask, render_template, request

app = Flask(__name__)

# Placeholder for ReservationSystem class change how you need it
class ReservationSystem:
    def __init__(self):
        self.cost_matrix = self.get_cost_matrix()
        self.seat_chart = [['o' for _ in range(4)] for _ in range(12)]
        self.reservations = []

    def get_cost_matrix(self):
        cost_matrix = [[100, 75, 50, 100] for row in range(12)]  # Placeholder cost matrix
        return cost_matrix

    def calculate_total_sales(self):
        total_sales = sum(sum(self.cost_matrix[row][col] for col in range(4)) for row in range(12))
        return total_sales

    def get_seats(self):
        return self.seat_chart

    def reserve_seat(self, row, column, first_name, last_name):
        try:
            row_index = int(row) - 1
            col_index = int(column) - 1
            if self.seat_chart[row_index][col_index] == 'o':
                self.seat_chart[row_index][col_index] = 'x'
                ticket_code = self.generate_code(first_name)
                self.reservations.append((first_name, last_name, row, column, ticket_code))
                return True, ticket_code
            else:
                return False, "Seat already reserved!"
        except (ValueError, IndexError):
            return False, "Invalid row or column number."

    def generate_code(self, first_name):
        return f"{first_name[:3].upper()}-{len(first_name)}{len(first_name) + 5}"


reservation_system = ReservationSystem()  # Initialize the reservation system


@app.route('/')
def main_menu():
    return render_template('main_menu.html')


@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Check if username and password match admin credentials
        # Perform validation here (for demonstration, keeping it simple)
        if username == 'admin' and password == 'password':
            total_sales = reservation_system.calculate_total_sales()
            seats = reservation_system.get_seats()
            return render_template('admin_portal.html', total_sales=total_sales, seats=seats)
        else:
            return "Invalid credentials. Please try again."
    return render_template('admin_login.html')


@app.route('/reserve_seat', methods=['GET', 'POST'])
def reserve_seat():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        seat_row = request.form['seat_row']
        seat_column = request.form['seat_column']
        success, ticket_code = reservation_system.reserve_seat(seat_row, seat_column, first_name, last_name)
        if success:
            return f"Seat reserved successfully! Your e-ticket number is: {ticket_code}"
        else:
            return f"Failed to reserve seat. Reason: {ticket_code}"
    return render_template('reserve_seat.html')


if __name__ == '__main__':
    app.run(debug=True)
