# Lab 5 - Reflection

Shriya Vasundhara Singh | PES1UG24AM269

The supplied PDF refers to reflection questions but does not show their wording. These four clearly labelled topics address the lab objectives; they are not quoted questions from the handout.

## What did the three tools contribute?

Pylint identified quality problems such as the mutable default, unused currency parameter, missing documentation and inconsistent names. Bandit found the shell command, unsafe XML parser and stored password. Flake8 found spacing, blank-line and line-length violations. Using all three covered more problems than using only one.

## Which issues were prioritized, and why?

The high-severity B605 finding was addressed first because the meter address could become shell instructions. Medium-severity B314 was next because XML can contain malicious entities. The two low-severity Bandit findings were also fixed before quality and style cleanup.

## How was correctness checked after the fixes?

The original and final demos were compared using captured terminal output and parsed JSON. Both produced M1=708.75, M2=2661.75, M3=78.75 and M4=288.75, with total 3738.00 and average 934.50. Regression checks covered slab boundaries, reversed readings, fees, JSON storage, import behavior, XML entities and mocked meter requests.

## What are the benefits and limits of static analysis?

Static analysis makes suspicious patterns and inconsistent style visible early, improving maintainability and review. A clean report does not prove correctness or complete security. Tests and human review are still needed. The HTTPS helper was checked with mocks; no real meter endpoint was available for an integration test.
