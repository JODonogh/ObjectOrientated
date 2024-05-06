# importing external patient files
from patient_original import Patient
from sll import SLL

# A GUI menu to faciliate doctors, nurses and receptionists

# creating global objects
patient = Patient()
sll = SLL()

def asterix():
    print("x" *75)

def menu_receptionist():
    print("\n1. Insert a patient: "
          "\n2. Update a patient: "
          "\n3. View all patients: "
          "\n4. exit program")
    asterix()
    try:
        choice = int(input("Please enter your choice:"))
    except ValueError:
        print("Value must be a number")
        menu_receptionist()
    asterix()
    while choice != 4:
        if choice == 1:
            patient.insert_patient()
        elif choice == 2:
            patient.update_query()
        elif choice == 3:
            patient.view_query()
            sll.patient_view()
        else:
            print("Im afraid you have entered an incorrect detail, please try again")
            main()
    counter = 1
    while counter <= sll.size():
        n = sll.get_node(counter)
        print(n.get_data().firstname)
        counter = counter + 1
    asterix()

def menu_nurse():
    print("\n1. Find particular patient "
          "\n2. Patients condition: "
          "\n3. Patients vitals: "
          "\n4. set priority:"
          "\n5. View all patients ")
    asterix()
    try:
        choice = int(input("Please enter your choice:"))
    except ValueError:
        print("Value must be a number")
        menu_nurse()
    asterix()
    if choice == 1:
        x = int(input("Please enter the number to be searched: "))
        sll.search(x)
    elif choice == 2:
        patient.get_condition()
    elif choice == 3:
        patient.get_vitals()
    elif choice == 4:
        priorty = patient.set_priority()
        return priorty
    elif choice == 5:
        patient.view_query()
    else:
        print("Im afraid you have entered an incorrect detail, please try again")
        main()
    asterix()

def menu_doctor():
    print("\n1. Patients treatment: "
          "\n2. See patient list: "
          "\n3. See last few patients"
          "\n4. Remove patient form list: "
          "\n5. check how many in the treatment list: ")
    asterix()
    try:
        choice = int(input("Please enter your choice:"))
    except ValueError:
        print("Value must be a number")
        menu_doctor()
    asterix()
    if choice == 1:
        patient.get_treatment()
    elif choice == 2:
        patient.view_query()
    elif choice == 3:
        patient.some_query()
    elif choice == 3:
        pos = input("Please enter the position on the list the patient is")
        sll.remove(pos)
        choice = input("Remove patient from the database entirely? y for yes")
        if choice == "y":
            patient.delete_query(pos)
        else:
            return
    elif choice == 4:
        print(sll.size())
    else:
        print("Im afraid you have entered an incorrect detail, please try again")
        main()
    asterix()

def main():
    # GUI menu to process patients
    asterix()
    menu_receptionist()
    asterix()
    menu_nurse()
    asterix()
    menu_doctor()
    asterix()
main()