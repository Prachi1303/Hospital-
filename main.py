import pymysql as p

try:
    con = None
    while not con:
        # Prompt user to enter login credentials
        print("\n*** *** *** *LOGIN TO DATABASE* *** *** *** \n")
        username = input("Enter username: ")
        password = input("Enter password: ")
        print("\n*** *** *** *** *** *** *** *** *** *** *** \n")

        # Connect to database using login credentials
        try:
            con = p.connect(host='localhost', port=3306, user=username, password=password, database='hospital', cursorclass=p.cursors.DictCursor)
        except:
            print("Invalid username or password. Please try again.")

    smt = con.cursor()
    
    # Create patient table if it doesn't exist
    smt.execute('''CREATE TABLE patient (
                    patient_id INT PRIMARY KEY,
                    first_name VARCHAR(50),
                    last_name VARCHAR(50),
                    address VARCHAR(100),
                    phone_number VARCHAR(20),
                    email VARCHAR(100)
                )''')

    print("\n*** *** *** *** *** *** *** *** WELCOME TO HOSPITAL DATABASE *** *** *** *** *** *** *** *** \n")
    
    while True:
        choice = input("Do you want to:\n 1. check old data\n 2. insert new data\n 3. update existing data\n 4. delete existing data\n \n(Enter 'check', 'insert', 'update', or 'delete'): ")
        if choice == 'check':
            print("\nWhich data do you want to check?")
            print("1. Patient data")
            print("2. Doctor data")
            print("3. Appointments of a patient")
            print("4. Prescriptions of a patient")

            check_choice = input("Enter your choice (1/2/3/4): ")

            if check_choice == '1':
                pid = int(input("\nEnter Patient id like 1,2...: "))
                q = 'SELECT * FROM patient WHERE patient_id={0}'.format(pid)
                smt.execute(q)
                rec = smt.fetchall()
                if rec:
                    for rows in rec:
                        print("Patient ID:", rows['patient_id'])
                        print("Name:", rows['first_name'], rows['last_name'])
                        print("Address:", rows['address'])
                        print("Phone Number:", rows['phone_number'])
                        print("Email:", rows['email'])
                        print(" ")
                else:
                    print("\nNo patient found with the given ID.")

            elif check_choice == '2':
                did = int(input("\nEnter Doctor id between 1000-1020: "))
                q = 'SELECT * FROM doctor WHERE doctor_id={0}'.format(did)
                smt.execute(q)
                rec = smt.fetchall()
                if rec:
                    for rows in rec:
                        print("Doctor ID:", rows['doctor_id'])
                        print("Name:", rows['first_name'], rows['last_name'])
                        print("Address:", rows['address'])
                        print("Phone Number:", rows['phone_number'])
                        print("Email:", rows['email'])
                        print("Speciality:", rows['specialty'])
                        print(" ")
                else:
                    print("\nNo doctor found with the given ID.")

            elif check_choice == '3':
                aid = int(input("\nEnter Appointment id like 101,102...: "))
                q = 'SELECT * FROM appointment WHERE appointment_id={0}'.format(aid)
                smt.execute(q)
                rec = smt.fetchall()
                if rec:
                    print("\nAppointments of the patient:")
                    for rows in rec:
                        print("Appointment ID:", rows['appointment_id'])
                        print("Patient ID:", rows['patient_id'])
                        print("Doctor ID:", rows['doctor_id'])
                        print("Date:", rows['appointment_date'])
                        print("Time:", rows['appointment_time'])
                        print("Diseases:", rows['notes'])
                        print(" ")
                        
                else:
                    print("\nNo appointments found for the given patient ID.")

            elif check_choice == '4':
                preid = int(input("\nEnter Prescription id like 10001,10002....: "))
                q =  'SELECT * FROM prescription WHERE prescription_id={0}'.format(preid)
                smt.execute(q)
                rec = smt.fetchall()
                if rec:
                    print("\nPrescriptions of the patient:")
                    for rows in rec:
                        print("Prescription ID:", rows['prescription_id'])
                        print("Patient ID:", rows['patient_id'])
                        print("Doctor ID:", rows['doctor_id'])
                        print("Medicine Name:", rows['medication'])
                        print("Dosage:", rows['dosage'])
                        print("Start Date:", rows['start_date'])
                        print("End Date:", rows['end_date'])
                        print("Lab Test:", rows['Lab_Test'])
                        print(" ")
                else:
                    print("\nNo prescriptions found for the given patient ID.")

            else:
                print("\nInvalid choice.")
                
        
        elif choice == 'insert':
            fname = input("\nEnter patient's first name: ")
            lname = input("Enter patient's last name: ")
            address = input("Enter patient's address: ")
            phone = input("Enter patient's phone number: ")
            email = input("Enter patient's email: ")
            print(" ")

            # Fetch the maximum patient id from the patient table
            smt.execute('SELECT MAX(patient_id) as max_id FROM patient')
            result = smt.fetchone()
            if result['max_id']:
                next_patient_id = result['max_id'] + 1
            else:
                next_patient_id = 1

            # Use the incremented patient id for the new patient record
            q = 'INSERT INTO patient (patient_id, first_name, last_name, address, phone_number, email) VALUES (%s, %s, %s, %s, %s, %s)'
            smt.execute(q, (next_patient_id, fname, lname, address, phone, email))
            con.commit()
            print("\nPatient information inserted successfully. Patient ID:", next_patient_id)
            print(" ")

        elif choice == 'update':
            pid = int(input("\nEnter Patient id: "))
            q = 'SELECT * FROM patient WHERE patient_id={0}'.format(pid)
            smt.execute(q)
            rec = smt.fetchall()
            if rec:
                fname = input("Enter patient's first name (press enter to leave unchanged): ")
                lname = input("Enter patient's last name (press enter to leave unchanged): ")
                address = input("Enter patient's address (press enter to leave unchanged): ")
                phone = input("Enter patient's phone number (press enter to leave unchanged): ") 
                email = input("Enter Patients's email (press enter to leave unchanged: )")
                print(" ")
                
                
                update_values = {}
                if fname:
                    update_values['first_name'] = fname
                if lname:
                    update_values['last_name'] = lname
                if address:
                    update_values['address'] = address
                if phone:
                    update_values['phone_number'] = phone
                if email:
                    update_values['email'] = email

                if update_values:
                    set_query = ', '.join([f"{key}='{value}'" for key, value in update_values.items()])
                    q = f"UPDATE patient SET {set_query} WHERE patient_id={pid}"
                    smt.execute(q)
                    con.commit()
                    print("\nPatient information updated successfully.")
                else:
                    print("\nNo values were updated.")
            else:
                print("\nNo patient found with the given ID.")

        elif choice == 'delete':
            pid = int(input("\nEnter Patient id: "))
            q = 'SELECT * FROM patient WHERE patient_id={0}'.format(pid)
            smt.execute(q)
            rec = smt.fetchall()
            if rec:
                q = f"DELETE FROM patient WHERE patient_id={pid}"
                smt.execute(q)
                con.commit()
                print("\nPatient information deleted successfully.\n")
            else:
                print("\nNo patient found with the given ID.\n")

        
        elif choice == 'exit':
            break
        
        else:
            print("\nInvalid choice. Please enter 'check', 'insert', 'update', 'delete', or 'exit'.")
            
except p.Error as e:
    print("Error occurred while connecting to MySQL database: ", e)

finally:
    if con:
        con.close()
print("Database connection closed.")


        