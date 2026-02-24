# For recording purposes only. Do not grade. 
# Do not consider as a part of the CEGAS.

import random, os

this = os.path.dirname(__file__)
cwd = os.path.abspath(this)
os.chdir(cwd)

first_names = [
    "James", "Mary", "Robert", "Patricia", "John", "Jennifer", "Michael", "Linda", "David", "Elizabeth",
    "William", "Barbara", "Richard", "Susan", "Joseph", "Jessica", "Thomas", "Sarah", "Charles", "Karen",
    "Christopher", "Nancy", "Daniel", "Margaret", "Matthew", "Lisa", "Anthony", "Betty", "Donald", "Dorothy",
    "Mark", "Sandra", "Paul", "Ashley", "Steven", "Kimberly", "Andrew", "Donna", "Kevin", "Carol",
    "Kenneth", "Michelle", "George", "Emily", "Joshua", "Amanda", "Timothy", "Helen", "Ryan", "Melissa",
    "Jason", "Deborah", "Jeffrey", "Laura", "Gary", "Stephanie", "Eric", "Cynthia", "Jacob", "Rebecca",
    "Nicholas", "Sharon", "Jonathan", "Kathleen", "Stephen", "Amy", "Larry", "Shirley", "Scott", "Anna",
    "Frank", "Angela", "Justin", "Ruth", "Brandon", "Brenda", "Raymond", "Virginia", "Gregory", "Pamela",
    "Samuel", "Catherine", "Patrick", "Nicole", "Benjamin", "Christine", "Dennis", "Samantha", "Alexander", "Janet",
    "Jerry", "Debra", "Tyler", "Maria", "Aaron", "Diane", "Henry", "Kelly", "Douglas", "Frances"
]
surnames = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
    "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
    "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson",
    "Walker", "Hall", "Allen", "Young", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill",
    "Flores", "Green", "Adams", "Nelson", "Baker", "Gomez", "Campbell", "Parker", "Evans", "Edwards",
    "Carter", "Phillips", "Roberts", "Turner", "Morris", "Mitchell", "Russell", "Cook", "Rivera", "Bailey",
    "Bell", "Cooper", "Reed", "Kelly", "Howard", "Ward", "Cox", "Diaz", "Wood", "Price",
    "Foster", "Coleman", "Hayes", "Murphy", "Washington", "Simmons", "Bennett", "Gray", "James", "Myers",
    "Ryan", "Cruz", "Watson", "Brooks", "Sanders", "Bryant", "Henderson", "Guzman", "Dixon", "Carroll",
    "West", "Mendoza", "Ruiz", "Hughes", "Ferguson", "Rose", "Harrison", "Vasquez", "Chavez", "Lane"
]
courses = ["Math", "Science", "English", "Programming", "DBMS"]
assessments = [("Midterms Assessment", 40), ("Finals Assessment", 40), ("Assessment 1", 20)]

n_students = 30
n_teachers = 5
n_courses = len(courses)
n_sections = 2
n_enrollment = n_students
n_assessments = n_courses * len(assessments)

with open("seed.sql", "w") as f:
    lines = []

    # Table students
    lines.append("INSERT INTO student(student_id, enrollment_id, section_id, given_name, surname, student_email) VALUES\n")
    for i in range(n_students):
        lines.append(f'(1{i:06d}, 2{i:06d}, 3{random.randint(1, n_sections)}, "{random.choice(first_names)}", "{random.choice(surnames)}", "s1{i:06d}@example.edu")')
        lines.append(';\n\n') if i == n_students - 1 else lines.append(',\n')

    # Table teacher
    lines.append("INSERT INTO teacher(teacher_id, given_name, surname, email, phone_number) VALUES\n")
    for i in range(n_teachers):
        lines.append(f'(4{i:06d}, "{random.choice(first_names)}", "{random.choice(surnames)}", "t4{i:06d}_personal@example.com", 09{random.randint(100000000, 999999999)})')
        lines.append(';\n\n') if i == n_teachers - 1 else lines.append(',\n')

    # Table course
    lines.append("INSERT INTO course(course_id, teacher_id, section_id, title) VALUES\n")
    for i, v in enumerate(courses):
        lines.append(f'(5{i:06d}, 4{i:06d}, 3{random.randint(1, n_sections):06d}, "{v}")')
        lines.append(';\n\n') if i == len(courses) - 1 else lines.append(',\n')

    # Table section
    lines.append("INSERT INTO section(section_id, max_capacity) VALUES\n")
    for i in range(n_sections):
        lines.append(f"(3{i:06d}, {random.randint(6, 10) * 5})")
        lines.append(';\n\n') if i == n_sections - 1 else lines.append(',\n')

    # Table enrollment
    lines.append("INSERT INTO enrollment(enrollment_id, year_enrolled, grade_level) VALUES\n")
    for i in range(n_enrollment):
        lines.append(f'(2{i:06d}, 2025, 1)')
        lines.append(';\n\n') if i == n_enrollment - 1 else lines.append(',\n')
        
    # Table assessment
    lines.append("INSERT INTO assessment(assessment_id, assessment_title, course_id, weighted_percent, max_score) VALUES\n")
    max_assessment_id = 0
    for i in range(n_courses):
        for a in assessments:
            lines.append(f'(8{max_assessment_id:06d}, "{a[0]}", 5{i:06d}, {a[1]}, 100)')
            max_assessment_id = max_assessment_id + 1
            lines.append(';\n\n') if max_assessment_id == n_courses * len(assessments) else lines.append(',\n')
    
    # Table score
    lines.append("INSERT INTO score(score_id, student_id, assessment_id, score) VALUES\n")
    max_score_id = 0
    for i in range(n_students):
        for a in range(max_assessment_id):
            lines.append(f'(9{max_score_id:06d}, 1{i:06d}, 8{a:06d}, {random.randint(77, 100)}.0)')
            lines.append(';') if max_score_id == n_students * max_assessment_id - 1 else lines.append(',\n')
            max_score_id = max_score_id + 1
        
    f.writelines(lines)