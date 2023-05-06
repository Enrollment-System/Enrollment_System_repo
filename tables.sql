CREATE TABLE AcademicYear (
  id INTEGER PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  subject1 VARCHAR(255),
  subject2 VARCHAR(255),
  subject3 VARCHAR(255),
  subject4 VARCHAR(255),
  subject5 VARCHAR(255),
  subject6 VARCHAR(255)
);

CREATE TABLE Department (
  id INTEGER PRIMARY KEY,
  dep_name VARCHAR(50) NOT NULL,
  dep_n VARCHAR(50) NOT NULL
);

CREATE TABLE Student (
  id INTEGER PRIMARY KEY,
  student_number INTEGER NOT NULL,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) NOT NULL,
  department_id INTEGER,
  academic_year_id INTEGER,
  gpa FLOAT NOT NULL,
  FOREIGN KEY (department_id) REFERENCES Department(id),
  FOREIGN KEY (academic_year_id) REFERENCES AcademicYear(id)
);

CREATE TABLE Teacher (
  id INTEGER PRIMARY KEY,
  tech_first_name VARCHAR(50) NOT NULL,
  tech_last_name VARCHAR(50) NOT NULL,
  tech_email VARCHAR(50) NOT NULL,
  tech_department_id INTEGER,
  tec_dob DATE NOT NULL,
  FOREIGN KEY (tech_department_id) REFERENCES Department(id)
);

CREATE TABLE Subject (
  id INTEGER PRIMARY KEY,
  sub_code VARCHAR(50) NOT NULL,
  sub_name VARCHAR(50) NOT NULL,
  sub_grade_id INTEGER,
  sub_description TEXT NOT NULL,
  sub_reference VARCHAR(100) NOT NULL,
  sub_teacher_id INTEGER,
  FOREIGN KEY (sub_grade_id) REFERENCES AcademicYear(id),
  FOREIGN KEY (sub_teacher_id) REFERENCES Teacher(id)
);
