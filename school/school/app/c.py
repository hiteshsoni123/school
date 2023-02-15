# Designing a school management system database involves identifying the entities involved in the system and the relationships between them. Here is a possible database schema for a school management system:

# Students table:

# Student ID (Primary Key)
# First Name
# Last Name
# Date of Birth
# Gender
# Address
# Phone Number
# Email
# Teachers table:

# Teacher ID (Primary Key)
# First Name
# Last Name
# Date of Birth
# Gender
# Address
# Phone Number
# Email
# Subject Taught
# Classes table:

# Class ID (Primary Key)
# Class Name
# Year Level
# Teacher ID (Foreign Key)
# Enrollments table:

# Enrollment ID (Primary Key)
# Student ID (Foreign Key)
# Class ID (Foreign Key)
# Attendance table:

# Attendance ID (Primary Key)
# Class ID (Foreign Key)
# Date
# Student ID (Foreign Key)
# Status (Present, Absent, Late)
# Grades table:

# Grade ID (Primary Key)
# Class ID (Foreign Key)
# Student ID (Foreign Key)
# Grade
# Users table:

# User ID (Primary Key)
# Username
# Password
# Role (Admin, Teacher, Student)
# In this schema, students, teachers, and classes are the main entities. The enrollments table connects students and classes, while the attendance and grades tables connect students and classes. The users table stores login information and assigns roles to users.

# This is just one example of a possible schema, and it may need to be modified to fit the specific needs of a particular school.




# HITESH SONI
# please give me with example
# Sure! Let's use a hypothetical school called "ABC High School" as an example to illustrate how the school management system database could be designed.

# Students table:
# Student ID	First Name	Last Name	Date of Birth	Gender	Address	Phone Number	Email
# 101	John	Smith	2004-01-01	M	123 Main St, Anytown	555-1234	john.smith@example.com
# 102	Jane	Doe	2004-02-15	F	456 Maple Ave, Othertown	555-5678	jane.doe@example.com
# Teachers table:
# Teacher ID	First Name	Last Name	Date of Birth	Gender	Address	Phone Number	Email	Subject Taught
# 201	David	Johnson	1980-05-10	M	789 Elm St, Somewhere	555-9012	david.johnson@example.com	Math
# 202	Sarah	Lee	1985-08-22	F	321 Oak Rd, Anywhere	555-3456	sarah.lee@example.com	English
# Classes table:
# Class ID	Class Name	Year Level	Teacher ID
# 301	Math 101	10	201
# 302	English 10	10	202
# Enrollments table:
# Enrollment ID	Student ID	Class ID
# 401	101	301
# 402	102	301
# 403	101	302
# 404	102	302
# Attendance table:
# Attendance ID	Class ID	Date	Student ID	Status
# 501	301	2023-02-14	101	Present
# 502	301	2023-02-14	102	Absent
# 503	302	2023-02-14	101	Late
# 504	302	2023-02-14	102	Present
# Grades table:
# Grade ID	Class ID	Student ID	Grade
# 601	301	101	85
# 602	301	102	92
# 603	302	101	88
# 604	302	102	90
# Users table:
# User ID	Username	Password	Role
# 701	admin	admin123	Admin
# 702	djohnson	pass123	Teacher
# 703	slee	pass123	Teacher
# 704	jsmith	pass123	Student
# 705	jdoe		



# HITESH SONI
# and give me these models.py file
# Sure, here's an example models.py file for a Django web application that uses the schema we designed earlier:

# scss
# Copy code
# from django.db import models

# class Student(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     date_of_birth = models.DateField()
#     GENDER_CHOICES = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#         ('O', 'Other'),
#     )
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
#     address = models.CharField(max_length=200)
#     phone_number = models.CharField(max_length=20)
#     email = models.EmailField()

# class Teacher(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     date_of_birth = models.DateField()
#     GENDER_CHOICES = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#         ('O', 'Other'),
#     )
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
#     address = models.CharField(max_length=200)
#     phone_number = models.CharField(max_length=20)
#     email = models.EmailField()
#     subject_taught = models.CharField(max_length=50)

# class Class(models.Model):
#     class_name = models.CharField(max_length=50)
#     year_level = models.IntegerField()
#     teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

# class Enrollment(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     enrolled_class = models.ForeignKey(Class, on_delete=models.CASCADE)

# class Attendance(models.Model):
#     STATUS_CHOICES = (
#         ('P', 'Present'),
#         ('A', 'Absent'),
#         ('L', 'Late'),
#     )
#     date = models.DateField()
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     enrolled_class = models.ForeignKey(Class, on_delete=models.CASCADE)
#     status = models.CharField(max_length=1, choices=STATUS_CHOICES)

# class Grade(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     enrolled_class = models.ForeignKey(Class, on_delete=models.CASCADE)
#     grade = models.DecimalField(max_digits=5, decimal_places=2)

# class User(models.Model):
#     username = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
#     ROLE_CHOICES = (
#         ('A', 'Admin'),
#         ('T', 'Teacher'),
#         ('S', 'Student'),
#     )
#     role = models.CharField(max_length=1, choices=ROLE_CHOICES)
# This models.py file defines Django models that correspond to the tables in our database schema. The ForeignKey fields represent the foreign key relationships between tables, and the choices parameter in some fields defines the available choices for certain fields with a limited set of options. Note that this is just an example, and you may need to modify the models.py file to fit your specific needs.