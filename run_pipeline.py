"""
===============================================================
   AI-Enhanced CI/CD Pipeline for EdTech Software
   MAIN PIPELINE RUNNER
   Author  : Keerthi
   Project : BCA Final Year | 2024-25
   Dept    : Computer Science
===============================================================

HOW TO RUN:
    python run_pipeline.py

WHAT THIS DOES:
  Runs all 4 pipeline stages one by one in the terminal.
  Each stage is color-coded so you can clearly see what
  is happening step by step.

  Stage 1 - BUILD   : Checks files and Python version
  Stage 2 - TEST    : Runs all automated unit tests
  Stage 3 - ANALYZE : AI rule-based code quality analysis
  Stage 4 - DEPLOY  : Simulated deployment with a log file

PIPELINE GATE RULE:
  If Stage 1 (Build) fails  -> pipeline STOPS.
  If Stage 2 (Test) fails   -> pipeline STOPS.
  Stage 3 never stops the pipeline (it is informational).
  Stage 4 always runs if Tests pass.

OUTPUT FILES (saved to reports/ folder):
  - reports/ai_analysis_report.txt   (from Stage 3)
  - reports/deployment_log.txt       (from Stage 4)
"""

import datetime
import time
import sys
import os

class Color:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    RED     = "\033[91m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    BLUE    = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN    = "\033[96m"
    WHITE   = "\033[97m"


def c(color, text):
    return f"{color}{text}{Color.RESET}"


def slow_print(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def print_banner():
    print()
    print(c(Color.CYAN, "=" * 60))
    slow_print(c(Color.BOLD + Color.CYAN, "   AI-ENHANCED CI/CD PIPELINE - EdTech Project"), delay=0.015)
    print(c(Color.CYAN,  "   Student : Keerthi"))
    print(c(Color.CYAN,  "   Course  : BCA Final Year | 2024-25"))
    print(c(Color.CYAN,  "   Dept    : Computer Science"))
    print(c(Color.CYAN, "=" * 60))
    print(c(Color.WHITE, f"   Started : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"))
    print(c(Color.CYAN, "=" * 60))
    print()
    time.sleep(0.5)


def print_stage_header(number, name, color):
    print()
    print(c(color, "-" * 60))
    slow_print(c(Color.BOLD + color, f"  >>> STAGE {number}: {name} <<<"), delay=0.02)
    print(c(color, "-" * 60))
    time.sleep(0.3)


def print_result(passed, stage_name):
    print()
    if passed:
        print(c(Color.GREEN, f"  [ PASSED ] {stage_name} completed successfully!"))
    else:
        print(c(Color.RED,   f"  [ FAILED ] {stage_name} did not pass!"))
    time.sleep(0.4)


from pipeline.build_stage       import run_build
from pipeline.test_stage        import run_tests
from pipeline.ai_analysis_stage import run_ai_analysis
from pipeline.deploy_stage      import run_deploy


def main():
    print_banner()
    start_time = datetime.datetime.now()

    # STAGE 1: BUILD
    print_stage_header(1, "BUILD", Color.CYAN)
    build_passed = run_build()
    print_result(build_passed, "BUILD")
    if not build_passed:
        print(c(Color.RED, "\n  Pipeline stopped. Fix build errors first.\n"))
        return

    # STAGE 2: TEST
    print_stage_header(2, "TEST", Color.YELLOW)
    tests_passed, test_details = run_tests()
    print_result(tests_passed, "TEST")
    if not tests_passed:
        print(c(Color.RED, "\n  Pipeline stopped. Fix failing tests first.\n"))
        return

    # STAGE 3: AI ANALYSIS
    print_stage_header(3, "AI CODE ANALYSIS", Color.MAGENTA)
    analysis_findings = run_ai_analysis()
    print()
    print(c(Color.MAGENTA, "  AI Analysis complete. See findings above."))
    time.sleep(0.4)

    # STAGE 4: DEPLOY
    print_stage_header(4, "DEPLOY (Simulated)", Color.BLUE)
    build_number = run_deploy()
    print_result(True, "DEPLOY")

    # FINAL SUMMARY
    end_time = datetime.datetime.now()
    duration = (end_time - start_time).seconds

    print()
    print(c(Color.GREEN, "=" * 60))
    print(c(Color.BOLD + Color.GREEN, "   PIPELINE COMPLETED SUCCESSFULLY!"))
    print(c(Color.GREEN, "=" * 60))
    print(c(Color.WHITE, f"   Build Number : {build_number}"))
    print(c(Color.WHITE, f"   Duration     : {duration} second(s)"))
    print(c(Color.WHITE, f"   Finished     : {end_time.strftime('%Y-%m-%d %H:%M:%S')}"))
    print(c(Color.WHITE,  "   Reports      : reports/ folder"))
    print(c(Color.GREEN, "=" * 60))
    print()


if __name__ == "__main__":
    main()
