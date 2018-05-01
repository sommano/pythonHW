import sys, os
import dill as pickle

class Employee(object):
    def __init__(self, passed_name, passed_number, passed_comment):
        self.name = passed_name
        self.number = passed_number
        self.comment = passed_comment

    def find(self, search_term):
        if self.name.lower().find(search_term.lower()) != -1:
            return 1
        elif self.number.lower().find(search_term.lower()) != -1:
            return 1
        elif self.comment.lower().find(search_term.lower()) != -1:
            return 1
        else:
            return 0

    def show(self):
        print("Name:", self.name)
        print("Number:", self.number)
        print("Comment:", self.comment)

def load_data(filename):
    try:
        global employees
        file_data = open(filename, "rb")
        employees = pickle.load(file_data)
        input("\nData loaded - hit enter to continue...")
        file_data.close()

    except OSError as err:
        print("File could not be opened:")
        print(err)
        sys.exit(1)

def save_data(filename):
    try:
        global employees
        file_data = open(filename, "wb")
        pickle.dump(employees, file_data)
        file_data.close()
        input("\nData saved - hit enter to continue...")

    except OSError as err:
        print("File couldn't be saved:")
        print(err)
        input("\nHit enter to continue...")





employees = []
choice = 0

if len(sys.argv) == 1:
    print("No filename specifced - starting with empty data")
    input("Hit enter to continue...")
else:
    load_data(sys.argv[1])

while choice != 6:
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

    print("===== Employee Directory Manager 2.0 =====\n")
    print(" 1. List employees")
    print(" 2. Add employee")
    print(" 3. Delete employee")
    print(" 4. Search employees")
    print(" 5. Save data")
    print(" 6. Quit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        for x in range(0, len(employees)):
            print("\nEmployee number:", x + 1)
            employees[x].show()
        input("\nHit enter to continue...")

    elif choice == 2:
        name = input("\nEnter employee name:")
        number = input("Enter employee number:")
        comment = input("Enter employee comment:")
        employees.append(Employee(name, number, comment))
        input("\nEmployee added - hit enter to continue...")

    elif choice == 3:
        number = int(input("\nEnter employee number to remove:"))
        if number > len(employees):
            input("No such employee! Hit enter to continue...")
        else:
            del employees[number - 1]
            input("\nEmployee removed - hit enter to continue...")

    elif choice == 4:
        search_term = input("\nEnter a name, number or comment:")
        for x in range(0, len(employees)):
            result = employees[x].find(search_term)
            if result == 1:
                print("\nEmployee number:", x + 1)
                employees[x].show()
        input("\nHit enter to continue...")

    elif choice == 5:
        filename = input("\nEnter a filename:")
        save_data(filename)
