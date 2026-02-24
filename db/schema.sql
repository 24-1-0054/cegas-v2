CREATE DATABASE IF NOT EXISTS cegas; USE cegas;

CREATE TABLE section (
  PRIMARY KEY(section_id), 
  max_capacity int
);

CREATE TABLE enrollment (
  PRIMARY KEY enrollment_id int, 
  year_enrolled int,
  grade_level int 
);

CREATE TABLE student (
  PRIMARY KEY(student_id),
  FOREIGN KEY(enrollment_id) REFERENCES enrollment(enrollment_id),
  FOREIGN KEY(section_id) REFERENCES section(section_id),
  given_name varchar(128) NOT NULL,
  surname varchar(128) NOT NULL,
  student_email varchar(128)
);

CREATE TABLE teacher (
  PRIMARY KEY(teacher_id),
  given_name varchar(128) NOT NULL, 
  surname varchar(128) NOT NULL,
  email varchar(128),
  phone_number int
);

CREATE TABLE course (
  PRIMARY KEY(course_id),
  FOREIGN KEY(teacher_id) REFERENCES teacher(teacher_id), 
  FOREIGN KEY(section_id) REFERENCES section(section_id),
  course varchar(128)
);

CREATE TABLE assessment (
  PRIMARY KEY(assessment_id),
  assessment_title varchar(128),
  FOREIGN KEY(course_id) REFERENCES course(course_id),
  weighted_percent int,
  max_score int
);

CREATE TABLE score (
  PRIMARY KEY(score_id),
  FOREIGN KEY(student_id) REFERENCES student(student_id), 
  FOREIGN KEY (assessment_id) REFERENCES assessment(assessment_id),
  score float
);