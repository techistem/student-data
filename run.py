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

