"""
===============================================================
   STAGE 2: TEST STAGE
===============================================================

WHAT IS THE TEST STAGE?
  Automatically runs all tests in the 'tests/' folder.
  If any test fails, the pipeline stops — broken code
  will NOT be deployed.

  Returns both pass/fail AND detailed results so the
  HTML report can show each individual test result.
"""

import unittest
import time
import io
import sys


def run_tests():
    """
    Runs all tests and returns:
      - passed (True/False)
      - details dict with counts and individual test names
    """

    print("  Loading tests from 'tests/' folder...")
    time.sleep(0.3)

    # Discover all test files
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir="tests", pattern="test_*.py")
    total = suite.countTestCases()
    print(f"  Found {total} test(s) to run.\n")
    time.sleep(0.3)

    # Use a custom result class to capture individual test names
    class DetailedResult(unittest.TextTestResult):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.passed_tests = []
            self.failed_tests = []

        def addSuccess(self, test):
            super().addSuccess(test)
            self.passed_tests.append(str(test.shortDescription() or test))

        def addFailure(self, test, err):
            super().addFailure(test, err)
            self.failed_tests.append(str(test.shortDescription() or test))

        def addError(self, test, err):
            super().addError(test, err)
            self.failed_tests.append(str(test.shortDescription() or test))

    # Run tests with our custom result class
    stream = io.StringIO()
    runner = unittest.TextTestRunner(
        verbosity=2,
        resultclass=DetailedResult
    )
    result = runner.run(suite)

    # Print summary
    passed_count = result.testsRun - len(result.failures) - len(result.errors)
    print()
    print(f"  Tests Run    : {result.testsRun}")
    print(f"  Tests Passed : {passed_count}")
    print(f"  Tests Failed : {len(result.failures)}")
    print(f"  Errors       : {len(result.errors)}")

    # Build details dict for HTML report
    details = {
        'total': result.testsRun,
        'passed': passed_count,
        'failed': len(result.failures) + len(result.errors),
        'passed_tests': getattr(result, 'passed_tests', []),
        'failed_tests': getattr(result, 'failed_tests', []),
    }

    success = result.wasSuccessful()
    if success:
        print("\n  [TEST STAGE PASSED] All tests passed!")
    else:
        print("\n  [TEST STAGE FAILED] Some tests failed.")

    return success, details
