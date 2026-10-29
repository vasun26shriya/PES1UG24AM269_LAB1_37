# Coverage analysis

Shriya Vasundhara Singh | PES1UG24AM269

## Concepts

Line (statement) coverage measures executable statements reached by tests. Branch coverage measures alternative control-flow outcomes, including decisions and loops. Executing every statement does not generally imply taking every branch. Path coverage considers complete sequences of decisions and is stronger than branch coverage; function coverage asks whether each function was called. Neither path nor function coverage is separately quantified here.

## Initial gaps

The supplied two tests only reject an unknown item and request zero change. They execute 13 of 30 statements. In branch mode, 6 of 18 branch outcomes are reached and four branch locations are partial. Missing statements are 8-12, 17, 21-22, 24 and 29-36. Thus the original tests never exercise valid selections, insufficient credit, nonzero change, negative change, or purchase behavior.

## Line test design

The 11 line cases reach every return and the negative-amount exception. Selection covers unknown items, missing stock, insufficient credit, and credit equal to price. Change tests cover zero, negative, unrepresentable amounts, and 290 (which uses every denomination and repeats the 100 coin). Purchase tests check rejection, inability to make exact change, and successful dispensing. Assertions verify returned status, exact coin lists, and stock preservation or decrement.

Result: 30/30 executable statements, zero missing statements, 100% line coverage. No source-code changes or coverage exclusions were needed.

## Branch test design

The independent 30-case branch suite covers both outcomes of each selection decision, negative/nonnegative change, zero/nonzero remainders, purchase rejection/success, and exact/unrepresentable change. The 290-change case exercises loop iteration and repetition; zero and small amounts exercise skipped loop bodies and loop termination.

| Decision or behavior | Representative inputs |
| --- | --- |
| Unknown / known item | water / cola, chips, candy |
| Stock missing, zero / available | empty stock, chips=0 / each item=1 |
| Credit below / at or above price | price-1, price, price+1 for all three items |
| Negative / nonnegative change | -1 / 0, 5, 10, 25, 50, 100, 290 |
| Coin loop repeats / skips | 290 / 0 and small amounts |
| Exact / impossible remainder | 0, denominations, 290 / 1, 4, 6, 101 |
| Failed / successful purchase | invalid, sold_out, insufficient / dispensed |
| Change failure preserves inventory | cola with credit=151 |
| Successful stock decrement | all items with exact price and excess credit |
| Inventory exhaustion | purchase last candy, then request candy again |

Result: 30/30 statements and 18/18 branch outcomes, zero missing branches, zero partial branches, 100% combined coverage. These results exceed both 90% thresholds.

## Interpretation and limits

The line suite happens to exercise the existing branch outcomes too, but the branch suite adds systematic price boundaries, every denomination, repeated purchases, and inventory assertions. Its value is explicit behavior verification beyond reaching lines. Full measured coverage does not prove correctness for every possible input or every path. The source does not validate negative stock, arbitrary types, or fractional monetary values; tests follow its supplied contract without changing application behavior.

The application values are integer coin units; tests do not assume a currency. Coverage JSON and command logs provide inspectable evidence. The PNGs display verbatim captured output in a transcript viewer; native terminal-window screenshots remain a separate presentation requirement if the evaluator insists on that exact format.
