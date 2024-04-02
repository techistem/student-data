import csv
from studentAbout import StudentAbout

def user_parameter():
    print("Welcome Automation")
    student_name = input("Enter Student Name: ")
    student_surname = input("Enter Student Surname: ")
    
    print("Select a lesson : ")
    student_lesson = [
        "English",
        "Science",
        "Math",
        "History",
    ]
    for i, lesson_name in enumerate(student_lesson):
        print(f" {i + 1}.{lesson_name}")

    value_range = f"[1 - {len(student_lesson)}]"
    selected_index = int(input(f"Enter a lesson number {value_range}: ")) - 1
    
    student_point_one = int(input("Enter Quiz One Point: "))
    student_point_two = int(input("Enter Quiz Two Point : "))

    if((student_point_one+student_point_two)/2>40):
