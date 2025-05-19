# This module provides functions to manage a student database, including adding students, viewing details, and calculating averages.

def validate_grade(prompt):
    while True:
        try:
            grade = float(input(prompt))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Enter a numeric value.")

def add_student(students):
    while True:
        name = input("Full name: ")
        if not name.replace(" ", "").isalpha():
            print("Invalid name. Please enter only letters.")
        else:
            break

    section = input("Section: ")
    spanish = validate_grade("Spanish grade: ")
    english = validate_grade("English grade: ")
    social = validate_grade("Social Studies grade: ")
    science = validate_grade("Science grade: ")

    student = {
        "name": name,
        "section": section,
        "spanish": spanish,
        "english": english,
        "social": social,
        "science": science,
        "average": (spanish + english + social + science) / 4
    }
    students.append(student)
    print("Student added successfully.")

def view_students(students):
    if not students:
        print("No students found.")
        return
    for i, student in enumerate(students, 1):
        print(f"\nStudent {i}:")
        for key, value in student.items():
            print(f"{key.title()}: {value}")

def top_students(students):
    if len(students) < 3:
        print("Not enough students to determine top 3.")
        return
    top = sorted(students, key=lambda x: x["average"], reverse=True)[:3]
    for i, student in enumerate(top, 1):
        print(f"\nTop {i}:")
        print(f"Name: {student['name']}, Average: {student['average']:.2f}")

def average_all_students(students):
    if not students:
        print("No students to average.")
        return
    total = sum(s["average"] for s in students)
    print(f"Overall average: {total / len(students):.2f}")