def calculate_total_sales():

    return 100.00

def generate_code(first_name):
    class_name = "INFOTC4320"

    # all it does is put the letters of the first_name between the letters of class_name
    # just make an algorithm that does that and doesnt throw an out_of_bounds error

    return "KIeNvFiOnTC4320"

def get_cost_matrix():
    cost_matrix = [[100, 75, 50, 100] for row in range(12)]
    return cost_matrix

def calculate_total_sales(seats_array, cost_matrix):
    total_sales = 0
    for i in range(len(seats_array)):
        for j in range(len(seats_array[i])):
            if seats_array[i][j] == 'X':
                total_sales += cost_matrix[i][j]
    return total_sales

def get_seats():
    #Initialize the seats as a 2D array with 4 columns and 12 rows
    seats = [['O' for _ in range(4)] for _ in range(12)]

    #Read reservations from reservations.txt and update the seats array
    with open('data/reservations.txt', 'r') as file:
        for line in file:
            name, row, column, code = line.strip().split(', ')
            row, column = int(row), int(column)

            #Mark the seat as bought in the seats array
            seats[row][column] = 'X'

    return seats

#Example usage:
#seats_array = get_seats()

#Display the seats array
#for row in seats_array:
    #print(row)

def write_to_file(data_array, file_path):

    return False