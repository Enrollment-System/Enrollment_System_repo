from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse 

from .models import Student, AcademicYear, Subject,Teacher
from .forms import StudentForm,AcademicYearForm,SubjectForm,TeacherForm

from django.db.models import Q
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
    
def all_teachers(request):
    return render(request, 'students/all_teachers.html', {
        'teachers': Teacher.objects.all(),
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
    teacher = subject.sub_teacher
    
    return render(request,'students/subject.html',{
        'subject':subject,
        'teacher':teacher
    })
    
def show_teacher(request, id):
    teacher = Teacher.objects.get(pk=id)
    
    return render(request,'students/teacher.html',{
        'teacher':teacher,
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
    
def add_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            new_sub_code = form.cleaned_data['sub_code']
            new_sub_name = form.cleaned_data['sub_name']
            new_sub_grade = form.cleaned_data['sub_grade']
            new_sub_description = form.cleaned_data['sub_description']
            new_sub_reference = form.cleaned_data['sub_reference']
            new_sub_teacher = form.cleaned_data['sub_teacher']
            
            new_subject = Subject(
                sub_code = new_sub_code,
                sub_name = new_sub_name,
                sub_grade = new_sub_grade,
                sub_description = new_sub_description,
                sub_reference = new_sub_reference,
                sub_teacher = new_sub_teacher,

            )
            new_subject.save()
            return render(request, 'students/add_subject.html',{
                'form' : SubjectForm(),
                'success' : True
            })
    else:
        form = SubjectForm()
    return render(request, 'students/add_subject.html',{
        'form' : SubjectForm()
    })
    
def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            new_tech_first_name = form.cleaned_data['tech_first_name']
            new_tech_last_name = form.cleaned_data['tech_last_name']
            new_tech_email = form.cleaned_data['tech_email']
            new_tech_department = form.cleaned_data['tech_department']
            new_tec_dob = form.cleaned_data['tec_dob']
            
            new_teacher = Teacher(
                tech_first_name = new_tech_first_name,
                tech_last_name = new_tech_last_name,
                tech_email = new_tech_email,
                tech_department = new_tech_department,
                tec_dob = new_tec_dob,

            )
            new_teacher.save()
            return render(request, 'students/add_teacher.html',{
                'form' : TeacherForm(),
                'success' : True
            })
    else:
        form = TeacherForm()
    return render(request, 'students/add_teacher.html',{
        'form' : TeacherForm()
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
    
def edit_subject(request, id):
    if request.method == 'POST':
        subject = Subject.objects.get(pk=id)
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return render(request, 'students/edit_subject.html', {
                'form': form,
                'success': True
            })
    else:
        subject = Subject.objects.get(pk=id)
        form = SubjectForm(instance=subject)
    return render(request, 'students/edit_subject.html', {
        'form': form
    })

def edit_teacher(request, id):
    if request.method == 'POST':
        teacher = Teacher.objects.get(pk=id)
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return render(request, 'students/edit_teacher.html', {
                'form': form,
                'success': True
            })
    else:
        teacher = Teacher.objects.get(pk=id)
        form = TeacherForm(instance=teacher)
    return render(request, 'students/edit_teacher.html', {
        'form': form
    })
    
def delete(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))

def delete_subject(request, id):
    if request.method == 'POST':
        subject = Subject.objects.get(pk=id)
        subject.delete()
    return HttpResponseRedirect(reverse('all_subjects'))

def delete_teacher(request, id):
    if request.method == 'POST':
        teacher = Teacher.objects.get(pk=id)
        teacher.delete()
    return HttpResponseRedirect(reverse('all_teachers'))


def search_students(request):
    if request.method == 'POST':
        searched=request.POST['searched']
        results=Student.objects.filter(Q(first_name__contains=searched) | Q(last_name__contains=searched))
    return render(request,'students/index.html',{
        'students':results,
        'searched':searched
    })
    
def search_subjects(request):
    if request.method == 'POST':
        searched=request.POST['searched']
        results=Subject.objects.filter(Q(sub_name__contains=searched) | Q(sub_code__contains=searched))
    return render(request,'students/all_subjects.html',{
        'subjects':results,
        'searched':searched
    })

def search_teacher(request):
    if request.method == 'POST':
        searched=request.POST['searched']
        results=Teacher.objects.filter(Q(tech_first_name__contains=searched) | Q(tech_last_name__contains=searched))
    return render(request,'students/all_teachers.html',{
        'teachers':results,
        'searched':searched
    })