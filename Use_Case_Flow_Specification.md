# Use-Case Flow Specification

## UC-001 – Settle Group Debts

### Use Case ID

**UC-001**

### Use Case Name

**Settle Group Debts**

### Primary Actor

**Group Traveler**

### Supporting Actor

**Trip Admin**

### Goal

Generate and optionally confirm a minimum-transaction payment plan that settles all outstanding trip balances.

---

## 1. Preconditions

1. The Group Traveler is authenticated and has access to the trip.
2. The trip contains at least two travelers.
3. Recorded expenses are valid and the latest traveler balances have been calculated.
4. All required exchange-rate conversions for recorded expenses are available.
5. The group balances are ready to be processed for settlement.

---

## 2. Main Success Scenario

1. The Group Traveler selects **Settle Group Debts** for the trip.

2. The system retrieves the latest recorded expenses and current net balances for all travelers.

3. The system verifies that the total group balance reconciles to zero.

4. The system separates travelers into:

   * Travelers who should receive money.
   * Travelers who need to pay money.

5. The system computes a debt settlement graph that minimizes the number of peer-to-peer payment transactions.

6. The system generates the proposed payment transactions.

7. The system displays each proposed payment with:

   * Payer
   * Recipient
   * Payment amount

8. The Group Traveler reviews the proposed settlement plan.

9. The Group Traveler confirms the settlement plan.

10. The system records the confirmed settlement instructions and marks the relevant balances as pending settlement.

11. The use case ends successfully.

---

## 3. Alternate Flow – Balance or Exchange-Rate Problem

**A1.** The system detects that the group balances do not reconcile to zero, or a required exchange rate is unavailable.

**A2.** The system does not generate a settlement plan.

**A3.** The system identifies the affected expense or conversion data and displays an appropriate error message.

**A4.** The user corrects the expense information or waits for the required exchange-rate information to become available.

**A5.** The user retries **Settle Group Debts** after the data becomes valid.

---

## 4. Postconditions

1. A valid settlement graph is displayed to the traveler.
2. If the traveler confirms the plan, the settlement instructions are stored.
3. The settlement instructions preserve every traveler's calculated net balance.
4. The system records the settlement confirmation and status for auditing.
5. The original expense records remain unchanged.

---

## 5. Success Guarantee

The system provides a valid and transaction-efficient payment plan that settles the group's current net balances while preserving the underlying expense records.

---

## 6. Exception Summary

| Exception                       | System Response                                       |
| ------------------------------- | ----------------------------------------------------- |
| Invalid expense data            | Reject the affected data and request correction       |
| Group balances do not reconcile | Do not generate settlement plan                       |
| Exchange rate unavailable       | Notify user and wait for valid rate                   |
| Unauthorized user               | Deny protected operation                              |
| No valid settlement possible    | Display an error and request correction of input data |
