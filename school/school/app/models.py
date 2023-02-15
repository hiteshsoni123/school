from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    date_of_birth = models.DateField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    address = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    email = models.EmailField(null=True)
    image = models.ImageField(upload_to ='uploads/', null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True

class Teacher(Person):
    qualifications = models.JSONField()

class Student(Person):
    pass

class Parent(Person):
    child_name = models.CharField(Student,max_length=50,null=True)

class Class(models.Model):
    class_name = models.CharField(max_length=50, null=True)
    SECTION_CHOICES = (
        ('A', 'SECTION A'),
        ('B', 'SECTION B'),
        ('C', 'SECTION C'),
    )
    year_section = models.CharField(max_length=1, choices=SECTION_CHOICES, null=True)
    class_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

class ClassRoom(models.Model):
    class_room_name = models.ForeignKey(Class,on_delete=models.CASCADE, null=True)
    Student_name = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    teacher_assign = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    enrolled_class = models.ForeignKey(Class, on_delete=models.CASCADE, null=True)
    enrollment_number = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class Subject(models.Model):
    subject_name = models.CharField(max_length=50,null=True)
    Teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

 

class Attendance(models.Model):
    STATUS_CHOICES = (
        ('P', 'Present'),
        ('A', 'Absent'),
        ('L', 'Late'),
    )
    date = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE,null=True)
    Teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE,null=True)
    enrolled_class = models.ForeignKey(Class, on_delete=models.CASCADE,null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,null=True)
    enrolled_class = models.ForeignKey(Class, on_delete=models.CASCADE,null=True)
    grade = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)













