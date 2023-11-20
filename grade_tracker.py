from array import array

# Creating an array of integers
# students = []

options = [
    "Add Student",
    "View Student Grades",
    "View Subject Averages",
    "Identify Top Performers",
    "Update Grades",
    "Exit"
]

def main():
    students = []
    subjects = ["Math", "English" , "Science"]
    grades = []

    student_info = (student_name, subjects, array('f', [grades]))

    while True:
        for index, option in enumerate(options, start=1):
            print(f"{index}. {option}")

        selected_option = int(input("Enter your choice: "))

        if selected_option == 1:
            student_name = input("Enter student name: ")
            new_grades = [(subject, int(input(f"Enter {subject} grade: "))) for subject in subjects]
            # grades.extend(new_grades)
            add_student(students, grades, student_name, new_grades)
        elif selected_option == 2:
            view_student_grades(students, grades)
        elif selected_option == 3:
            view_subject_averages(students ,grades, new_grades)
        elif selected_option == 4:
            identify_top_performers()
        elif selected_option == 6:
            print("Goodbye!")
            break

def add_student(students, grades, student_name, new_grades):
    # student_name = input("Enter student name: ")
    # math_grade = float(input(f"Enter {student_name}'s Math grade: "))
    # english_grade = float(input(f"Enter {student_name}'s English grade: "))
    # science_grade = float(input(f"Enter {student_name}'s Science grade: "))

    # student_info = (student_name, array('f', [math_grade, english_grade, science_grade]))
    students.append(student_name) # "Joy" , [89.0, 90.0, 89.0]
    grades.extend(new_grades)


    # return student_info


def view_student_grades(students, grades):
    for index, student in enumerate(students, start=1):
        print(f"{index}. {student}")
        for i, grade in enumerate(grades, start=1):
            print(f"Subject: {grade[0]}, Grade: {grade[1]}")
    # if not students:
    #     print("No students to display.\n")
    # else:
    #     for student_info in students:
    #         print("Student:", student_info[0])
    #         print(f"Subject: Math, Grade: ", student_info[1][0])
    #         print(f"Subject: English, Grade: ", student_info[1][1])
    #         print(f"Subject: Science, Grade: ", student_info[1][2])

            
# def calculate_subject_averages():
#     all_math_grades = []
#     all_english_grades = []
#     all_science_grades = []
#     count = 0

#     for grade in grades:
#         math_individual_grade = grade[1][0]
#         english_individual_grade = grade[1][1]
#         science_individual_grade = grade[1][2]
#         count += 1
#         all_math_grades.append(math_individual_grade)
#         all_english_grades.append(english_individual_grade)
#         all_science_grades.append(science_individual_grade)

#     if count > 0:
#         average_math = sum(all_math_grades) / count
#         print("Average Math Grade: ", average_math)
#         average_english = sum(all_english_grades) / count
#         print("Average English Grade: ", average_english)
#         average_science = sum(all_science_grades) / count
#         print("Average Science Grade: ", average_science)
#     else:
#         print("No students to calculate averages.")   


def view_subject_averages(students, grades, new_grades):
    all_math_grades = []
    all_english_grades = []
    all_science_grades = []

    count = 0

    if not students:
        print("No students to calculate averages.")
        return

    for new_grade in new_grades:
        math_individual_grade = new_grade[1] if new_grade[0] == "Math" else 0
        english_individual_grade = new_grade[1] if new_grade[0] == "English" else 0
        science_individual_grade = new_grade[1] if new_grade[0] == "Science" else 0
        count += 1
        all_math_grades.append(math_individual_grade)
        all_english_grades.append(english_individual_grade)
        all_science_grades.append(science_individual_grade)

    count = len(students)
    if count > 0:
        average_math = sum(all_math_grades) / count
        print("Average Math Grade: ", average_math)
        average_english = sum(all_english_grades) / count
        print("Average English Grade: ", average_english)
        average_science = sum(all_science_grades) / count
        print("Average Science Grade: ", average_science)
    else:
        print("No students to calculate averages.")


def identify_top_performers():
    number_of_top_performer = input("Enter the number of top performer to show: ")
    top_performers = []
    highest_average_grade = 0

    for student_info in students:
        student_name = student_info[0]
        average_grade = sum(student_info[1]) / len(student_info[1])

        if average_grade > highest_average_grade:
            top_performers = [student_name]
            highest_average_grade = average_grade
        elif average_grade == highest_average_grade:
            top_performers.append(student_name)

    if top_performers:
        print("\nTop Performers:")
        print(f"{rank}. {performer}: {highest_average_grade}")
    else:
        print("No top performers found.")
    

# display_options()
main()