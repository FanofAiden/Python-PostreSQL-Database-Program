#AIDEN FAN 101266368

import psycopg2
from psycopg2 import sql

connection = psycopg2.connect(
    dbname="studentdb",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)

currentConnect = connection.cursor()

def getAllStudents():
    currentConnect.execute("SELECT * FROM students;")
    records = currentConnect.fetchall()
    for record in records:
        print(record)

def addStudent(first_name, last_name, email, enrollment_date):
    currentConnect.execute(
        "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);",
        (first_name, last_name, email, enrollment_date)
    )
    connection.commit()

def updateStudentEmail(student_id, new_email):
    currentConnect.execute(
        "UPDATE students SET email = %s WHERE student_id = %s;",
        (new_email, student_id)
    )
    connection.commit()

def deleteStudent(student_id):
    currentConnect.execute(
        "DELETE FROM students WHERE student_id = %s;",
        (student_id,)
    )
    connection.commit()

def main_menu():
    while True:
        print("\n--- Student Management System ---")
        print("1. Get all students")
        print("2. Add a new student")
        print("3. Update student email")
        print("4. Delete a student")
        print("0. Exit")
        choice = input("Enter your choice (0-4): ")

        if choice == "1":
            print("\nGetting all students:")
            getAllStudents()

        elif choice == "2":
            print("\nAdding a new student:")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ")
            addStudent(first_name, last_name, email, enrollment_date)
            print("---Student Added Successfully---")

        elif choice == "3":
            print("\nUpdating student email:")
            student_id = int(input("Enter student ID to update email for: "))
            new_email = input("Enter new email: ")
            updateStudentEmail(student_id, new_email)
            print("---Student Email Updated Successfully---")

        elif choice == "4":
            print("\nDeleting a student:")
            student_id = int(input("Enter student ID to delete: "))
            deleteStudent(student_id)
            print("---Student Record Deleted Sucessfully---")

        elif choice == "0":
            print("Exit Successful")
            break
        else:
            print("Invalid choice, please enter a number between 0 and 4.")

def main():
    main_menu()

main()

currentConnect.close()
connection.close()
