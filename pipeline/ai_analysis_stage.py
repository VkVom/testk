"""
===============================================================
   STAGE 3: AI CODE ANALYSIS STAGE
===============================================================

WHAT IS THE AI ANALYSIS STAGE?
  Uses rule-based static analysis to check code quality.
  Reads the code using Python's 'ast' (Abstract Syntax Tree)
  module and applies rules to detect common issues.

  Returns all findings as a dictionary so the HTML report
  can display them in a beautiful, organized way.
"""

import ast
import os
import time


def check_function_length(tree, max_lines=15):
    """Finds functions that are longer than max_lines."""
    warnings = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if hasattr(node, 'end_lineno'):
                length = node.end_lineno - node.lineno + 1
                if length > max_lines:
                    warnings.append(
                        f"Function '{node.name}' is {length} lines long "
                        f"(recommended max: {max_lines})"
                    )
    return warnings


def check_missing_docstrings(tree):
    """Finds functions that don't have a docstring description."""
    warnings = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if node.name.startswith("__") and node.name.endswith("__"):
                continue
            if not ast.get_docstring(node):
                warnings.append(
                    f"Function '{node.name}' is missing a docstring"
                )
    return warnings


def check_short_variable_names(tree):
    """Finds variables with very short (unclear) names."""
    warnings = []
    acceptable = {'i', 'j', 'k', 'n', 'x', 'y', 'z', 'e', 'f'}
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    if len(target.id) < 2 and target.id not in acceptable:
                        warnings.append(
                            f"Variable '{target.id}' at line {node.lineno} "
                            f"has a very short name"
                        )
    return warnings


def check_todo_comments(source_code):
    """Finds TODO or FIXME comments left in the code."""
    warnings = []
    for num, line in enumerate(source_code.split('\n'), 1):
        if 'TODO' in line.upper() or 'FIXME' in line.upper():
            warnings.append(f"Line {num} has a TODO/FIXME comment")
    return warnings


def check_line_length(source_code, max_len=79):
    """Finds lines longer than PEP8's recommended 79 characters."""
    warnings = []
    for num, line in enumerate(source_code.split('\n'), 1):
        if len(line) > max_len:
            warnings.append(
                f"Line {num} is {len(line)} chars long (max: {max_len})"
            )
    return warnings


def suggest_test_cases(tree):
    """Suggests test function names for each function found."""
    suggestions = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if not node.name.startswith("_"):
                suggestions.append(
                    f"Write a test called 'test_{node.name}()'"
                )
    return suggestions


def run_ai_analysis():
    """
    Main AI Analysis function.
    Analyzes sample_code/edtech_app.py and returns all findings.
    Also saves a text report to reports/ai_analysis_report.txt
    """

    filepath = "sample_code/edtech_app.py"
    print(f"  Analyzing: {filepath}")
    time.sleep(0.4)

    if not os.path.exists(filepath):
        print("  [SKIP] File not found.")
        return {}

    with open(filepath, 'r') as f:
        source_code = f.read()

    try:
        tree = ast.parse(source_code)
    except SyntaxError as e:
        print(f"  [ERROR] Syntax error in file: {e}")
        return {}

    # Run all rule checks
    findings = {
        "Long Functions":       check_function_length(tree),
        "Missing Docstrings":   check_missing_docstrings(tree),
        "Short Variable Names": check_short_variable_names(tree),
        "TODO Comments":        check_todo_comments(source_code),
        "Long Lines (Style)":   check_line_length(source_code),
        "Test Suggestions":     suggest_test_cases(tree),
    }

    # Print to terminal
    total = 0
    for category, items in findings.items():
        print(f"\n  --- {category} ---")
        if items:
            for item in items:
                print(f"    [!] {item}")
                total += 1
                time.sleep(0.05)
        else:
            print("    [OK] No issues found.")

    print(f"\n  Total issues/suggestions: {total}")

    # Save text report
    os.makedirs("reports", exist_ok=True)
    with open("reports/ai_analysis_report.txt", 'w') as f:
        f.write("AI CODE ANALYSIS REPORT\n")
        f.write("=" * 50 + "\n\n")
        for category, items in findings.items():
            f.write(f"--- {category} ---\n")
            for item in items:
                f.write(f"  [!] {item}\n")
            if not items:
                f.write("  [OK] No issues.\n")
            f.write("\n")
        f.write(f"Total: {total} issues/suggestions\n")

    return findings
