from django.contrib import admin

from .models import Teacher, Student, Parent

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Parent)