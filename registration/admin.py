from django.contrib import admin
from .models import Course, Student

admin.site.site_header = "Class Registration System Admin Panel"
admin.site.site_title = "Class Registration Admin"
admin.site.index_title = "Welcome to the Class Registration System"

admin.site.register(Course)
admin.site.register(Student)
