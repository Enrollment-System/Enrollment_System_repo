# Enrollment_System_repo
## Table of Contents
- Prerequisites
- Installation
- Run the application
- View the application

### Project Overview
- Student Management system that allows for creating reading updating and deleting students 
information this core functionality is known by the acronym crude create read update delete.
- This is the application we are going to build on the home page we have a list of students 
presented in a table for each student we have available three action buttons that 
allow us to view edit and delete students from a database.

- If we press the first button with the information icon you can view the 
information of a selected student we use here a bootstrap model to present the data to the 
user. 

- If we press the second button with the edit icon we can edit the information of a selected 
student.

- If we press the third button with the delete icon we can delete a selected student from 
a database before deleting a student we are first presented with a bootstrap model that asks 
us to confirm the deletion we can also add a new student when adding a new student we need 
to provide the student number a first and last name and email a field of study and a gpa.

- We also have subjects for each students actually six subjects assigned for each academic year 
and each subject has an instructor. 

- We can also add new subjects and instructors for these 
subjects.

### Installation

1. Create a virtual environment
From the root directory run:

``` python -m venv venv ````
2. Activate the virtual environment
From the root directory run:

On macOS:

``` source venv/bin/activate ```
On Windows:

```venv\scripts\activate```
3. Install required dependencies
From the root directory run:

```pip install -r requirements.txt```
4. Run migrations
From the root directory run:

```python manage.py makemigrations```
```python manage.py migrate```
5. Create an admin user to access the Django Admin interface
From the root directory run:

```python manage.py createsuperuser```
When prompted, enter a username, email, and password.

### Run the application
From the root directory run:

```python manage.py runserver```

### View the application
Go to http://127.0.0.1:8000/ to view the application.
