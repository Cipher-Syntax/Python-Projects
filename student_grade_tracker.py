import sys
import os

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

student_grades = {}

def add_students():
    print("=======================================================")
    print(f"{'Add Students':^50}")
    print("=======================================================")
    student_name = input("Enter student name: ")
    try:
        student_grade = float(input("Enter grade: "))
    except ValueError:
        print("\nInavalid Input....enter a valid grade")
    
    student_grades[student_name] = student_grade
    print(f"\nStudent {student_name} added successfully")

def access_student_grades():
    print("=======================================================")
    print(f"{'Access Students':^50}")
    print("=======================================================")
    access_student = input("Enter the name of the student to access grade: ")
    
    if len(student_grades) == 0:
        print("\nNo student to access...add a student first...")
        add_students()
    if access_student in student_grades:
        print(f"\n{access_student} : {student_grades[access_student]}")
def update_student_grades():
    print("=======================================================")
    print(f"{'Update Students':^50}")
    print("=======================================================")
    update_student = input("Enter student name to update: ")

    if len(student_grades) == 0:
        print("No students to update...")
    
    if update_student in student_grades:
        try:
            new_grade = int(input("Enter new grade: "))
        except ValueError:
            print("\nInvalid Input...Enter a valid grade")
        student_grades[update_student] = new_grade
        print(f"\nStudent {update_student} updated successfully")

def view_students():
    print("=======================================================")
    print(f"{'Display Students':^50}")
    print("=======================================================")

    for student_name, student_grade in student_grades.items():
            print(f"{student_name} : {student_grade}")

while True:
    print("=======================================================")
    print(f"{'Student Management System':^50}")
    print("=======================================================")
    print("1. Add Student")
    print("2. Access Student Grade")
    print("3. Update Student Grade")
    print("4. Display Student")
    print("5. Exit")
    print("=======================================================")
    user_choice = input("Enter your choice: ")
    clear_screen()

    if user_choice == "1":
        add_students()
    elif user_choice == "2":
        access_student_grades()
    elif user_choice == "3":
        update_student_grades()
    elif user_choice == "4":
        view_students()
    elif user_choice == "5":
        print("Exiting....")
        sys.exit()
