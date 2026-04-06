"""
===============================================================
   STAGE 1: BUILD STAGE
===============================================================

WHAT IS THE BUILD STAGE?
  Checks that all required files exist and Python version
  is correct before anything else runs.
  Like a checklist before a flight takes off!
"""

import os
import sys
import time


def check_file_exists(filepath):
    """Checks if a file exists. Returns (True/False, message)."""
    if os.path.exists(filepath):
        print(f"  [OK]      Found: {filepath}")
        time.sleep(0.2)
        return True
    else:
        print(f"  [MISSING] Not found: {filepath}")
        return False


def check_python_version():
    """Checks Python version is 3.x or higher."""
    version = sys.version_info
    print(f"  [INFO]    Python version: {version.major}.{version.minor}.{version.micro}")
    time.sleep(0.2)
    if version.major >= 3:
        print("  [OK]      Python 3.x detected — acceptable!")
        return True
    else:
        print("  [FAIL]    Python 3.x is required.")
        return False


def run_build():
    """
    Main Build Stage function.
    Returns True if all checks pass, False if any fail.
    """

    print("  Checking Python version...")
    python_ok = check_python_version()

    print("\n  Checking required project files...")
    required_files = [
        "sample_code/edtech_app.py",
        "tests/test_edtech_app.py",
        "pipeline/ai_analysis_stage.py",
    ]

    all_ok = True
    for f in required_files:
        if not check_file_exists(f):
            all_ok = False

    print()
    if python_ok and all_ok:
        print("  [BUILD PASSED] All checks successful!")
        return True
    else:
        print("  [BUILD FAILED] Fix the issues above.")
        return False
