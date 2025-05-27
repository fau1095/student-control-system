from menu import show_menu
from typing import List, Dict, Any

students: List[Dict[str, Any]] = []  # Define students list as list of dicts

if __name__ == "__main__":
    show_menu(students)  # Pass students to show_menu