# Week 0 Math Diagnostic

**Sit this before Week 1 starts.**

## Rules

- **90 minutes. Closed book.** No notes, no internet, no calculator beyond arithmetic.
- Write the working, not just the answer. Partial credit is real.
- If stuck, write down what you *would* look up. That is diagnostic information.
- **Do not cheat.** The only person you can lie to here is your own schedule. A score inflated by 20% costs three months of planning error.

**Pass 1:** closed-book, timed, scored. This measures **retention**.

**Pass 2:** afterwards, with notes, redo everything missed. This measures **re-learning speed**.

The **gap between the two scores** is the real signal. A small gap means genuine relearning is needed. A large gap means it is all still in there and just needs waking up.

---

## Section A — Calculus (4 points)

**A1.** Evaluate `∫₀^∞ x·e^(−x) dx`.

**A2.** Differentiate `ln(cos x)`. Then expand `e^x · cos x` as a Taylor series up to and including the `x³` term.

**A3.** State the value of `∫_{−∞}^{∞} e^(−ax²) dx` for `a > 0`, and sketch how it is derived.

**A4.** For `f(x,y) = x²y + y³`: find the gradient, then the directional derivative at `(1,2)` in the direction of the vector `(3,4)`.

---

## Section B — Linear algebra (3 points)

**B1.** Find the eigenvalues and eigenvectors of `[[2,1],[1,2]]`.

**B2.** Define a positive semi-definite matrix. Give one practical test for PSD-ness. Explain why a covariance matrix is always PSD.

**B3.** What does the singular value decomposition give you, geometrically? Name one thing it is used for in finance.

---

## Section C — Probability (8 points)

**Weighted heaviest, on purpose.** This is the working mathematics of market microstructure, and it is the section physics graduates are typically weakest at — stat mech is not the same thing as probability theory.

**C1.** Two fair dice are rolled. Given that the sum is 8, what is the probability that at least one die shows a 3?

**C2.** `X ~ Exponential(λ)`. Compute `E[X]` and `Var[X]` from the definition. Then show that `P(X > s+t | X > s) = P(X > t)`, and say in one sentence what that property is called and why it matters.

**C3.** `X, Y` are iid `Uniform(0,1)`. Compute `E[max(X,Y)]` and `P(X + Y < 1)`.

**C4.** Define conditional expectation `E[X | Y]`. State the tower property. Then use it: a coin with unknown bias `p ~ Uniform(0,1)` is flipped once — what is the probability of heads?

**C5.** `Sₙ` is a simple symmetric random walk (steps of ±1, fair). Give `E[Sₙ]` and `Var[Sₙ]`. Compute `P(S₁₀ = 0)`. Define a martingale, and state whether `Sₙ` is one.

**C6.** State the Central Limit Theorem precisely. Then: 100 iid random variables with mean 0 and variance 1 — approximate `P(sum > 20)`.

**C7.** A stock's mid-price is 100.00 with a spread of 0.02. You buy at the ask and immediately sell at the bid. What is your loss? Now: if you could instead post at the bid and get filled half the time, and must cross the spread the other half, what is your expected cost per round trip? *(This one is deliberately not a textbook problem — it is the kind of reasoning the job actually requires.)*

**C8.** What is the difference between correlation and independence? Give a concrete example of two variables that are uncorrelated but not independent.

---

## Section D — Differential equations (2 points)

**D1.** Solve `dy/dx = −ky` with `y(0) = y₀`. Then solve `y'' + 3y' + 2y = 0`.

**D2.** Write down the one-dimensional heat equation. In one sentence, say what it describes physically — and, if you know, what it has to do with option pricing.

---

## Section E — Numerical & computational (3 points)

**E1.** Describe how to estimate π by Monte Carlo. How does the error scale with the number of samples `N`? What is the practical consequence of that scaling?

**E2.** Why does `0.1 + 0.2 != 0.3` in floating point? What is catastrophic cancellation, and give an example where it would destroy a financial calculation.

**E3.** You must compute a running mean and variance of a stream of prices, in one pass, without storing the data. Describe an approach. What goes wrong with the naive `E[X²] − E[X]²` formula?

---

## Scoring

**Total: 20 points.** Score each part generously for correct method, harshly for hand-waving.

Record in the log:
- `Pass 1 total: __ / 20`
- `Pass 1 Section C: __ / 8`
- `Pass 2 total: __ / 20`

### Setting the math block length

Use **whichever row is worse** — the overall score or the Section C score. Probability dominates because probability *is* the job.

| Pass 1 overall | Pass 1 Section C | Math block |
|---|---|---|
| ≥ 85% (17+) | ≥ 80% (7+) | **4 weeks** — refresh only. Straight into statistics and microstructure. |
| 60–85% (12–16) | 60–80% (5–6) | **8 weeks** — the assumed default. Probability-first. |
| 40–60% (8–11) | 40–60% (3–4) | **12 weeks** — real relearning. Blitzstein properly, front to back. |
| < 40% (<8) | < 40% (<3) | **16 weeks**, and revisit the timeline honestly at Week 16. |

### Reading the gap

- **Gap < 15%** — it genuinely is not there. Take the longer block. No shame in it; the degree bought re-learning *speed*, not retained knowledge.
- **Gap > 30%** — it is all still there, just cold. Take the shorter block and lean on problem sets rather than lectures.

### If Section C is much weaker than the rest

Expected, and fine. Spend the entire block on Blitzstein & Hwang's *Introduction to Probability* and ignore the rest. Rusty calculus costs almost nothing in this field. Weak probability costs everything.
