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

def check_credentials(username, password):
    with open('data/passcodes.txt', 'r') as file:
        for line in file:
            stored_username, stored_password = line.strip().split(',')
            if username == stored_username and password == stored_password:
                return True
    return False

def generate_code(first_name):
    class_name = "INFOTC4320"
    result = ""
    len_name, len_class = len(first_name), len(class_name)
    max_length = max(len_name, len_class)

    for i in range(max_length):
        if i < len_name:
            result += first_name[i]
        if i < len_class:
            result += class_name[i]

    return result

def reserve_seat(row, column, first_name, last_name):
    code = generate_code(first_name)

    data_array = [first_name, row, column, code]

    write_to_file(data_array, 'data/reservations.txt')

    return code



def write_to_file(data_array, file_path):
    line = ', '.join(map(str, data_array))
    
    # Write the line to the file
    with open(file_path, 'a') as file:
        file.write('\n' + line)