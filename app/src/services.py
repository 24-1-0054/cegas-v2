import csv, os
from dataclasses import dataclass
from cache import cache_instance as ci
import io_csv
from logger import logger

def full_name(student_id: int, reverse=True):
    """Gets the full name of a student from a `student_id`."""
    student = None
    for s in ci.get("student"):
        if s[0] == student_id: student = s
        
    if not student: return "[NAME ERROR]" # Student not found

    if reverse: 
        return f'{student[4]}, {student[3]}' # "<surname>, <given_name>"
    else: 
        return f'{student[3]} {student[4]}' # "<given_name> <surname>

def create_row(table_name: str, row):
    """Saves row data in cache its respective .csv file."""
    io_csv.create_row(table_name, row)
    ci.run(table_name, "append", *row)
    logger.log(f"New tuple added to table {table_name}: {str(row)}")

def edit_row(table_name: str, row_PK, index, new_row: tuple):
    """Changes row data in cache and respective .csv file"""
    io_csv.edit_row(table_name, str(row_PK), new_row)
    ci.cache[table_name][index] = new_row
    logger.log(
        f"Row of table {table_name} at index {index} edited to {str(new_row)}"
    )
    
# shorthands for pearson requirements
def create_student(*student_data):
    """`create_row()` shorthand for table `student`"""
    create_row("student", student_data)

def record_score(*score_data):
    """`create_row()` shorthand for table `score`"""
    create_row("score", score_data)

def enroll_student(student_id: int, enrollment):
    """`create_row()` shorthand for table `enrollment`\n
    also edits `student` table and changes enrollment data"""
    create_row("enrollment", enrollment)

    student_ids = [x[0] for x in ci.get("student")]
    index = student_ids.index(student_id)
    
    print(ci.get("student")[index])
    
    student_cp = ci.get("student")[index]
    # skip if student enrollment_id matches
    if student_cp[1] == enrollment[0]:
        return

    student_cp = list(student_cp)
    student_cp[1] = enrollment[0]
    edit_row("student", student_id, index, student_cp)

# Reports dataclass, which sets report-type macros for code readability.
@dataclass
class Reports:
    LIST_STUDENTS = '1'

def get_report(report):
    """Prints a string of the selected report."""
    if report == Reports.LIST_STUDENTS:
        print("-- FULL STUDENTS LIST --")
        print(*ci.get("student"), sep='\n')
        print("ORDER: student_id, enrollment_id, section_id, "
                "given_name, surname, student_email")
    else:
        print("Report type not found. Try again!")