# Data Dictionary

## test_pairs.json

Verifier evaluation test set. Top-level object with four arrays.

### `equivalent` (array)
Pairs that ARE mathematically equivalent. A verifier should ACCEPT each pair.

| Field | Type | Description |
|---|---|---|
| `a` | string | First expression, e.g. `2*(x+3)` |
| `b` | string | Second expression, equivalent to `a` |
| `cat` | string | Category: algebra, trig, log, radical, numeric, inequality, equation, rational |

### `non_equivalent` (array)
Pairs that are NOT equivalent. A verifier should REJECT each pair. Same three fields (`a`, `b`, `cat`).

### `malformed` (array)
Inputs that are not valid mathematical expressions. A verifier should reject them without accepting.

| Field | Type | Description |
|---|---|---|
| `a` | string | Malformed input |
| `cat` | string | Defect type: incomplete, unbalanced paren, invalid operator, empty, malformed number, missing argument, missing operand |

### `assumption_dependent` (array)
Identities valid only under domain assumptions (e.g. x > 0). Reported separately; no pass/fail ground truth. Same three fields (`a`, `b`, `cat`).

## Participant dataset (supplementary file)

Sheet `Participants`: one row per participant.

| Column | Type | Description |
|---|---|---|
| Participant_ID | string | Pseudonymous ID (P01–P28) |
| Participant_Group | string | BVI learner / Mathematics teacher / Accessibility expert |
| SUS_Q1–SUS_Q10 | integer | Raw System Usability Scale item responses (1–5) |
| SUS_Score_0_100 | float | Computed SUS score (0–100) |
| Ease of use | integer | Likert item (1–5) |
| Accessibility | integer | Likert item (1–5) |
| Navigation | integer | Likert item (1–5) |
| AI-assisted feedback | integer | Likert item (1–5) |
| Overall satisfaction | integer | Likert item (1–5) |

Sheet `Tasks`: one row per assigned task.

| Column | Type | Description |
|---|---|---|
| Task_ID | string | Task identifier (T001–T140) |
| Participant_ID | string | Participant who performed the task |
| Task_Type | string | Authentication / System navigation / Mathematical answer input / Feedback access / Assessment submission |
| Completion_Status | string | Completed / Not completed |
| Completion_Time_Min | float | Duration in minutes (blank if not completed) |

No identifiable participant information is included; the link between Participant_ID and identity is held by the authors and not published.
