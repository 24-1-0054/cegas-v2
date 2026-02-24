# merged with `weights_demo.py` 

from statistics import fmean
from cache import cache_instance as ci

def update_ranking_cache():
    """`ranking.py` is heavily dependent upon the cache. It computes many
    things not found in other files. Ranking does not work if not initialized"""

    scores = ci.get("score")
    assessments = ci.get("assessment")

    ci.set("assessment_info", { a[0]: (a[4], a[2]) for a in assessments })
    ci.set("percents", score_percents(scores))
    ci.set("grades_weighed", weigh_all_by_course(assessments))
    ci.set("student_avgs", get_student_avgs())

def score_percents(scores: tuple):
    """for neatnessGets percentages of all scores.\n
    Returns: [(student_id, assessment_id, percent, course_id)]"""

    output = []

    for _, student_id, assessment_id, score in scores:
        percent = (score/ci.get("assessment_info")[assessment_id][0])
        output.append((student_id, assessment_id,
                        percent, ci.get("assessment_info")[assessment_id][1]))

    return output

def weigh_all_by_course(assessments):
    """Weigh all students' grades out of 100%.\n
    Returns: { (student_id, course): [weighted_grade, total_scores] }"""

    # { assessment_id: weighted_score }
    weights = { a[0] : a[3] for a in assessments } 
    grades = {} 
    
    for student_id, assessment_id, percent, course_id in ci.get("percents"):
        score = round(percent * weights[assessment_id]/100, 3) * 100
        if score > 100: # score cannot be higher than 100
            score = 100

        if (student_id, course_id) not in grades: 
            grades[(student_id, course_id)] = [score, 1] 
        else:
            grades[(student_id, course_id)][0] += score
            grades[(student_id, course_id)][1] += 1

    return grades

def get_student_avgs():
    """Get average%s of student overall.\n
    Returns: (student_id, average%)"""
    student_grades = {} # {student_id: [grades] }

    for subject, grade in ci.get("grades_weighed").items():
        # initialize lists
        if subject[0] not in student_grades:
            student_grades[subject[0]] = []

        student_grades[subject[0]].append(grade[0])

    return [(student_id, round(fmean(grades), 3)) 
            for student_id, grades in student_grades.items()]