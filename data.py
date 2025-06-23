import csv
import os
from typing import List
from student import Student

# This module handles the export and import of student data to and from a CSV file.

def export_data(students: List[Student]) -> None:
    if not students:
        print("No students to export")
        return
    try:
        with open("students.csv", mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "section", "spanish", "english", "social", "science", "average"])
            writer.writeheader()
            for student in students:
                writer.writerow(student.to_dict())
        print("Data exported to students.csv")
    except (IOError, OSError) as e:
        print(f"Failed to export data: {e}")

def import_data() -> List[Student]:
    students: List[Student] = []
    if not os.path.exists("students.csv"):
        print("No CSV file found to import.")
        return students
    try:
        with open("students.csv", mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    student = Student(
                        name=row['name'],
                        section=row['section'],
                        spanish=float(row['spanish']),
                        english=float(row['english']),
                        social=float(row['social']),
                        science=float(row['science'])
                    )
                    students.append(student)  
                except (ValueError, KeyError) as parse_error:
                    print(f"Skipping malformed row: {parse_error}")
        print("Data imported from students.csv")
    except (IOError, OSError) as e:
        print(f"Failed to import data: {e}")
    return students