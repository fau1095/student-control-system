def menu():
    student_info_dict = {
        "student_name": input("Enter student name: "),
        "student_section": input("Enter student section: "),
        "spanish_grade": int(input("Enter Spanish grade: ")),
        "english_grade": int(input("Enter English grade: ")),
        "social_studies_grade": int(input("Enter Math grade: ")),
        "science_grade": int(input("Enter Science grade: "))
    }
    student_info_dict["total_average_grades"] = (
        student_info_dict["spanish_grade"] +
        student_info_dict["english_grade"] +
        student_info_dict["social_studies_grade"] +
        student_info_dict["science_grade"]
    ) / 4
    
    grades_counter = 0
    
        

