from django.contrib import admin
# Importamos las 4 clases exactas de tu archivo models.py
from .models import Courses, CoursesStudents, Student, Users

# Registramos cada una en el panel administrador de Django
admin.site.register(Courses)
admin.site.register(CoursesStudents)
admin.site.register(Student)
admin.site.register(Users)