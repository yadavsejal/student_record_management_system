# student_record_management_system
This project is based on Student Record Management System developed using Python.
It allows users to manage student records by performing basic CRUD (Create, Read, Update, Delete) operations using file-based storage (CSV) without using any database.

How to Run the Program

Prerequisites
Python 3.10.1 installed on the system

Steps to Run
1.Clone the GitHub repository or download the project files.
2.Open a terminal / command prompt.
3.Navigate to the project directory.
4.Run the command.
5.The program will start and display a menu with available options.

Features Implemented

- Add new student records
- Ensure unique Student ID
- View all student records in a readable format
- Search student by Student ID
- Update existing student details
- Delete student records
- Automatic save and load of data using CSV file
- CSV file validation and auto-creation if missing or corrupted
- Menu-driven user interface
- File-based persistence without using any database

Assumptions Made

- Each student has a unique Student ID
- Student data is stored in a CSV file, not in a database
- Age and Marks are entered correctly by the user
- The number of records is small to medium, so linear search is sufficient

