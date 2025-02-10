import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('student-data')


class StudentData():
    """A class to represent student data."""

    def __init__(
         self, name, surname, lesson, score_one, score_two, status) -> None:
        self.name = name
        self.surname = surname
        self.lesson = lesson
        self.score_one = score_one
        self.score_two = score_two
        self.status = status


def user_parameter():
    """
    Collects user input for student information and returns a StudentData
    object.
    This function prompts the user to enter the student's name, surname,
    lesson, exam scores, and calculates the student's status based on their
    average score.
    """

    print("Welcome Automation")
    student_name = None
    student_surname = None
    while True:
        student_name = input("Enter Student Name: ")
        if student_name.isalpha() and len(student_name) > 1:
            break
        else:
            print(
                f"{student_name} is invalid. Please use only letters and must be longer than 1 character.")

    while True:
        student_surname = input("Enter Student Surname: ")
        if student_surname.isalpha() and len(student_surname) > 1:
            break
        else:
            print(
                f"{student_surname} is invalid. Please use only letters and must be longer than 1 character..")

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
    while True:
        user_input = input(f"Enter a lesson number {value_range}:")
        if user_input.isdigit():
            selected_index = int(user_input) - 1
        if 0 <= selected_index < len(student_lesson):
            break 
        else:
            print(
                "Invalid lesson number.Please enter a valid lesson number.")
    while True:
        student_exam_score_one = input("Enter Exam Score One:")
        if student_exam_score_one.isdigit():
            student_exam_score_one = int(student_exam_score_one)
            break
        else:
            print(
             f"{student_exam_score_one} is invalid. Please use only numbers.")

    while True:
        student_exam_score_two = input("Enter Exam Score Two:")
        if student_exam_score_two.isdigit():
            student_exam_score_two = int(student_exam_score_two)
            break
        else:
            print(
             f"{student_exam_score_two} is invalid. Please use only numbers.")

    if (student_exam_score_one + student_exam_score_two) / 2 > 40:
        student_status = "Passed"
    else:
        student_status = "Fail"

    if selected_index in range(len(student_lesson)):
        selected_lesson = student_lesson[selected_index]
        return StudentData(
            name=student_name, surname=student_surname, lesson=selected_lesson,
            score_one=student_exam_score_one, score_two=student_exam_score_two,
            status=student_status)
    else:
        print("Invalid lesson. Please try again!")


def save_to_sheet(studentdata):
    """Saves student data to a Google Sheets worksheet."""
    worksheet = SHEET.worksheet("studentData")
    worksheet.append_row([
                          studentdata.name, studentdata.surname,
                          studentdata.lesson, studentdata.score_one,
                          studentdata.score_two,
                          studentdata.status])
    print("New student data added successfully!")


def student_data_gspread_list():
    """Fetches and lists student data from a Google Sheets worksheet."""
    worksheet = SHEET.worksheet("studentData")
    rows = worksheet.get_all_values()
    print("Listing Student Data:")
    for row in rows:
        print("Student Name:", row[0])
        print("Student Surname:", row[1])
        print("Student Lesson:", row[2])
        print("Student Exam Score One:", row[3])
        print("Student Exam Score Two:", row[4])
        print("Student Lesson Status:", row[5])
        print()


def main():
    """
    This function provides a menu-driven interface for interacting with
    student data.
    """
    while True:
        print("What do you want to do?")
        print("1. Add a student data")
        print("2. List student data")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            StudentData = user_parameter()
            save_to_sheet(StudentData)

        elif choice == "2":
            student_data_gspread_list()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()