from actions import *
from data import *
from student import Student
from typing import List

# This module handles the menu and user interaction for the student management system.

def show_menu(students: List[Student]):
    
    while True:
        print("\nMenu:")
        print("1. Add student")
        print("2. View all students")
        print("3. Top 3 students by average grade")
        print("4. Average grade of all students")
        print("5. Export data to CSV file")
        print("6. Import data from CSV file")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            top_students(students)
        elif choice == "4":
            average_all_students(students)
        elif choice == "5":
            export_data(students)
        elif choice == "6":
            imported = import_data()
            if imported:
                students.clear()
                students.extend(imported)
        elif choice == "0":
            break
        else:
            print("Invalid option. Try again.")

