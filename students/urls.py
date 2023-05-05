from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('academic_years', views.academic_years, name='academic_years'),
    path('all_subjects', views.all_subjects, name='all_subjects'),
    path('<int:id>', views.view_student, name='view_student'),
    path('add/', views.add, name = 'add'),
    path('add_subject/', views.add_subject, name = 'add_subject'),
    path('show_student/<int:id>/', views.show_student, name='show_student'),
    path('show_subject/<int:id>/', views.show_subject, name='show_subject'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('edit_year/<int:id>/', views.edit_year, name='edit_year'),
    path('edit_subject/<int:id>/', views.edit_subject, name='edit_subject'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('delete_subject/<int:id>/', views.delete_subject, name='delete_subject'),
    path('search_students/',views.search_students, name='search_students'),
    path('search_subjects/',views.search_subjects, name='search_subjects')
]