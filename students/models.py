from django.db import models

# Create your models here.
class AcademicYear(models.Model):
    options = [
        (1, '1st yaer'),
        (2, '2st yaer'),
        (3, '3st yaer'),
        (4, '4st yaer'),
    ]
    name = models.CharField(max_length=100)
    subject1 = models.CharField(max_length=255, null=True, blank=True)
    subject2 = models.CharField(max_length=255, null=True, blank=True)
    subject3 = models.CharField(max_length=255, null=True, blank=True)
    subject4 = models.CharField(max_length=255, null=True, blank=True)
    subject5 = models.CharField(max_length=255, null=True, blank=True)
    subject6 = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return f'Grade : {self.name}'
    
    
class Student(models.Model):
    student_number = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    field_of_study = models.CharField(max_length=50)
    academic_year_id = models.ForeignKey(AcademicYear, on_delete=models.SET_NULL,null=True)
    gpa = models.FloatField()
    
    def __str__(self):
        return f'Student: {self.first_name} {self.last_name}'
    
    # class Meta:
    #     ordering = ['first_name']

class Teachers(models.Model):
    pass

class Subject(models.Model):
    sub_code = models.CharField(max_length=50)
    sub_name = models.CharField(max_length=50)
    sub_grade = models.ForeignKey(AcademicYear, on_delete=models.SET_NULL, null=True, blank=True)
    sub_description = models.TextField()
    sub_reference = models.CharField(max_length=100)
    sub_teachers = models.ManyToManyField(Teachers, null=True, blank=True)
    
    def __str__(self):
        return self.sub_name