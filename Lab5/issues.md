# Lab 5 - Documented Issues

Shriya Vasundhara Singh | PES1UG24AM269

Line numbers refer to the original assigned source at commit a48c8e9fe56e72e1d809174a23ec2e96a67dd48e. Bandit severities are reported by the tool; Pylint categories are not security severities.

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Shell command injection | Bandit B605 / High | 61-63 | A meter address is concatenated into an os.system command. | Use an HTTPS client directly, validate an IP literal, set a timeout, and close the connection in finally. |
| Unsafe XML parsing | Bandit B314 / Medium | 18 | ElementTree.fromstring accepts untrusted XML without hardening. | Use defusedxml.ElementTree.fromstring; verify entity input is rejected. |
| Unsafe XML import | Bandit B405 / Low | 3 | The standard XML parser import is flagged for untrusted input. | Replace the import with defusedxml and declare its dependency. |
| Hard-coded password | Bandit B105 / Low | 13 | An unused password literal is stored in source. | Remove the unused credential; the program has no authentication flow. |
| Mutable default argument | Pylint W0102 / Warning | 42 | extras={} creates a shared default dictionary. It is not mutated by the original function, but is a risky default for later changes. | Default extras to None and create a fresh dictionary inside the function. |
| Unused parameter | Pylint W0613 / Warning | 50 | The currency argument has no effect on averageBill. | Remove the argument and update its caller; billing remains in rupees. |
| Unspecified encoding | Pylint W1514 / Warning | 57 | JSON output relies on the operating system default encoding. | Open the output file with encoding="utf-8". |
| Nonstandard names | Pylint C0103 / Convention | 17-76 | Functions, arguments and local variables use camelCase. | Use snake_case names consistently and update internal callers. |
| Missing documentation | Pylint C0114/C0116 / Convention | 1,17-66 | The module and functions lack descriptions. | Add concise module and function docstrings. |
| PEP 8 formatting | Flake8 E302/E203/E501/E225 | 22,44,72,76 | Missing blank line, whitespace before a colon, an 86-character line and missing operator spacing. | Use two blank lines between functions, correct spacing and wrap long statements below 80 characters. |

Additional improvements: guard main() so importing does not run the demo; clear BILLS at demo startup so repeated runs do not accumulate old results. These are review improvements, not claimed as original tool findings.
