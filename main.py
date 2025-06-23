from menu import show_menu
from student import Student
from typing import List

def main():
    students: List[Student] = []  # Local variable for students
    show_menu(students)  # Pass students as argument

if __name__ == "__main__":
    main()  # Pass students to show_menu