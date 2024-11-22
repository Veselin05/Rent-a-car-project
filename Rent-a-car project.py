import datetime

def display_menu():
    print("\nYou may select one of the following:")
    print("1) List available cars")
    print("2) Rent a car")
    print("3) Return a car")
    print("4) Count the money")
    print("0) Exit")
    selection = input("What is your selection? ")
    return selection

def list_available_cars():
    try:
        rented_cars = []
        rented_file = open('rentedVehicles.txt', 'r')
        for line in rented_file:
            rented_cars.append(line.split(',')[0])
        rented_file.close()

        print("\nThe following cars are available:")
        file = open('vehicles.txt', 'r')
        for line in file:
            car_details = line.strip().split(',')
            reg_nr = car_details[0]
            model = car_details[1]
            price = car_details[2]
            properties = car_details[3:]
            properties_str = ""
            for prop in properties:
                if properties_str:
                    properties_str += ", "
                properties_str += prop
            if reg_nr not in rented_cars:
                print("* Reg. nr:", reg_nr + ",", "Model:", model + ",", "Price per day:", price)
                print("  Properties:", properties_str)
        file.close()

    except FileNotFoundError:
        print("Error: The file containing vehicle data could not be found.")

def is_valid_name(name):
    return name.isalpha() and name[0].isupper()

def is_valid_email(email):
    if "@" not in email or email.count("@") != 1:
        return False
    local, domain = email.split("@")
    if not domain or "." not in domain:
        return False
    allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-")
    return all(char in allowed_chars for char in local + domain)

def rent_a_car():
    plate_number = input("Enter the plate number of the car: ").strip()

    try:
        available_cars = []
        available_file = open('vehicles.txt', 'r')
        for line in available_file:
            available_cars.append(line.split(',')[0])
        available_file.close()

        rented_cars = []
        rented_file = open('rentedVehicles.txt', 'r')
        for line in rented_file:
            rented_cars.append(line.split(',')[0])
        rented_file.close()

        if plate_number in rented_cars:
            print(plate_number, "already rented.")
            return
        elif plate_number not in available_cars:
            print("Car does not exist.")
            return

        while True:
            birth_date = input("Please enter your birthday in the form DD/MM/YYYY: ").strip()
            try:
                birth_date_obj = datetime.datetime.strptime(birth_date, "%d/%m/%Y")
                break
            except ValueError:
                print("There is no such date. Please try again.")

        customers_file = open('customers.txt', 'r')
        is_returning_customer = False
        first_name = ""
        for line in customers_file:
            existing_birth_date, first_name, last_name, email = line.strip().split(',')
            if birth_date == existing_birth_date:
                is_returning_customer = True
                break
        customers_file.close()

        if is_returning_customer:
            print("Hello", first_name)
        else:
            age = (datetime.datetime.now() - birth_date_obj).days // 365
            if age < 18:
                print("You are too young to rent a car, sorry.")
                return
            elif age > 75:
                print("You are too old to rent a car, sorry.")
                return
            print("Age OK.")

            while True:
                first_name = input("Enter the first name of the customer: ").strip()
                if is_valid_name(first_name):
                    break
                print("Names contain only letters and start with capital letters.")

            while True:
                last_name = input("Enter the last name of the customer: ").strip()
                if is_valid_name(last_name):
                    break
                print("Names contain only letters and start with capital letters.")

            while True:
                email = input("Give your email address: ").strip()
                if is_valid_email(email):
                    break
                print("Give a valid email address.")

            customers_file = open('customers.txt', 'a')
            customers_file.write(birth_date + ',' + first_name + ',' + last_name + ',' + email + '\n')
            customers_file.close()

        rental_date = datetime.datetime.now()
        rental_date_str = rental_date.strftime("%d/%m/%Y %H:%M")

        rented_file = open('rentedVehicles.txt', 'a')
        rented_file.write(plate_number + ',' + birth_date + ',' + rental_date_str + '\n')
        rented_file.close()

        if not is_returning_customer:
            print("Hello", first_name)
        print("You rented a car", plate_number)

    except FileNotFoundError:
        print("Error: One or more required files could not be found.")

def return_a_car():
    plate_number = input("Give the register number of the car you want to return: ").strip()
    try:
        available_cars = {}
        file = open('vehicles.txt', 'r')
        for line in file:
            car_details = line.strip().split(',')
            available_cars[car_details[0]] = line.strip()
        file.close()

        rented_cars = []
        rented_file = open('rentedVehicles.txt', 'r')
        for line in rented_file:
            rented_cars.append(line.strip().split(','))
        rented_file.close()

        if plate_number not in available_cars:
            print("Car does not exist.")
            return

        rented_car_info = None
        for car in rented_cars:
            if car[0] == plate_number:
                rented_car_info = car
                break

        if rented_car_info is None:
            print("The car is not rented.")
            return

        birth_date = rented_car_info[1]
        rent_start_datetime = rented_car_info[2]
        rent_start = datetime.datetime.strptime(rent_start_datetime, "%d/%m/%Y %H:%M")
        rent_end = datetime.datetime.now()

        rental_duration = (rent_end - rent_start).days
        if rental_duration == 0:
            rental_duration = 1

        price_per_day = float(available_cars[plate_number].split(',')[2])
        total_cost = rental_duration * price_per_day

        print("The rent lasted", rental_duration, "days and the cost is", f"{total_cost:.2f}", "euros.")

        rented_file = open('rentedVehicles.txt', 'w')
        for car in rented_cars:
            if car[0] != plate_number:
                rented_file.write(car[0] + ',' + car[1] + ',' + car[2] + '\n')
        rented_file.close()

        transactions_file = open('transActions.txt', 'a')
        transactions_file.write(plate_number + ',' + birth_date + ',' + rent_start.strftime('%d/%m/%Y %H:%M') + ',' +
                                rent_end.strftime('%d/%m/%Y %H:%M') + ',' + str(rental_duration) + ',' +
                                f"{total_cost:.2f}" + '\n')
        transactions_file.close()

    except FileNotFoundError:
        print("Error: One or more required files could not be found.")

def count_the_money():
    total_money = 0.0
    try:
        transactions_file = open('transActions.txt', 'r')
        for line in transactions_file:
            total_cost = float(line.strip().split(',')[-1])
            total_money += total_cost
        transactions_file.close()

        print("The total amount of money is", f"{total_money:.2f}", "euros.")
    except FileNotFoundError:
        print("Error: The transactions file could not be found.")

while True:
    user_selection = display_menu()
    
    if user_selection == '1':
        list_available_cars()
    elif user_selection == '2':
        rent_a_car()
    elif user_selection == '3':
        return_a_car()
    elif user_selection == '4':
        count_the_money()
    elif user_selection == '0':
        print("Exiting the program.")
        break
    else:
        print("You selected:", user_selection)