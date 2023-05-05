from django import forms
from .models import Student, AcademicYear, Subject

class StudentForm(forms.ModelForm):
    # academic_year = queryset=AcademicYear.objects.all()
    class Meta:
        model = Student
        fields = ['student_number', 'first_name', 'last_name', 'email', 'field_of_study', 'academic_year_id', 'gpa']
        labels = {
            'student_number': 'Student Number', 
            'first_name': 'First Name', 
            'last_name': 'Last Name', 
            'email': 'Email', 
            'field_of_study': 'Field of Study', 
            'academic_year_id' : 'Academic Year',
            'gpa': 'GPA'
        }
        widgets = {
            'student_number': forms.NumberInput(attrs={'class': 'form-control'}), 
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'field_of_study': forms.TextInput(attrs={'class': 'form-control'}),
            'academic_year_id': forms.Select(attrs={'class': 'form-control'}),
            'gpa': forms.NumberInput(attrs={'class': 'form-control','min':'0', 'max':'4'}),
        }

class AcademicYearForm(forms.ModelForm):
    class Meta:
        model = AcademicYear
        fields = ['subject1','subject2','subject3','subject4','subject5','subject6']
        labels = {
            'subject1' : 'Subject 1',
            'subject2' : 'Subject 2',
            'subject3' : 'Subject 3',
            'subject4' : 'Subject 4',
            'subject5' : 'Subject 5',
            'subject6' : 'Subject 6',
        }
        widgets = {
            'subject1': forms.TextInput(attrs={'class': 'form-control'}),
            'subject2': forms.TextInput(attrs={'class': 'form-control'}),
            'subject3': forms.TextInput(attrs={'class': 'form-control'}),
            'subject4': forms.TextInput(attrs={'class': 'form-control'}),
            'subject5': forms.TextInput(attrs={'class': 'form-control'}),
            'subject6': forms.TextInput(attrs={'class': 'form-control'}),
        }
  
class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['sub_code', 'sub_name', 'sub_grade','sub_description','sub_reference','sub_teacher']
        labels ={
            'sub_code' : 'Subject Code',
            'sub_name' : 'Subject Name',
            'sub_grade' : 'Subject Grade',
            'sub_description' : 'Subject Description',
            'sub_reference' : 'Subject reference',
            'sub_teacher' : 'Subject Teachers',    
        }
        widgets = {
            'sub_code' : forms.TextInput(attrs={'class': 'form-control'}),
            'sub_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'sub_grade' : forms.Select(attrs={'class': 'form-control'}),
            'sub_description' : forms.Textarea(attrs={'class': 'form-control'}),
            'sub_reference' : forms.TextInput(attrs={'class': 'form-control'}),
            'sub_teacher' : forms.Select(attrs={'class': 'form-control'}),    
        }