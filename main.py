
# Student Management System

students = {}


def add_student():
    roll_no = input("Enter roll number: ")

    if roll_no in students:
        print("Student already exists!")
        return

    name = input("Enter student name: ")
    marks = input("Enter student marks: ")

    students[roll_no] = {
        "name": name,
        "marks": marks
    }

    print("Student added successfully!")


def display_students():
    if not students:
        print("No students found.")
        return

    print("\n--- Student Records ---")

    for roll_no, details in students.items():
        print("Roll Number:", roll_no)
        print("Name:", details["name"])
        print("Marks:", details["marks"])
        print("-----------------------")


def search_student():
    roll_no = input("Enter roll number to search: ")

    if roll_no in students:
        print("Name:", students[roll_no]["name"])
        print("Marks:", students[roll_no]["marks"])
    else:
        print("Student not found!")


def delete_student():
    roll_no = input("Enter roll number to delete: ")

    if roll_no in students:
        del students[roll_no]
        print("Student deleted successfully!")
    else:
        print("Student not found!")


while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Thank you for using the system!")
        break
    else:
        print("Invalid choice. Try again.")
