Aiden Fan 101266368
Assignment 3 for COMP 3005

This is a simple Python program that interacts with a PostgreSQL server and performs specific CRUD operations.

Setup:

- Have Python installed on machine.
- Run the following command in the shell of your choice and within the directory of this folder to install psycopg2
  `pip install psycopg2`

Instructions:
If you choose to use your machine's cmd, run the following command to run the program:<br> `python application-code.py`<br>If you choose to run on an IDE like VSCode, just run it<br><br>
The program is connected to the specific database called `studentdb`. The username and password are both `postgres`. The host is `localhost`  and the port is `5432` . 

Create a students table and add the initial data
  This is done in the `database-create-table` sql file.
  Input these commands into the SQL Shell (psql)
    Make sure you're inside the `studentdb` database<br>

Once the program is running, choose inputs to test different CRUD operations:<br>
**ALL INPUTED DATA MUST BE WITHIN CONSTRAINTS**
If your input is:<br>
1. this calls the `getAllStudents()` function
2. this asks for user input `(first_name, last_name, email, enrollment_date)` then calls the `addStudent()` function with that inputted data
3. this asks for user input `(student_id, new_email)` then calls the `updateStudentEmail()` function with the inputted data
4. this asks for user input `(student_id)` then calls the `deleteStudent()` function with the inputted data

Documentation:<br>
`getAllStudents()` - function that retrieves and displays all records from the students table <br>
`addStudent(first_name, last_name, email, enrollment_date)` - inserts a new student record into the students table <br>
`updateStudentEmail(student_id, new_email)` - updates the email address for a student with the specified student_id <br>
`deleteStudent(student_id)` - deletes the record of the student with the specified student_id <br>
`main_menu()` - function that creates a menu for user input then calls corresponding functions until user chooses to exit<br>
`main()` - calls the `main_menu()` function<br>

Video Demo:
https://youtu.be/GgFBXbvQFo4
