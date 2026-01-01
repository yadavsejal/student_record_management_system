import csv
import os


# Configuration

CSV_FILE = "Students.csv"
FIELDNAMES = ["Student_ID", "Name", "Age", "Course", "Marks"]


# CSV Initialization

def initialize_csv():
    """
    Checks if CSV exists and is valid.
    If missing or corrupted, creates a fresh CSV.
    """
    if not os.path.exists(CSV_FILE):
        create_clean_csv()
    else:
        try:
            with open(CSV_FILE, "r", newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                if reader.fieldnames != FIELDNAMES:
                    print("Corrupt CSV file detected. Recreating...")
                    create_clean_csv()
        except Exception:
            print("CSV error detected. Recreating file...")
            create_clean_csv()


def create_clean_csv():
    """
    Creates a fresh CSV file with headers.
    """
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
    print("Fresh CSV created successfully.")


# Utility Functions

def read_all_students():
    """
    Reads all student records from CSV.
    """
    students = []
    try:
        with open(CSV_FILE, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                students.append(row)
    except Exception as e:
        print("Error reading file:", e)
    return students


def find_student_by_StudentID(Student_ID):
    """
    Searches for a student by Student ID.
    """
    students = read_all_students()
    for student in students:
        if student["Student_ID"] == Student_ID:
            return student
    return None


# CRUD Operations

def add_student():
    Student_ID = input("Enter Student ID: ").strip()
    if not Student_ID:
        print("Student ID cannot be empty.")
        return

    if find_student_by_StudentID(Student_ID):
        print("Student ID already exists.")
        return

    Name = input("Enter Name: ").strip()
    Age = input("Enter Age: ").strip()
    Course = input("Enter Course: ").strip()
    Marks = input("Enter Marks: ").strip()

    if not Name or not Age or not Course or not Marks:
        print("All fields are required.")
        return

    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writerow({
            "Student_ID": Student_ID,
            "Name": Name,
            "Age": Age,
            "Course": Course,
            "Marks": Marks
        })

    print("Student added successfully.")


def view_students():
    students = read_all_students()
    if not students:
        print("No student records found.")
        return

    print("\nStudent_ID | Name | Age | Course | Marks")
    print("-" * 55)
    for s in students:
        print(f"{s['Student_ID']} | {s['Name']} | {s['Age']} | {s['Course']} | {s['Marks']}")


def update_student(Student_ID):
    students = read_all_students()
    found = False

    for student in students:
        if student["Student_ID"] == Student_ID:
            found = True
            print("\nLeave blank to keep existing value")

            name = input(f"New Name [{student['Name']}]: ").strip()
            age = input(f"New Age [{student['Age']}]: ").strip()
            course = input(f"New Course [{student['Course']}]: ").strip()
            marks = input(f"New Marks [{student['Marks']}]: ").strip()

            if name:
                student["Name"] = name
            if age:
                student["Age"] = age
            if course:
                student["Course"] = course
            if marks:
                student["Marks"] = marks
            break

    if not found:
        print("Student ID not found.")
        return

    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(students)

    print("Student updated successfully.")


def delete_student(Student_ID):
    students = read_all_students()
    updated_students = [s for s in students if s["Student_ID"] != Student_ID]

    if len(students) == len(updated_students):
        print("Student ID not found.")
        return

    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(updated_students)

    print("Student deleted successfully.")


# Main Menu

def main():
    initialize_csv()

    while True:
        print("\n--- Student Record Management System ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by ID")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            sid = input("Enter Student ID: ").strip()
            student = find_student_by_StudentID(sid)
            if student:
                print("\nStudent Found:")
                for k, v in student.items():
                    print(f"{k}: {v}")
            else:
                print("Student not found.")
        elif choice == "4":
            sid = input("Enter Student ID to update: ").strip()
            update_student(sid)
        elif choice == "5":
            sid = input("Enter Student ID to delete: ").strip()
            delete_student(sid)
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1–6.")


# Entry Point

if __name__ == "__main__":
    main()
