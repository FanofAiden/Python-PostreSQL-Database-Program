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

try:        #uncomment each function call individually to test and see individual effects of each function
    # print("Getting all students:")
    # getAllStudents()

    # print("Adding a new student:")
    # addStudent('Aiden', 'Fan', 'aiden.fan@carleton.ca', '2024-03-14')
    # getAllStudents()

    # print("Updating student email:")
    # updateStudentEmail(4, 'aiden.fan@newemail.ca')
    # getAllStudents()

    # print("Deleting a student:")
    # deleteStudent(4)
    # getAllStudents()

except Exception as e:
    print("An error occurred:", e)

finally:
    if currentConnect:
        currentConnect.close()
    if connection:
        connection.close()

currentConnect.close()
connection.close()
