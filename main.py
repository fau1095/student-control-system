from menu import show_menu
from typing import List, Dict, Any

def main():
    students: List[Dict[str, Any]] = []  # Local variable for students
    show_menu(students)  # Pass students as argument

if __name__ == "__main__":
    main()  # Pass students to show_menu