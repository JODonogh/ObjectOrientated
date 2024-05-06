from sll import SLL
import sqlite3
from node import Node

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

    def view_query(self):
        view_query = "SELECT * FROM Patients;"
        pointer = 0
        try:
            self.c.execute(view_query)
            for row in self.c.fetchall():
                print(row)
                node = Node(row, pointer + 1)
                node.set_data(row)
                node.get_data()
                node.set_next(pointer + 1)
                node.get_next()
                sll.append_node(row, pointer)
                print(node)
        except ValueError as err:
            print(f"The following error occurred: '{err}'")

patient = Patient()
patient.view_query()
sll.patient_view()
