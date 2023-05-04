from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse 

from .models import Student, AcademicYear, Subject
from .forms import StudentForm,AcademicYearForm

# Create your views here.
def index(request):
    return render(request, 'students/index.html', {
        'students': Student.objects.all(),
        # 'academic_years': AcademicYear.objects.all(),
    })
    
def academic_years(request):
    return render(request, 'students/academic_years.html', {
        'academic_years': AcademicYear.objects.all(),
    })
    
def all_subjects(request):
    return render(request, 'students/all_subjects.html', {
        'subjects': Subject.objects.all(),
    })

def view_student(request, id):
    student = Student.objects.get(pk=id)
    academic_year = AcademicYear.objects.get(pk=student.academic_year_id)
    print('ok')
    return render(request,'index',{
        'academic_year':academic_year
    })


def show_student(request, id):
    student = Student.objects.get(pk=id)
    academic_year = student.academic_year_id
    
    return render(request,'students/show_student.html',{
        'student':student,
        'academic_year':academic_year
    })
    
def show_subject(request, id):
    subject = Subject.objects.get(pk=id)
    teachers = subject.sub_teachers
    
    return render(request,'students/subject.html',{
        'student':subject,
        'teachers':teachers
    })

def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student_number = form.cleaned_data['student_number']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_field_of_study = form.cleaned_data['field_of_study']
            new_academic_year_id = form.cleaned_data['academic_year_id']
            new_gpa = form.cleaned_data['gpa']
            
            new_student = Student(
                student_number = new_student_number,
                first_name = new_first_name,
                last_name = new_last_name,
                email = new_email,
                field_of_study = new_field_of_study,
                academic_year_id = new_academic_year_id,
                gpa = new_gpa
            )
            new_student.save()
            return render(request, 'students/add.html',{
                'form' : StudentForm(),
                'success' : True
            })
    else:
        form = StudentForm()
    return render(request, 'students/add.html',{
        'form' : StudentForm()
    })

def edit(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'students/edit.html', {
                'form': form,
                'success': True
            })
    else:
        student = Student.objects.get(pk=id)
        form = StudentForm(instance=student)
    return render(request, 'students/edit.html', {
        'form': form
    })
    
def edit_year(request, id):
    if request.method == 'POST':
        year = AcademicYear.objects.get(pk=id)
        form = AcademicYearForm(request.POST, instance=year)
        if form.is_valid():
            form.save()
            return render(request, 'students/edit_year.html', {
                'form': form,
                'success': True
            })
    else:
        year = AcademicYear.objects.get(pk=id)
        form = AcademicYearForm(instance=year)
    return render(request, 'students/edit_year.html', {
        'form': form
    })
    
def delete(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))
