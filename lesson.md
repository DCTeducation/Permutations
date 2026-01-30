
---

## lesson.md (the actual lesson plan)

```md
# Lesson Plan: Permutations (Order Matters)

## Audience
Grade 11–12 (or beginner discrete math)

## Learning Goals
By the end, students can:
1. Decide when a problem is a permutation (order matters).
2. Use the multiplication principle.
3. Use formulas:
   - \( P(n,r) = \frac{n!}{(n-r)!} \)
   - Special case: arranging all \(n\) items → \(n!\)
4. Use Python to:
   - Generate permutations
   - Verify answers
   - Compare brute-force counting vs formulas

## Time
45–60 minutes

---

## Part 1 — The Core Idea (5–10 min)

### Definition
A **permutation** is an arrangement where **order matters**.

**Quick test:**
If changing the order creates a different outcome, it’s a permutation.

Example:
- PIN 1234 is NOT the same as 4321 → permutation

---

## Part 2 — Multiplication Principle (10 min)

If you have:
- 5 choices for the first position
- 4 for the second
- 3 for the third  
Then total = \(5 · 4 · 3\)

### Example
How many 3-letter “codes” can be made from A, B, C, D, E without repeats?

Answer:
\(5 · 4 · 3 = 60\)

---

## Part 3 — Permutation Formula (10–15 min)

### Arranging r items from n distinct items (no repeats)
\[
P(n,r)=\frac{n!}{(n-r)!}
\]

### Why it works
You’re multiplying:
\[
n · (n-1) · (n-2) · ... \text{(r terms)}
\]
Factorials package this cleanly.

### Example
How many ways to arrange 4 students chosen from 10 students in a line?

\[
P(10,4)=\frac{10!}{6!}=10·9·8·7=5040
\]

---

## Part 4 — Code Demo (10–15 min)

We use Python to:
- Generate permutations using `itertools.permutations`
- Count them
- Compare brute force vs formula

Run:
- `python code/permutations_basics.py`
- `python code/brute_force_vs_formula.py`

---

## Part 5 — Practice (10–15 min)

Go to `exercises.md`.

---

## Exit Check (2 min)
1. Does order matter in a phone number? Why?
2. Compute \(P(8,3)\).
3. In your own words: why is a permutation different from a combination?
