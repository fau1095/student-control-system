import csv
import os
from typing import List, Dict, Any

# This module handles the export and import of student data to and from a CSV file.

def export_data(students: List[Dict[str, Any]]) -> None:
    if not students:
        print("No students to export")
        return
    with open("students.csv", mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=students[0].keys())
        writer.writeheader()
        writer.writerows(students)
    print("Data exported to students.csv")

def import_data() -> List[Dict[str, Any]]:
    students: List[Dict[str, Any]] = []
    if not os.path.exists("students.csv"):
        print("No CSV file found to import.")
        return students
    with open("students.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["spanish"] = float(row["spanish"])
            row["english"] = float(row["english"])
            row["social"] = float(row["social"])
            row["science"] = float(row["science"])
            row["average"] = float(row["average"])
            students.append(row)
    print("Data imported from students.csv")
    return students