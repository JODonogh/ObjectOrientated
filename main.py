# importing external patient files
from patient import Patient
from sll import SLL

# A GUI menu to faciliate doctors, nurses and receptionists


# function to use to create visual separation in program
def asterix():
    print("x" *75)

#************************COMBINE Menus into one so you can use objects more effectively***************************

def menu_parent():
    asterix()
    print("Options for selection")
    print("1. Receptionist menu: "
          "\n2. Nurses menu: "
          "\n3. Doctors menu: "
          "\n4. Exit program")
    asterix()
    try: # exception handling in case the user inputs a wrong value
        choice = int(input("Please enter your choice: "))
    except ValueError:
        print("Value must be a number")
        menu_receptionist()
    asterix()
    if choice == 1:
        menu_receptionist()
    elif choice == 2:
        menu_nurse()
    elif choice == 3:
        menu_doctor()
    elif choice == 4:
        return
    else:
        print("Im afraid you have entered an incorrect detail, please try again")
        menu_parent()
    asterix()

# menu that will be displayed for the receptionist and the options they will need
def menu_receptionist():
    asterix()
    print("Options for selection")
    print("1. Insert a patient: "
          "\n2. Update a patient: "
          "\n3. View all patients: "
          "\n4. Return to main menu")
    asterix()

    # ******* this is repeated a few times, maybe this functionality needs to be elsewhere? *************

    try: # exception handling in case the user inputs a wrong value
        choice = int(input("Please enter your choice: "))
    except ValueError:
        print("Value must be a number")
        menu_receptionist()
    asterix()
    while choice != 4: # a indefinite loop to take user inputs and run various object methods
        patient = Patient()
        if choice == 1:
            sll = SLL()
            patient.insert_patient()
            sll.append_node(patient) # ******* is this an empty node? maybe this functionality needs to be elsewhere? *************
        elif choice == 2:
            patient.update_query()
        elif choice == 3:
            patient.view_query()
        else:
            print("Im afraid you have entered an incorrect detail, please try again")
            main()
        menu_receptionist()
    menu_parent()
    asterix()
    return patient

# menu that shows the options for the nurse
def menu_nurse():
    patient = Patient()
    sll = SLL()
    password = "nurse"
    login = input("Please input the password to get access to the nurse menu:")
    asterix()
    if login == password:
        asterix()
        print("Options for selection")
        print("1. Find particular patient "
              "\n2. Update Patients condition & vitals: "
              "\n3. set priority:"
              "\n4. View all patients "
              "\n5. Return to main menu")
        asterix()
        try:# exception handling in case the user inputs a wrong value
            choice = int(input("Please enter your choice: "))
        except ValueError:
            print("Value must be a number")
            menu_nurse()
        asterix()

        #******************Check if this is working properly, remember this was looping indefinitely in other places *********************************

        while choice != 5:# a indefinite loop to take user inputs and run various object methods
            if choice == 1:
                to_find = int(input("Please enter the number to be searched: "))
                patient.search(to_find)
                sll.get_node(to_find)
            elif choice == 2:
                patient.get_nurse()
            elif choice == 3:
                priorty = patient.set_priority()
                return priorty
            elif choice == 4:
                patient.view_query()
            else:
                print("Im afraid you have entered an incorrect detail, please try again")
                menu_nurse()
        menu_parent()
        asterix()

# menu that shows the options for the doctor to use
def menu_doctor():
    patient = Patient()
    sll = SLL()
    password = "doctor"
    login = input("Please input the password to get access to the doctor menu:")
    asterix()
    if login == password:
        print("Options for selection")
        print("1. Patients treatment: "
              "\n2. See patient all list: "
              "\n3. See patients by priority: "
              "\n4. Remove patient form list: "
              "\n5. Check how many in the treatment list: "
              "\n6. Return to main menu")
        asterix()
        try:# exception handling in case the user inputs a wrong value
            choice = int(input("Please enter your choice: "))
        except ValueError:
            print("Value must be a number")
            menu_doctor()
        asterix()
        if choice == 1:# a indefinite loop to take user inputs and run various object methods
            patient.get_treatment()
        elif choice == 2:
            patient.view_query()
        elif choice == 3:
            patient.some_query()
        elif choice == 4:
            pos = input("Please enter the position on the list where the patient you wish delete is: ")
            sll.remove(pos)
            choice = input("Remove patient from the database entirely? y for yes: ")
            if choice == "y":
                patient.delete_query(pos)
            else:
                return
        elif choice == 5:
            print(sll.size())
        elif choice == 6:
            menu_parent()
        else:
            print("Im afraid you have entered an incorrect detail, please try again")
            menu_doctor()
        asterix()

# main program for all the various functions to run that will handle the user interaction functionality
def main():
    # UI menu to process patients
    menu_parent()
main()