# Table Normalization Status Notes

## Table student
`student` attributes: 
- int: `student_id` (PK), `enrollment_id` (FK), `section_id` (FK)
- varchar: `given_name`, `surname`, `student_email`

- [x] 1NF: Attributes cannot take more than one value; atomic.
- [x] 2NF: The primary key is fully made up of only `student_id`; not a composite key.
- [x] 3NF: Non-key attributes, `given_name`, `surname`, and `student_email`, all depend on `student_id`.

## Table teacher
`teacher` attributes:
- int: `teacher_id` (PK), `phone_number`
- varchar: `given_name`, `surname`, `email`

- [x] 1NF: Attributes cannot take more than one value; atomic.
- [x] 2NF: The primary key is fully made up of only `teacher_id`; not a composite key.
- [x] 3NF: Non-key attributes, `given_name`, `surname`, `email`, and `phone_number`, all depend on `teacher_id`.

## Table course
`course` attributes: 
- int: `course_id` (PK), `teacher_id` (FK), `section_id` (FK)
- varchar: `title`

- [x] 1NF: Attributes cannot take more than one value; atomic.
- [x] 2NF: The primary key is fully made up of only `teacher_id`; not a composite key.
- [x] 3NF: The only non-key attribute, `title`, depends on `course_id`.

## Table section
`section` attributes: 
- int `section_id` (PK) and `max_capacity`

- [x] 1NF: Attributes cannot take more than one value; atomic.
- [x] 2NF: The primary key is fully made up of only `section_id`; not a composite key.
- [x] 3NF: The only non-key attribute `max_capacity` depends on `section_id`.

## Table enrollment
`enrollment` attributes:
- int: `enrollment_id` (PK), `year_enrolled`, `grade_level`

- [x] 1NF: Attributes cannot take more than one value; atomic.
- [x] 2NF: The primary key is fully made up of only `enrollment_id`; not a composite key.
- [x] 3NF: Non-key attributes, `year_enrolled` and `grade_level` depend on `section_id`.

## Table assessment
`assessment` attributes: 
- int: `assessment_id` (PK), `course_id` (FK), `weighted_percent`, `max_score`
- varchar: `assessment_title`

- [x] 1NF: Attributes cannot take more than one value; atomic.
- [x] 2NF: The primary key is fully made up of only `enrollment_id`; not a composite key.
- [x] 3NF: Non-key attributes, `weighted_percent`, `max_score`, and `assessment_title`, depend on `section_id`.

## Table score
`score` attributes:
- int: `score_id` (PK), `student_id` (FK), `assessment_id` (FK),
- float: `score`

- [x] 1NF: Attributes cannot take more than one value; atomic.
- [x] 2NF: The primary key is fully made up of only `enrollment_id`; not a composite key.
- [x] 3NF: The only non-key attribute `score` depends on `section_id`.