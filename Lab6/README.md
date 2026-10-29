# Lab 6: Code and Branch Coverage Analysis

**Name:** Shriya Vasundhara Singh  
**SRN:** PES1UG24AM269  
**Assigned application:** 30 - Vending Machine

Assignment mapping: row 30 of `Lab-6-7-Repo-Assignment_in_Lab5_E.xlsx` assigns this SRN to [SETAPESU26/L6_L7_30_vending_machine](https://github.com/SETAPESU26/L6_L7_30_vending_machine). The original application and starter tests are preserved without changes. Only the supplied Lab 6 handout defines deliverables; no Lab 7 handout was supplied.

## Results

| Test suite | Passed | Statements covered | Branch outcomes covered | Coverage.py combined score |
| --- | ---: | ---: | ---: | ---: |
| Original starter (line run) | 2 | 13/30 (43.33%) | Not measured | 43% |
| Original starter (branch run) | 2 | 13/30 (43.33%) | 6/18 (33.33%) | 40% |
| CodeCoverageTest_vending_machine.py | 11 | 30/30 (100%) | Not measured | 100% |
| BranchCoverageTest_vending_machine.py | 30 | 30/30 (100%) | 18/18 (100%) | 100% |

Running all three files together passes **43 tests**. Measurement is restricted to `vending_machine.py`, so test code does not inflate coverage. Coverage.py's branch-mode `Cover` column combines statements and branch outcomes; it is not a pure branch percentage.

## Deliverables

- [Code coverage tests](CodeCoverageTest_vending_machine.py)
- [Branch coverage tests](BranchCoverageTest_vending_machine.py)
- [Code output image](evidence/code_coverage_output.png) and [verbatim output](evidence/code_terminal_output.txt)
- [Branch output image](evidence/branch_coverage_output.png) and [verbatim output](evidence/branch_terminal_output.txt)
- [Line measurement JSON](evidence/code_coverage.json) and [branch measurement JSON](evidence/branch_coverage.json)
- [Coverage analysis](coverage_analysis.md)

Evidence images show verbatim captured command output in a browser-rendered transcript viewer. They are screenshots of that viewer, rather than native terminal-window captures; the text logs and JSON retain the actual measured results. Only successful final results are pictured. Initial results are retained as text for comparison.

## Reproduce

From this `Lab6` directory, with Python 3.12:

```sh
python -m pip install -r requirements.txt
python -m coverage run --source=vending_machine -m pytest -q CodeCoverageTest_vending_machine.py
python -m coverage report -m --fail-under=90
python -m coverage run --branch --source=vending_machine -m pytest -q BranchCoverageTest_vending_machine.py
python -m coverage report -m --fail-under=90
python -m pytest -q
```

The explicit filenames work with pytest independently; `pytest.ini` also enables automatic discovery of the handout's required capitalized filenames. Coverage data files are ignored and each measurement starts a fresh run.

## Commit stages

1. Code coverage test suite, unmodified assigned application, starter tests, line results and evidence.
2. Branch coverage test suite, branch results and evidence, and final analysis.
