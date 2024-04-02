import csv
from studentAbout import StudentAbout

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
    
    student_point_one = int(input("Enter Quiz One Point: "))
    student_point_two = int(input("Enter Quiz Two Point : "))

    if((student_point_one+student_point_two)/2>40):
        student_statu = "Passed"
    else:
        student_statu = "Stayed"    

    if selected_index in range(len(student_lesson)):
        selected_lesson = student_lesson[selected_index]
        return StudentAbout(name=student_name, surname=student_surname, lesson=selected_lesson, point_one=student_point_one, point_two=student_point_two, statu=student_statu)
    else:
        print("Invalid lesson. Please try again!")

def save_to_csv(studentabout: StudentAbout, student_file_path):
    print(f"Saving User Parameter : {studentabout} to {student_file_path}")
    with open(student_file_path, "a", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([studentabout.name, studentabout.surname, studentabout.lesson, studentabout.point_one, studentabout.point_two, studentabout.statu])

def student_about_file_path_list(student_about_file_path_list):
    print("Listing Student About:")
    with open(student_about_file_path_list, "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print("Student Name:", row[0])
            print("Student Surname:", row[1])
            print("Student Lesson:", row[2])
            print("Student Quiz Point One:", row[3])
            print("Student Quiz Point Two:", row[4])
            print("Student Lesson Statu:", row[5])
            print()

def main():
    studentabout_file_path = "studentabout.csv"
    while True:
        print("What do you want to do?")
        print("1. Add a student about")
        print("2. List student about")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            studentabout = user_parameter()
            save_to_csv(studentabout, studentabout_file_path)
            print("New student about added successfully!")
        elif choice == "2":
            student_about_file_path_list(studentabout_file_path)
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
