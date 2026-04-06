# AI-Enhanced CI/CD Pipeline for EdTech Software
### BCA Final Year Project | Keerthi | 2024-25

---

## What Is This Project?

This project demonstrates how modern software teams use a **CI/CD Pipeline** to automatically:
1. **Build** – Check if the code is ready
2. **Test** – Run automated tests to verify the code works
3. **Analyze** – Use AI (rule-based) to check code quality
4. **Deploy** – Simulate pushing the code to a server

It is built for an **EdTech (Educational Technology)** software platform.

---

## Project Structure

```
cicd_project/
│
├── run_pipeline.py                  ← MAIN FILE — run this to start the pipeline
│
├── pipeline/
│   ├── build_stage.py               ← Stage 1: Build checks
│   ├── test_stage.py                ← Stage 2: Runs automated tests
│   ├── ai_analysis_stage.py         ← Stage 3: AI code quality checker
│   └── deploy_stage.py              ← Stage 4: Simulated deployment
│
├── sample_code/
│   └── edtech_app.py                ← The EdTech app code (what gets built/tested/analyzed)
│
├── tests/
│   └── test_edtech_app.py           ← Automated tests for the EdTech app
│
├── reports/                         ← Created automatically when pipeline runs
│   ├── ai_analysis_report.txt       ← AI analysis output
│   └── deployment_log.txt           ← Deployment log
│
└── .github/workflows/pipeline.yml   ← GitHub Actions config (for real GitHub CI/CD)
```

---

## Requirements

- **Python 3.x** — No other libraries needed! (Uses only built-in Python modules)

Check your Python version:
```bash
python --version
```

---

## How to Run

### Step 1: Open a terminal / command prompt

### Step 2: Navigate to the project folder
```bash
cd cicd_project
```

### Step 3: Run the full pipeline
```bash
python run_pipeline.py
```

That's it! You'll see each stage run one by one with detailed output.

---

## How to Run Just the Tests

If you want to run only the tests (Stage 2):
```bash
python -m unittest discover tests/
```

Or with more detail:
```bash
python -m unittest tests/test_edtech_app.py -v
```

---

## How to Run Just the EdTech App (demo)

To see the EdTech app work on its own:
```bash
python sample_code/edtech_app.py
```

---

## How to Run Just the AI Analyzer

```bash
python -c "from pipeline.ai_analysis_stage import run_ai_analysis; run_ai_analysis()"
```

---

## What Each Stage Does

| Stage | File | What It Does |
|-------|------|--------------|
| 1. Build | `pipeline/build_stage.py` | Checks Python version and required files exist |
| 2. Test | `pipeline/test_stage.py` | Runs all tests in `tests/` automatically |
| 3. AI Analysis | `pipeline/ai_analysis_stage.py` | Scans code for quality issues using rules |
| 4. Deploy | `pipeline/deploy_stage.py` | Simulates pushing code to a server |

---

## What the AI Analyzer Checks

The AI analyzer (`ai_analysis_stage.py`) uses **rule-based static analysis** — no machine learning needed. It checks for:

1. **Long functions** – Functions over 15 lines (hard to read)
2. **Missing docstrings** – Functions without descriptions
3. **Short variable names** – Variables like `a`, `b` (not descriptive)
4. **TODO comments** – Unfinished work markers
5. **Long lines** – Lines over 79 characters (PEP8 style guide)
6. **Test suggestions** – Hints for which functions need tests

---

## Reports Generated

After running the pipeline, check the `reports/` folder:

- `ai_analysis_report.txt` — Full AI code analysis
- `deployment_log.txt` — Simulated deployment details

---

## Setting Up on GitHub (Optional — for real CI/CD demo)

1. Create a free account at [github.com](https://github.com)
2. Create a new repository
3. Upload all project files
4. The `.github/workflows/pipeline.yml` file tells GitHub to run the pipeline automatically on every push!
5. Go to the **Actions** tab on GitHub to see it run

---

## Technology Used

| Component | Technology |
|-----------|-----------|
| Programming Language | Python 3.x |
| Testing Framework | unittest (built-in) |
| Code Analysis | ast module (built-in) |
| CI/CD Automation | Python scripts + GitHub Actions |
| Version Control | Git + GitHub |
| Output | CLI logs + Text report files |

---

## Viva Quick Reference

**Q: What is CI/CD?**  
A: CI = Continuous Integration (auto build & test on every code push). CD = Continuous Deployment (auto deploy passing code).

**Q: What does the AI do?**  
A: It does rule-based static analysis — reads the code and checks for issues like long functions, missing comments, and short variable names. No machine learning is used.

**Q: Why is deployment simulated?**  
A: Real deployment needs cloud servers (AWS, Azure) which are out of scope for an undergraduate project. The simulation shows the concept.

**Q: What tools does this use?**  
A: Python's built-in `unittest` for testing, `ast` module for code analysis, and GitHub Actions for real CI/CD automation.

---

*Project by Keerthi | BCA Final Year | Department of Computer Science | 2024–25*
