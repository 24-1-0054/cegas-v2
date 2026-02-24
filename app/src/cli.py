import services
from ranking import *

from cache import cache_instance as ci
from logger import logger
import traceback

from cli_helpers import *

def run_cli():
    """Functions as `main()`"""
    print("The Campus Enrollment & Grade Analytics System (CEGAS) Terminal")
    while True:
        selection = input(
            "Functions:\n"
            "(1) Create student\n"
            "(2) Enroll student\n"
            "(3) Record score\n"
            "(4) List reports\n"
            "(5) Rank top-N by average%\n"
            "(0) Exit\n"
            "Selection: "
        ).strip() 
        
        if selection == '1':
            # AUTO_INCREMENT IMPLEMENTATION
            student_id = int(ci.get("student")[-1][0]) + 1 
            enrollment_id = None
            
            try:
                section_id = attr_input(
                    "section ID", "section", datatype=int, 
                    fk_ref=ci.get("section")
                )
                
                given_name = attr_input("given name", "student")
                surname = attr_input("surname", "student")
                student_email = attr_input(
                    "school email", "student", nullable=True
                )

                if student_email and not is_email_format(student_email):
                    raise ValueError("Invalid email format: " + student_email)

                services.create_student(
                    student_id, enrollment_id, section_id, given_name, 
                    surname, student_email
                )
            except ValueError as e: input_err(e)

            logger.log("[INFO] User executed command #1")
            
        elif selection == '2':
            # AUTO_INCREMENT IMPLEMENTATION
            enrollment_id = int(ci.get("enrollment")[-1][0]) + 1 
            try:
                year_enrolled = attr_input("year", "enrollment", datatype=int)

                grade_level = attr_input(
                    "", "", prompt= "For what grade level is the enrollment? ",
                    datatype=int
                )

                student_id = attr_input("student_id", "enrollee", datatype=int)

                if not enrollment_id or not year_enrolled \
                    or not grade_level or not student_id:
                    raise ValueError("Attribute set as NOT NULL is NULL.")
                
                services.enroll_student(
                    student_id, 
                    (enrollment_id, year_enrolled,  grade_level)
                )
            except ValueError as e: input_err(e)

            logger.log("[INFO] User executed command #2")

        elif selection == '3':
            score_id = int(ci.get("score")[-1][0]) + 1 # AUTO_INCREMENT IMPLEMENTATION
            try: 
                student_id = attr_input(
                    "student ID", "score", datatype=int,
                    fk_ref=ci.get("student")
                
                )
                assessment_id = attr_input(
                    "assessment ID", "score", datatype=int,
                    fk_ref=ci.get("assessment")
                
                )
                score = attr_input("numerical score", "score", datatype=float)

                services.record_score(
                    score_id, 
                    student_id, 
                    assessment_id, 
                    score
                )

            except ValueError as e: input_err(e)

            logger.log("[INFO] User executed command #3")

        elif selection == '4':
            report = input("COMMANDS\n"
                           "(1) List students\n"
                           "Selection: ").strip()
            
            services.get_report(report)

            logger.log("[INFO] User executed command #4.")
        elif selection == '5':
            try:
                n = int(input("How many students would you like to display? "))
            except ValueError as e:
                logger.tee("ValueError: ", e)
                logger.log(traceback.format_exc())
                continue

            if "averages_desc" not in ci:
                update_ranking_cache()
                ci.new_sorted("averages_desc", get_student_avgs(), 1, 
                              reverse=True)
            
            for i, student in enumerate(ci.get("averages_desc")):
                if i >= n: break
                
                print(f'#{i + 1} {services.full_name(student[0])} - {student[1]}% ')

            logger.log("[INFO] User executed command #5.")

        elif selection == '0':
            logger.close()
            break
            
        else:
            print("Invalid input.")

if __name__ == "__main__":
    run_cli()