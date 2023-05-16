# Hospital-
This Python script provides a command-line interface for interacting with a MySQL Hospital database 
It stores the information about patients, doctors, appointments, and prescriptions in a hospital system.

#Prerequisites

Before running the script, make sure you have the following prerequisites:
Python installed on your system.

pymysql library installed. You can install it using the command pip install pymysql.

MySQL server installed and running locally on your system.

#Database Setup

Create a MySQL database named "hospital" on your MySQL server.

Copy the SQL code (sql code.txt) from the text file then execute it on your Mysql server to create the tables of patient, doctor, appointment, prescription.

#Running the Script

Save the provided code in a Python file (e.g., hospital_db.py).

Open a terminal or command prompt and navigate to the directory where the script is saved.

Run the script using the command python hospital_db.py.

Follow the prompts to enter your MySQL database login credentials (username and password).

Once logged in, you can choose from the following options:

Check old data: Retrieve and display existing data from the database.

Insert new data: Add a new patient to the database.

Update existing data: Update information for an existing patient.

Delete existing data: Delete a patient from the database.

Exit: Close the script and end the database connection.

#Note

The code assumes that the MySQL server is running on localhost with the default port 3306. If your setup differs, you can modify the connection parameters in the code accordingly.

The code handles incorrect login credentials by prompting the user to enter the correct ones.

The code performs basic input validation but does not handle all possible edge cases. It assumes valid input from the user.

It's recommended to have a backup of your database before using this script in a production environment.

This script is for educational purposes and may require modifications to suit your specific requirements.
