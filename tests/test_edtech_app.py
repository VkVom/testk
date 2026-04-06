"""
===============================================================
   TEST FILE: Tests for EdTech Application
===============================================================

WHAT IS THIS FILE?
  This file contains all the AUTOMATED TESTS for edtech_app.py.
  The CI/CD pipeline runs these tests automatically during Stage 2.

HOW DOES TESTING WORK?
  Python's 'unittest' framework works like this:
    - Create a class that inherits from unittest.TestCase
    - Write methods that start with 'test_'
    - Inside each method, use 'assert' statements to check results
    - If an assertion fails, the test fails!

TYPES OF ASSERTIONS USED:
  self.assertEqual(a, b)    → Check that a == b
  self.assertTrue(x)        → Check that x is True
  self.assertFalse(x)       → Check that x is False
  self.assertIn(a, b)       → Check that a is inside b

HOW TO RUN JUST THE TESTS (without full pipeline):
  python -m pytest tests/        (if pytest is installed)
  python -m unittest discover tests/   (using built-in unittest)
"""

# We import 'unittest' to use the testing framework
import unittest

# We import 'sys' and 'os' to make sure Python can find our app
import sys
import os

# Add the parent folder to Python's search path
# This lets us import from 'sample_code/edtech_app.py'
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Now import the functions and classes we want to test
from sample_code.edtech_app import (
    Student,
    add_quiz_score,
    calculate_average_score,
    get_grade_from_score,
    generate_student_report,
    search_courses,
)


# ---------------------------------------------------------------
# TEST CLASS 1: Testing the Student class
# ---------------------------------------------------------------

class TestStudent(unittest.TestCase):
    """
    Tests for the Student class — creating students and enrolling them.
    """

    def setUp(self):
        """
        setUp() runs BEFORE each test automatically.
        We create a fresh Student object so each test starts clean.
        """
        self.student = Student(1, "Test Student", "test@example.com")

    def test_student_created_correctly(self):
        """Test that a student is created with the correct details."""
        self.assertEqual(self.student.student_id, 1)
        self.assertEqual(self.student.name, "Test Student")
        self.assertEqual(self.student.email, "test@example.com")

    def test_student_starts_with_no_courses(self):
        """A new student should have an empty course list."""
        self.assertEqual(len(self.student.enrolled_courses), 0)

    def test_enroll_in_course(self):
        """Test that a student can enroll in a course successfully."""
        result = self.student.enroll_in_course("Python Programming")
        self.assertTrue(result)   # Should return True (success)
        self.assertIn("Python Programming", self.student.enrolled_courses)

    def test_cannot_enroll_twice(self):
        """Test that a student cannot enroll in the same course twice."""
        self.student.enroll_in_course("Python Programming")
        result = self.student.enroll_in_course("Python Programming")  # Second time
        self.assertFalse(result)  # Should return False (already enrolled)

        # Should still only appear once in the list
        count = self.student.enrolled_courses.count("Python Programming")
        self.assertEqual(count, 1)

    def test_enroll_multiple_courses(self):
        """Test that a student can enroll in multiple different courses."""
        self.student.enroll_in_course("Math")
        self.student.enroll_in_course("Science")
        self.student.enroll_in_course("English")
        self.assertEqual(len(self.student.enrolled_courses), 3)

    def test_get_enrolled_courses(self):
        """Test that get_enrolled_courses() returns the correct list."""
        self.student.enroll_in_course("Art")
        courses = self.student.get_enrolled_courses()
        self.assertIn("Art", courses)


# ---------------------------------------------------------------
# TEST CLASS 2: Testing quiz score functions
# ---------------------------------------------------------------

class TestQuizScores(unittest.TestCase):
    """
    Tests for adding scores and calculating averages.
    """

    def setUp(self):
        """Create a student and enroll them in one course before each test."""
        self.student = Student(2, "Quiz Tester", "quiz@example.com")
        self.student.enroll_in_course("Mathematics")

    def test_add_valid_score(self):
        """Test that a valid score (0-100) can be added."""
        result = add_quiz_score(self.student, "Mathematics", 85)
        self.assertTrue(result)
        self.assertIn(85, self.student.quiz_scores["Mathematics"])

    def test_add_score_of_zero(self):
        """Score of 0 is valid (student got everything wrong)."""
        result = add_quiz_score(self.student, "Mathematics", 0)
        self.assertTrue(result)

    def test_add_score_of_hundred(self):
        """Score of 100 is valid (perfect score)."""
        result = add_quiz_score(self.student, "Mathematics", 100)
        self.assertTrue(result)

    def test_reject_score_above_100(self):
        """Score above 100 is invalid and should be rejected."""
        result = add_quiz_score(self.student, "Mathematics", 105)
        self.assertFalse(result)   # Should return False

    def test_reject_negative_score(self):
        """Negative scores are invalid and should be rejected."""
        result = add_quiz_score(self.student, "Mathematics", -5)
        self.assertFalse(result)

    def test_reject_score_for_unenrolled_course(self):
        """Can't add a score for a course the student isn't enrolled in."""
        result = add_quiz_score(self.student, "History", 80)  # Not enrolled in History
        self.assertFalse(result)


# ---------------------------------------------------------------
# TEST CLASS 3: Testing calculate_average_score
# ---------------------------------------------------------------

class TestCalculateAverage(unittest.TestCase):
    """Tests for the average score calculation function."""

    def test_average_of_normal_scores(self):
        """Test average of a typical set of scores."""
        scores = [80, 90, 70]
        result = calculate_average_score(scores)
        self.assertEqual(result, 80.0)  # (80+90+70) / 3 = 80

    def test_average_of_single_score(self):
        """Average of one score should be that score itself."""
        result = calculate_average_score([95])
        self.assertEqual(result, 95)

    def test_average_of_empty_list(self):
        """Average of empty list should be 0 (no scores yet)."""
        result = calculate_average_score([])
        self.assertEqual(result, 0)

    def test_average_is_rounded(self):
        """Average should be rounded to 2 decimal places."""
        scores = [100, 100, 99]   # Average = 99.666...
        result = calculate_average_score(scores)
        self.assertEqual(result, 99.67)  # Rounded to 2 decimal places

    def test_average_of_zeros(self):
        """All zeros should give average of 0."""
        result = calculate_average_score([0, 0, 0])
        self.assertEqual(result, 0)


# ---------------------------------------------------------------
# TEST CLASS 4: Testing get_grade_from_score
# ---------------------------------------------------------------

class TestGrading(unittest.TestCase):
    """Tests for the letter grade assignment function."""

    def test_grade_A(self):
        """Scores 90 and above should give grade A."""
        self.assertEqual(get_grade_from_score(90), 'A')
        self.assertEqual(get_grade_from_score(100), 'A')
        self.assertEqual(get_grade_from_score(95), 'A')

    def test_grade_B(self):
        """Scores 80-89 should give grade B."""
        self.assertEqual(get_grade_from_score(80), 'B')
        self.assertEqual(get_grade_from_score(89), 'B')

    def test_grade_C(self):
        """Scores 70-79 should give grade C."""
        self.assertEqual(get_grade_from_score(70), 'C')
        self.assertEqual(get_grade_from_score(79), 'C')

    def test_grade_D(self):
        """Scores 60-69 should give grade D."""
        self.assertEqual(get_grade_from_score(60), 'D')
        self.assertEqual(get_grade_from_score(69), 'D')

    def test_grade_F(self):
        """Scores below 60 should give grade F (fail)."""
        self.assertEqual(get_grade_from_score(59), 'F')
        self.assertEqual(get_grade_from_score(0), 'F')
        self.assertEqual(get_grade_from_score(30), 'F')


# ---------------------------------------------------------------
# TEST CLASS 5: Testing course search
# ---------------------------------------------------------------

class TestCourseSearch(unittest.TestCase):
    """Tests for the course search function."""

    def setUp(self):
        """Set up a sample course catalog to use in all tests."""
        self.catalog = [
            "Python Programming",
            "Web Development",
            "Data Science Basics",
            "Machine Learning Intro",
            "Python for Data Analysis",
        ]

    def test_search_finds_matching_courses(self):
        """Search for 'python' should return 2 results."""
        results = search_courses(self.catalog, "python")
        self.assertEqual(len(results), 2)

    def test_search_is_case_insensitive(self):
        """Searching 'PYTHON' and 'python' should give same results."""
        results_lower = search_courses(self.catalog, "python")
        results_upper = search_courses(self.catalog, "PYTHON")
        self.assertEqual(results_lower, results_upper)

    def test_search_no_results(self):
        """Searching for something not in the catalog should return empty list."""
        results = search_courses(self.catalog, "blockchain")
        self.assertEqual(results, [])

    def test_search_partial_keyword(self):
        """Searching 'data' should match courses with 'data' in the name."""
        results = search_courses(self.catalog, "data")
        self.assertEqual(len(results), 2)  # "Data Science Basics" and "Python for Data Analysis"


# ---------------------------------------------------------------
# TEST CLASS 6: Testing generate_student_report
# ---------------------------------------------------------------

class TestStudentReport(unittest.TestCase):
    """Tests for the student report generation function."""

    def test_report_contains_student_name(self):
        """The report should include the student's name."""
        student = Student(3, "Priya Sharma", "priya@example.com")
        report = generate_student_report(student)
        self.assertIn("Priya Sharma", report)

    def test_report_shows_no_courses_message(self):
        """Report for a student with no courses should say so."""
        student = Student(4, "No Course Student", "none@example.com")
        report = generate_student_report(student)
        self.assertIn("No courses enrolled", report)

    def test_report_shows_enrolled_course(self):
        """Report should show the course name and scores."""
        student = Student(5, "Course Taker", "course@example.com")
        student.enroll_in_course("Biology")
        add_quiz_score(student, "Biology", 88)
        report = generate_student_report(student)
        self.assertIn("Biology", report)
        self.assertIn("88", report)


# ---------------------------------------------------------------
# RUN TESTS DIRECTLY
# ---------------------------------------------------------------

if __name__ == "__main__":
    """
    If you run this file directly (python tests/test_edtech_app.py),
    it will run all the tests and show results.
    """
    unittest.main(verbosity=2)
