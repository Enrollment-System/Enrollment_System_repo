from django.contrib import admin
from .models import Student,AcademicYear,Subject

# Register your models here.
admin.site.register(Student)
admin.site.register(AcademicYear)
admin.site.register(Subject)