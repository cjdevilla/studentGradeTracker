from array import array

# Creating an array of integers
students = []

options = [
    "Add Student",
    "View Student Grades",
    "View Subject Averages",
    "Identify Top Performers",
    "Update Grades",
    "Exit"
]

def display_options():
    while True:
        for index, option in enumerate(options, start=1):
            print(f"{index}. {option}")

        selected_option = int(input("Enter your choice: "))

        if selected_option == 1:
            add_student()
        elif selected_option == 2:
            view_student_grades()
        elif selected_option == 3:
            view_subject_averages()
        elif selected_option == 6:
            print("Goodbye!")
            break

def add_student():
    student_name = input("Enter student name: ")
    math_grade = float(input(f"Enter {student_name}'s Math grade: "))
    english_grade = float(input(f"Enter {student_name}'s English grade: "))
    science_grade = float(input(f"Enter {student_name}'s Science grade: "))

    student_info = (student_name, array('f', [math_grade, english_grade, science_grade]))
    students.append(student_info) # "Joy" , [89.0, 90.0, 89.0]

    return student_info

def view_student_grades():
    if not students:
        print("No students to display.\n")
    else:
        for student_info in students:
            print("Student:", student_info[0])
            print(f"Subject: Math, Grade: ", student_info[1][0])
            print(f"Subject: English, Grade: ", student_info[1][1])
            print(f"Subject: Science, Grade: ", student_info[1][2])
            print()

def view_subject_averages():
    if not students:
        print("No students to calculate averages.")
        return

    all_math_grades = []
    all_english_grades = []
    all_science_grades = []
    count = 0

    for student_info in students:
        math_individual_grade = student_info[1][0]
        english_individual_grade = student_info[1][1]
        science_individual_grade = student_info[1][2]
        count += 1
        all_math_grades.append(math_individual_grade)
        all_english_grades.append(english_individual_grade)
        all_science_grades.append(science_individual_grade)

    if count > 0:
        average_math = sum(all_math_grades) / count
        print("Average Math Grade: ", average_math)
        average_english = sum(all_english_grades) / count
        print("Average English Grade: ", average_english)
        average_science = sum(all_science_grades) / count
        print("Average Science Grade: ", average_science)
    else:
        print("No students to calculate averages.")
           
display_options()