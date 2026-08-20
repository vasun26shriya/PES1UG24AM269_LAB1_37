# Group Travel Expense Simplification Engine

## PES University – Department of CSE

**Lab 1: Requirements Engineering & UML Use-Case Modelling**

**Problem Statement #37 – Retail, E-Commerce & Finance**

---

## 1. Problem Statement

The **Group Travel Expense Simplification Engine** is a multi-currency expense-sharing utility designed to simplify the management and settlement of expenses incurred by groups during travel.

The system records uneven group expenses, handles expenses in multiple currencies using daily exchange rates, calculates the net balance of each traveler, and generates a debt settlement plan that minimizes the number of peer-to-peer transactions required.

---

## 2. Objectives

The main objectives of the system are:

* Record expenses made by different members of a travel group.
* Support uneven expense sharing between travelers.
* Support multiple currencies.
* Convert foreign-currency expenses using daily exchange rates.
* Calculate the net balance of each traveler.
* Generate an optimized debt settlement graph.
* Minimize the number of peer-to-peer payment transactions.
* Allow authorized users to manage trip members and expenses.
* Maintain an auditable record of important changes.

---

## 3. Actors

### Group Traveler

A traveler who participates in a trip and can:

* Create or join a trip.
* Record expenses.
* View trip balances.
* View the settlement plan.
* Settle group debts.

### Trip Admin

A user responsible for managing the trip who can:

* Manage trip members.
* Manage expenses.
* View balances.
* Generate or review settlement information.

### Exchange Rate Service

An external service that provides the daily exchange rates required to convert expenses between supported currencies.

### Payment Service

An external service that can be used to process or support settlement payments between travelers.

---

## 4. Functional Requirements

The system contains five functional requirements:

* **FR-001:** Record group expenses.
* **FR-002:** Convert expenses between supported currencies.
* **FR-003:** Calculate and display traveler net balances.
* **FR-004:** Generate a minimum-transaction debt settlement graph.
* **FR-005:** Allow authorized users to manage expenses and participants while maintaining an audit trail.

Detailed requirements are available in [`Requirements.md`](Requirements.md).

---

## 5. Non-Functional Requirements

The system contains two non-functional requirements:

* **NFR-001:** The balance and settlement calculation engine shall execute within 100 ms for groups of up to 50 travelers and 500 expenses under normal operating conditions.
* **NFR-002:** The system shall protect trip and financial data using authentication, authorization, encrypted communication, and secure storage controls.

Detailed requirements are available in [`Requirements.md`](Requirements.md).

---

## 6. UML Use-Case Diagram

The UML diagram models the major actors and use cases of the system.

### Primary Actors

* Group Traveler
* Trip Admin

### Supporting Actors

* Exchange Rate Service
* Payment Service

### Important Use Cases

* Create / Join Trip
* Record Expense
* View Trip Balances
* Convert Currency
* Settle Group Debts
* View Settlement Plan
* Manage Trip Members
* Record Settlement
* Authenticate User

The diagram includes both:

* `<<include>>` relationships
* `<<extend>>` relationship

The complete diagram is available here:

**[UML Use-Case Diagram](UML_Use_Case_Diagram.png)**

---

## 7. Core Use Case

The selected core use case is:

**UC-001 – Settle Group Debts**

This use case allows a traveler to generate a payment plan that settles the group's outstanding balances while minimizing the number of payment transactions.

The complete flow specification is available in [`Use_Case_Flow_Specification.md`](Use_Case_Flow_Specification.md).

---

## 8. Repository Contents

| File                             | Description                                   |
| -------------------------------- | --------------------------------------------- |
| `README.md`                      | Project overview and repository documentation |
| `Requirements.md`                | Functional and non-functional requirements    |
| `Use_Case_Flow_Specification.md` | Detailed UC-001 flow specification            |
| `UML_Use_Case_Diagram.png`       | UML use-case diagram                          |

---

## 9. Expected System Outcome

The system should allow a group of travelers to enter their expenses, calculate how much each person owes or should receive, and produce a simple and efficient settlement plan.

The final settlement should:

1. Preserve all traveler balances.
2. Ensure the total group balance is zero.
3. Minimize unnecessary peer-to-peer transactions.
4. Support expenses recorded in different currencies.
5. Provide secure access to trip and financial information.
