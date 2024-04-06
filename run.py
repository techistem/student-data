import csv
from studentData import studentData

def user_parameter():
    print("Welcome Automation")
    student_name = None
    student_surname = None
    while True:
        student_name = input("Enter Student Name: ")
        if student_name.isalpha():
            break
        else:
            print(f"{student_name} is invalid. Please use only letters.")

    while True:
        student_surname = input("Enter Student Surname: ")
        if student_surname.isalpha():
            break
        else:
            print(f"{student_surname} is invalid. Please use only letters.")
    
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
    
    student_exam_score_one = int(input("Enter Exam Score One : "))
    student_exam_score_two = int(input("Enter Exam Score Two : "))

    if((student_exam_score_one +student_exam_score_two)/2>40):
        student_status = "Passed"
    else:
        student_status = "Fail"    

    if selected_index in range(len(student_lesson)):
        selected_lesson = student_lesson[selected_index]
        return StudentData(name=student_name, surname=student_surname, lesson=selected_lesson, score_one=student_score_one, score_two=student_score_two, status=student_status)
    else:
        print("Invalid lesson. Please try again!")

def save_to_csv(studentdata: StudentData, student_file_path):
    print(f"Saving User Parameter : {studentdata} to {student_file_path}")
    with open(student_file_path, "a", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([studentdata.name, studentdata.surname, studentdata.lesson, studentdata.score_one, studentdata.score_two, studentdata.status])

def student_data_file_path_list(student_data_file_path_list):
    print("Listing Student Data:")
    with open(student_data_file_path_list, "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print("Student Name:", row[0])
            print("Student Surname:", row[1])
            print("Student Lesson:", row[2])
            print("Student Exam Score One:", row[3])
            print("Student Exam Score Two:", row[4])
            print("Student Lesson Status:", row[5])
            print()

def main():
    studentdata_file_path = "studentdata.csv"
    while True:
        print("What do you want to do?")
        print("1. Add a student data")
        print("2. List student data")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            studentdata = user_parameter()
            save_to_csv(studentdata, studentdata_file_path)
            print("New student data added successfully!")
        elif choice == "2":
            student_data_file_path_list(studentdata_file_path)
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
