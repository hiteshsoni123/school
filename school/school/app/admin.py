from django.contrib import admin

from .models import Teacher, Student, Parent,Class,ClassRoom,Enrollment,Subject,Attendance,Grade

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Class)
admin.site.register(ClassRoom)
admin.site.register(Enrollment)
admin.site.register(Subject)
admin.site.register(Attendance)
admin.site.register(Grade)

