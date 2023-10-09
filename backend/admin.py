from django.contrib import admin
from .models import Student, Teacher, Parent

admin.site.register(Parent)
admin.site.register(Teacher)
admin.site.register(Student)

# Customizing the admin dashboard

admin.site.site_header = 'Ibn Rochd University Administration'
