Rent-A-Car Management System

This is a Python-based project designed to manage a car rental service. It allows users to interact with the system to view available cars, rent cars, return cars, and calculate total earnings.
The project is simple and easy to use, with clear menus and functionality.

Features:
	1.	List Available Cars: Displays all cars currently available for rent.
	2.	Rent a Car: Allows users to select and rent a car.
	3.	Return a Car: Processes the return of a rented car.
	4.	Count the Money: Calculates the total earnings from rented cars.
	5.	Exit: Gracefully exits the system.

Files Used in the Project:
	•	vehicles.txt: Stores details of all cars available in the system, including registration number, model, price, and properties.
	•	rentedVehicles.txt: Tracks cars currently rented out.
  •	customers.txt: Logs all existing and new customers.
  •	transActions.txt: Manages all payments made.

Requirements:
	•	Python 3.6 or later.
	•	Basic familiarity with terminal or command-line interfaces.

How to Run the Project:
	1.	Clone the repository:
 git clone https://github.com/Veselin05/Rent-a-car-project.git
cd rent-a-car
	2.	Ensure the necessary files (vehicles.txt and rentedVehicles.txt) are in the same directory as the script.
	3.	Run the Python script:
 python Rent-a-car project.py
 	4.	Follow the on-screen menu to interact with the system.

Example Workflow:
	1.	Launch the script.
	2.	Choose an option from the menu:
	•	Option 1: View a list of all available cars.
	•	Option 2: Rent a car by entering its details.
	•	Option 3: Return a rented car.
	•	Option 4: Check total earnings.
	•	Option 0: Exit the system.

Project Structure:
The main script is divided into the following functions:
	•	display_menu(): Displays the menu options.
	•	list_available_cars(): Lists cars currently available for rent.
	•	rent_a_car(): Allows renting a car and updates relevant files.
	•	return_a_car(): Handles the return process and updates files.
	•	count_money(): Calculates and displays total rental income.

Contributing:
Contributions are welcome! If you’d like to contribute, please fork the repository and submit a pull request.

License:
This project is open-source and available under the MIT License.
