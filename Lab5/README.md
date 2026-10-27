# Lab 5 submission

Name: Shriya Vasundhara Singh  
SRN: PES1UG24AM269  
Date: 27 October 2026

Assigned repository: https://github.com/SETAPESU26/L5_30_electricity_bill
Original commit: a48c8e9fe56e72e1d809174a23ec2e96a67dd48e

Contents: cleaned electricity_bill.py, Lab_5_Report.pdf, issues.md,
reflection.md, reports/before and reports/after, evidence and regression tests.
An empty reports/after/flake8_report.txt is the actual successful tool output;
commands.json records the zero exit status. Tool stderr is saved separately.

## Reproduce

    python -m venv .venv
    .venv\Scripts\python -m pip install -r requirements-dev.txt
    .venv\Scripts\python electricity_bill.py
    .venv\Scripts\python -m pylint --persistent=n electricity_bill.py
    .venv\Scripts\python -m bandit -r electricity_bill.py
    .venv\Scripts\python -m flake8 electricity_bill.py
    .venv\Scripts\python tests/test_electricity_bill.py
    git log --oneline -4

Three fix commits follow the uploaded baseline, grouped by Bandit,
Pylint and Flake8. No checks were disabled. All deliverables are uploaded
to this Lab5 folder. The original local commit hashes are recorded in
commit_history.txt for provenance; the GitHub commit history shows the
corresponding upload commits. No course-portal submission was performed.

The unused sync helper now requires a numeric IP and verified HTTPS on port
443. Its return value is response bytes. The demo never calls this helper.
Real meters must offer HTTPS with a trusted certificate for their IP.
Function names now follow snake_case; average_bill no longer accepts the
unused currency argument. External callers, if any, must use the new names.

The supplied handout omits the exact reflection question wording; the
reflection document therefore uses four labelled learning-objective topics.
