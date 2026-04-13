"""
===============================================================
   EdTech Learning Platform - Sample Application Code
===============================================================

WHAT IS THIS FILE?
  This is the SAMPLE CODE that our CI/CD pipeline will:
    1. BUILD (check it exists and is valid Python)
    2. TEST  (run tests on its functions)
    3. ANALYZE (the AI analyzer will check this file for issues)
    4. DEPLOY (simulate pushing this to a server)

  It represents a simple EdTech (Educational Technology) app
  with features like student management, course enrollment,
  quiz scoring, and grade calculations.

  NOTE: Some functions below are intentionally imperfect so
  that the AI Analyzer has something to detect and report!
"""

# STUDENT MANAGEMENT

class Student:
    """
    Represents a student in the EdTech platform.
    Stores student details and their enrolled courses.
    """

    def __init__(self, student_id, name, email):
        """
        Creates a new Student object.

        Parameters:
            student_id : A unique number to identify the student
            name       : Full name of the student
            email      : Student's email address
        """
        self.student_id = student_id
        self.name = name
        self.email = email
        self.enrolled_courses = []   # List of courses this student is enrolled in
        self.quiz_scores = {}        # Dictionary: {course_name: [score1, score2, ...]}

    def enroll_in_course(self, course_name):
        """
        Enrolls the student in a course.
        Prevents duplicate enrollments.
        """
        if course_name not in self.enrolled_courses:
            self.enrolled_courses.append(course_name)
            self.quiz_scores[course_name] = []   # Start with empty scores
            return True   # Enrollment was successful
        else:
            return False  # Already enrolled

    def get_enrolled_courses(self):
        """Returns the list of courses the student is enrolled in."""
        return self.enrolled_courses



# QUIZ & SCORE MANAGEMENT


def add_quiz_score(student, course_name, score):
    """
    Adds a quiz score for a student in a specific course.

    Parameters:
        student     : A Student object
        course_name : Name of the course the quiz belongs to
        score       : The quiz score (should be between 0 and 100)

    Returns:
        True if score was added successfully, False otherwise.
    """

    # Validate: score must be between 0 and 100
    if score < 0 or score > 100:
        print(f"  [ERROR] Invalid score: {score}. Score must be between 0 and 100.")
        return False

    # Validate: student must be enrolled in the course
    if course_name not in student.quiz_scores:
        print(f"  [ERROR] Student not enrolled in '{course_name}'.")
        return False

    # Add the score
    student.quiz_scores[course_name].append(score)
    return True


def calculate_average_score(scores):
    """
    Calculates the average (mean) of a list of scores.

    Parameters:
        scores : A list of numbers (quiz scores)

    Returns:
        The average score, or 0 if the list is empty.
    """

    # Handle the case where there are no scores yet
    if len(scores) == 0:
        return 0

    # Sum all scores and divide by count
    total = sum(scores)
    average = total / len(scores)

    # Round to 2 decimal places for clean output
    return round(average, 2)


def get_grade_from_score(average_score):
    """
    Converts a numeric average into a letter grade.

    Grading scale:
        90-100 → A (Excellent)
        80-89  → B (Good)
        70-79  → C (Average)
        60-69  → D (Below Average)
        0-59   → F (Fail)

    Parameters:
        average_score : A number between 0 and 100

    Returns:
        A letter grade as a string ('A', 'B', 'C', 'D', or 'F')
    """

    if average_score >= 90:
        return 'A'
    elif average_score >= 80:
        return 'B'
    elif average_score >= 70:
        return 'C'
    elif average_score >= 60:
        return 'D'
    else:
        return 'F'


# ---------------------------------------------------------------
# REPORT GENERATION
# ---------------------------------------------------------------

def generate_student_report(student):
    """
    Generates a readable report for a student showing:
      - Their enrolled courses
      - Their quiz scores per course
      - Their average score and letter grade per course

    Parameters:
        student : A Student object

    Returns:
        A formatted string report.
    """

    # Build the report as a list of lines, then join at the end
    report_lines = []
    report_lines.append(f"Student Report: {student.name} (ID: {student.student_id})")
    report_lines.append(f"Email: {student.email}")
    report_lines.append("-" * 40)

    # If student hasn't enrolled in anything
    if not student.enrolled_courses:
        report_lines.append("No courses enrolled.")
        return '\n'.join(report_lines)

    # Show details for each course
    for course in student.enrolled_courses:
        scores = student.quiz_scores.get(course, [])
        average = calculate_average_score(scores)
        grade = get_grade_from_score(average)

        report_lines.append(f"Course: {course}")
        report_lines.append(f"  Scores: {scores}")
        report_lines.append(f"  Average: {average} | Grade: {grade}")
        report_lines.append("")  # Blank line between courses

    return '\n'.join(report_lines)


# ---------------------------------------------------------------
# COURSE SEARCH
# ---------------------------------------------------------------

def search_courses(all_courses, keyword):
    """
    Searches through a list of course names for a keyword.
    The search is case-insensitive.

    Parameters:
        all_courses : A list of course name strings
        keyword     : The word to search for

    Returns:
        A list of matching course names.
    """

    keyword_lower = keyword.lower()
    matching_courses = []

    for course in all_courses:
        if keyword_lower in course.lower():
            matching_courses.append(course)

    return matching_courses


# ---------------------------------------------------------------
# INTENTIONALLY IMPERFECT FUNCTION (for AI analyzer to detect)
# ---------------------------------------------------------------

# TODO: This function needs to be refactored before production release
def process_batch_enrollment(students_data):
    # This function has NO docstring — the AI analyzer will flag this!
    # It also has a long line below which the analyzer will catch.
    results = []
    for d in students_data:  # 'd' is a short variable name — analyzer will flag this!
        s = Student(d['id'], d['name'], d['email'])  # 's' is also short!
        for course in d.get('courses', []):
            s.enroll_in_course(course)
        results.append(s)
    return results


# ---------------------------------------------------------------
# DEMONSTRATION: Run this file directly to see it in action
# ---------------------------------------------------------------

if __name__ == "__main__":
    """
    This block only runs when you do: python edtech_app.py
    It demonstrates the features of the EdTech app.
    """

    print("=== EdTech Platform Demo ===\n")

    # Create a student
    student1 = Student(101, "Anjali Kumar", "anjali@edtech.com")

    # Enroll in courses
    student1.enroll_in_course("Python Programming")
    student1.enroll_in_course("Web Development")

    # Add quiz scores
    add_quiz_score(student1, "Python Programming", 85)
    add_quiz_score(student1, "Python Programming", 92)
    add_quiz_score(student1, "Python Programming", 78)

    add_quiz_score(student1, "Web Development", 70)
    add_quiz_score(student1, "Web Development", 88)

    # Generate and print the report
    report = generate_student_report(student1)
    print(report)

    # Search example
    course_catalog = [
        "Python Programming", "Web Development", "Data Science Basics",
        "Machine Learning Intro", "Python for Data Analysis"
    ]
    results = search_courses(course_catalog, "python")
    print(f"Courses matching 'python': {results}")
