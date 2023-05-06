from django.db import models

# Create your models here.
class AcademicYear(models.Model):
    name = models.CharField(max_length=255)
    # subject1 = models.CharField
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

class Department(models.Model):
    dep_name = models.CharField(max_length=50)
    dep_n= models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.dep_name} Department' 
    
class Teacher(models.Model):
    tech_first_name =  models.CharField(max_length=50)
    tech_last_name =  models.CharField(max_length=50)
    tech_email =  models.EmailField(max_length=50)
    tech_department =  models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    tec_dob = models.DateField()
    
    def __str__(self):
        return f'DR {self.tech_first_name} {self.tech_last_name}'
    pass
    

class Subject(models.Model):
    sub_code = models.CharField(max_length=50)
    sub_name = models.CharField(max_length=50)
    sub_grade = models.ForeignKey(AcademicYear, on_delete=models.SET_NULL, null=True, blank=True)
    sub_description = models.TextField()
    sub_reference = models.CharField(max_length=100)
    sub_teacher = models.ForeignKey(Teacher,on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.sub_name