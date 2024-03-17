#AIDEN FAN 101266368

import psycopg2
from psycopg2 import sql

#this function connects the application to the specific database
connection = psycopg2.connect(
    dbname="studentdb",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)

currentConnect = connection.cursor()

#this function fetches all students from the students table
def getAllStudents():
    currentConnect.execute("SELECT * FROM students;")
    records = currentConnect.fetchall()
    for record in records:
        print(record)

#this function performs the INSERT operation and adds a student into the students table with user input data
def addStudent(first_name, last_name, email, enrollment_date):
    currentConnect.execute(
        "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);",
        (first_name, last_name, email, enrollment_date)
    )
    connection.commit()

#this function performs the UPDATE operation and updates a student's email in the students table with user input data
def updateStudentEmail(student_id, new_email):
    currentConnect.execute(
        "UPDATE students SET email = %s WHERE student_id = %s;",
        (new_email, student_id)
    )
    connection.commit()

#this function performs the DELETE operation and deletes a student's record in the students table with user input data
def deleteStudent(student_id):
    currentConnect.execute(
        "DELETE FROM students WHERE student_id = %s;",
        (student_id,)
    )
    connection.commit()

#this function provides a main menu for the user to choose what CRUD oepration they want to test, it asks for multiple inputs
def main_menu():
    global exiting
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
            exiting = True
            print("Exit Successful")
            break
        else:
            print("Invalid choice, please enter a number between 0 and 4.")

def main():
    main_menu()
    #if the user exits, it drops the table ---THIS PART IS NOT SHOWN IN VIDEO---
    if exiting:
        with connection.cursor() as cur:
            cur.execute("DROP TABLE students;")
            connection.commit()
        connection.close

exiting = False
main()

currentConnect.close()
connection.close()
