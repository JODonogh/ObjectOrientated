from sll import SLL
import sqlite3

sll = SLL()

class Patient:

    '''class for patient objects with methods to help in the processing of the patient'''
    ''' class to house all SQL lite functionality'''
    def __init__(self):
        # creating an sqlite connection
        self.conn = sqlite3.connect('patientdatabase.db')
        self.c = self.conn.cursor()
        # Query to create a database
        self.c.execute('''CREATE TABLE IF NOT EXISTS Patients 
                    (
                    patient_id INT PRIMARY KEY NOT NULL,
                    name TEXT NOT NULL,
                    age INT NOT NULL,
                    address CHAR(50),
                    tel_no INT NOT NULL,
                    pps_no TEXT NOT NULL,
                    summary CHAR(50));''')

    def patient_info(self):
        self.patient_id = int(input("Please enter the patients id number: "))
        self.patient_name = str(input("Please enter the persons name: "))
        try:
            self.patient_age = int(input("Please enter the patients age: "))
        except ValueError:
            print("Value must be a number")
            self.patient_age = int(input("Please enter the patients age: "))
        self.patient_address = str(input("Please enter the patients address: "))
        try:
            self.patient_tel = int(input("Please enter the patients telephone number: "))
        except ValueError:
            print("Value must be a number")
            self.patient_tel = int(input("Please enter the patients telephone number: "))
        self.patient_pps = input("Enter patients PPS: ")
        self.patient_summary = input("Please summarise patients condition:")

    def insert_patient(self):
        self.patient_info()
        query = f"INSERT INTO Patients(patient_id, name, age, address, tel_no, pps_no, summary) VALUES({self.patient_id}, '{self.patient_name}', {self.patient_age}, '{self.patient_address}', {self.patient_tel}, '{self.patient_pps}', '{self.patient_summary}');"
        data = self.patient_id, self.patient_name, self.patient_age, self.patient_address, self.patient_tel, self.patient_pps, self.patient_summary
        self.c.execute(query)
        self.conn.commit()
        return

    def view_query(self):
        view_query = self.c.execute("SELECT * FROM Patients;")
        cursor =self.c
        result = None
        for row in view_query:
            print(row)
        #self.c.execute(view_query)
        return self.c.fetchall()

    def some_query(self):
        view_query = "SELECT * FROM Patients;"
        self.c.execute(view_query)
        return self.c.fetchmany(5)

    def update_query(self):
        new_id = input("What is the patient id number you want to update? ")
        self.patient_info()
        query = f"UPDATE Patients SET patient_id= {self.patient_id}, name = '{self.patient_name}', age = {self.patient_age}, address= '{self.patient_address}', tel_no = {self.patient_tel}, pps_no = '{self.patient_pps}', summary = '{self.patient_summary}' WHERE patient_id = {new_id};"
        self.c.execute(query)
        print("Total number of rows updated:", self.conn.total_changes)
        self.conn.commit()

    def search(self, pos):
        search_query = f"SELECT patient_id = {pos} FROM Patients;"
        print(search_query)
        self.c.execute(search_query)

    def delete_query(self, pos):
        delete_query = f"DELETE FROM Patients WHERE patient_id = {pos};"
        self.c.execute(delete_query)
        self.conn.commit()

    def get_nurse(self):
        new_id = input("What is the patient id number you want to update?")
        patient_update = input("Please enter the patients vitals and update on their condition:")
        query = f"UPDATE Patients SET Summary = '{patient_update}' WHERE patient_id = {new_id};",
        print(query)
        self.c.execute(query)
        return patient_update

    def set_priority(self):
        #Temporary patient data
        patient_details = "Sam"
        try:
            priority = int(input("Please enter priority of patient, 1-10, 10 being highest priority, 1 being lowest: "))
        except ValueError:
            print("Value must be a number")
            priority = int(input("Please enter priority of patient, 1-10, 10 being highest priority, 1 being lowest: "))
        patient = SLL()
        if priority == 1:
            patient.insert_start(patient_details, 0)
        elif priority == 10:
            patient.insert_end(patient_details, None)
        else:
            patient.insert_particular(patient_details, 1)

    def get_treatment(self):
        new_id = input("What is the patient id number you want to update?")
        patient_update = input("Please enter the patients treatment:")
        query = f"UPDATE Patients SET Summary = '{patient_update}' WHERE patient_id = {new_id};",
        print(query)
        self.c.execute(query)
        return patient_update

