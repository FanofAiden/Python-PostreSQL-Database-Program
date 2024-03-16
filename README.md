Aiden Fan 101266368
Assignment 3 for COMP 3005

This is a simple Python program that interacts with a PostgreSQL server and performs specific CRUD operations.

Setup:

- Have Python installed on machine.
- Run the following command in the shell of your choice and within the directory of this folder to install psycopg2
  ` pip install psycopg2`

Instructions:
The program is connected to the specific database called `studentdb`. The username and password are both `postgres`. The host is `localhost`  and the port is `5432` . 

Create a students table and add the initial data
  This is done in the `database-create-table` sql file.
  Input these commands into the SQL Shell (psql)
    Make sure you're inside the `studentdb` database
  
The functions for INSERT, UPDATE, and DELETE operations are all called separately called in the `application-code` file.

To test, you can uncomment each function call separately to see the individual effects it has on the database in pgAdmin. In the function call to `addStudent()` you can edit the data of the new student that you want to add within the parameters.
The same can be done with the function call to `updateStudentEmail()`.

Documentation:
`getAllStudents()` - function that retrieves and displays all records from the students table
`addStudent(first_name, last_name, email, enrollment_date)` - inserts a new student record into the students table
`updateStudentEmail(student_id, new_email)` - updates the email address for a student with the specified student_id
`deleteStudent(student_id)` - deletes the record of the student with the specified student_id

Video Demo:
[https://youtu.be/49HH5T_Wka8](url)
