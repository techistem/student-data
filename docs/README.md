# **Student Data**

## **Overview**

This Student Data program is useful for teachers or administrators to manage student records easily. They can add new student data, view existing data, 
and have it all organized neatly in a Google Sheet.

It is built using Python and runs through the Code institute mock terminal on Heroku.

Welcome to <a href="https://student-data-706119549c09.herokuapp.com/" target="_blank" rel="noopener">Student Data</a>

![Responsive design](screenshots/student-data-welcome-screen.png)


# **Planing Stage**

## **_User Stories:_**

As a user, I want to be able to:

1. As an administrator,
I want to add a new student's data so that their information is stored in the system.
2. As a teacher,
I want to view a list of all student data so that I can have an overview of all students in the system.
3. As a teacher,
I want to calculate a student's average grade so that I can assess their performance in the course.
4. As a teacher,
I want to filter students by lesson so that I can view the performance of students in a specific lesson.
5. As an administrator,
I want to update a student's information so that the data in the system remains accurate.
6. As an administrator,
I want to delete a student's data so that their information is removed from the system.

## **_Site Aims:_**

The site aims to:

1. Users can input student information, including name, surname, lesson, and exam scores.
2. Users can list and display student data from Google Sheets worksheet.
3. Describes how the program saves the entered student data to the worksheet.
4. Users are encouraged to provide feedback or report issues for program improvement.

## **_Path to Achieve:_** 

To achieve the above, the site will:

1. When the user enters information that is not valid, a message should appear on the screen explaining what to do and how to continue.
2. Create an option so that the user can check the information they enter.
3. Provide the user with the opportunity to easily view and delete the information they enter.

## **_Student Data Flow Chart:_**

I created the following flow chart using [lucid charts] (https://www.lucidchart.com/) to outline the necessary steps for programming
the student data recording system.

![Student Data Logic Flowchart](screenshots/student-data-flowchart.png)  

# **Features**

This Python program allows users to manage and record student data using Google Sheets.
The features included in this programme are listed in the main menu and they can be seen below:

![Main Menu](screenshots/student-data-main-menu.png)

## **Add student data:**

When the user selects the add new student option, the program will be asked to enter student information.

![Add Student Data](screenshots/student-data1.png)

## **List Student Data**

- The program can list and display student data from the Google Sheets worksheet.
- Accordingly, the student's name, surname, course, and average exam 
scores are reflected on the screen.
- The system automatically calculates the student's status (Pass/Fail) based on their exam scores.

![List Student Data](screenshots/list-student-data.png)

### **Google Sheets Integration**

Utilizes Google Sheets API for data storage and retrieval.

### **Validated Input** 

Input validation ensures correct data entry, prompting users when invalid input is provided.

![Validated Input](screenshots/Validated-Input.png)

### **Flexible Lesson Selection**

Users can select from a list of predefined lessons: English, Science, Math, and History.

![Flexible Lesson Selection](screenshots/lesson-section.png)

### **Feedback and Error Handling**

The program provides feedback on successful data entry and error messages for invalid inputs.

![Feedback and Error Handling](screenshots/feedback-error-handling.png)

### **Exit**

Users can exit the program at any time.

![Exit](screenshots/exitt.png)

# **Future-Enhancements**

Here are some potential improvements and features that I could add to enhance the functionality of the program:

- **User Authentication**: I can implement user authentication to ensure only authorized users can access and modify student data.
  
- **Search and Filter**: I can add functionality to search for specific students or filter students by criteria such as lesson, score, or status.

- **Update and Delete**: I can include options to update and delete student records directly from the program interface.

- **Data Visualization**: I can integrate data visualization tools to create charts and graphs for better data analysis and insights.

- **Email Notifications**: I can send automated email notifications to teachers or administrators for important events, such as new student entries or low scores.

- **CSV Import/Export**: I can allow users to import student data from CSV files and export data to CSV for easy sharing and backup.

- **Mobile App**: I can develop a mobile app version of the program for convenient access on smartphones and tablets.

These enhancements could make the program more versatile, user-friendly, and efficient for managing student data.

# **Technologies Used**

I have used several technologies that have enabled this design to work:

-[Python](https://www.python.org/)
- The entirety of the code in this application is composed using Python as the fundamental programming language, ensuring its complete functionality.
    - In addition to core Python I have used the following Python modules:
        - [Gspread](https://docs.gspread.org/en/latest/)
            - Used to access my google sheets document throughout the application, to access and edit data.
        - [Google Auth](https://google-auth.readthedocs.io/en/master/)
            - Used to provide access to the application to interact with my google sheet.
- [GitHub](https://github.com/)
    - Used to store code for the project after being pushed.
- [Git](https://git-scm.com/)
    - Used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
- [Gitpod](https://www.gitpod.io/)
    - Used as the development environment.
- [Heroku](https://dashboard.heroku.com/apps)
    - Used to deploy my application.
- [Lucid](https://lucid.app/documents#/dashboard)
    - Used to create the flowchart for the project.
- [Grammarly](https://www.grammarly.com/)
    - Used to fix the grammar errors across the project.
- [Google Sheets](https://www.google.co.uk/sheets/about/)
    - Used to store the 'Contacts' data used for the application.
- [Pep8](https://pep8ci.herokuapp.com/)
    - Used to test my code for any issues or errors.

# **Testing Phase**

I have written my testing in a different file for both during-development and post-development called [TESTING.md](TESTING.md).


        


















