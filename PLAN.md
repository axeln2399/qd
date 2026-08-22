# The 24-Month Plan

Week numbers are relative. Week 1 = whenever I start. 104 weeks total.

---

## The time model — read this first

I have ~10–11 hours a week. **But only ~5 of those hours can absorb new concepts.**

Studying after a 9-to-5 means the weekday hour is low-to-medium cognitive load. Trying to learn new mathematics at 9pm is how people conclude they aren't smart enough, when the real problem is scheduling.

So the split is asymmetric and it is a hard rule:

**Weekday evenings (1 hr × 5) — medium/low load**
- C++ drilling, exercises, small refactors
- Reading (books, papers, blogs)
- Spaced repetition review
- One 15-min English recording per week (from Week 14)

**Weekend blocks (2–3 hrs × 2) — high load, the only slot for hard things**
- New mathematics
- Microstructure theory
- Project design and the hard parts of implementation
- Benchmarking and analysis

C++ drilling is the one technical thing that genuinely works at 8pm — muscle memory, not insight. That partly rescues the weekday hour, and it is a real argument in favour of the C++ pivot.

---

## Phase 0 — Calibration (Weeks 1–2)

**Goal:** know my actual starting point, and remove every excuse for friction later.

- Sit [DIAGNOSTIC.md](DIAGNOSTIC.md) closed-book and timed. Score honestly. Record the score in the log.
- Second pass with notes on everything missed. Record that score too. The **gap between the two** is the number that matters.
- Set the math block length from the scoring table in the diagnostic.
- Toolchain: clang/gcc, CMake, a debugger, GoogleTest or Catch2, Google Benchmark, sanitizers (ASan/UBSan/TSan), Compiler Explorer bookmarked.
- First log entry committed.
- Start reading Harris, *Trading and Exchanges*, ch. 1–3. Pure background reading, no notes pressure.

**Exit:** two diagnostic scores in the log, a `hello world` that builds under CMake with a passing test and a clean ASan run.

---

## Phase 1 — Foundations (Weeks 3–14)

Two tracks, running in parallel. This is the phase people quit in, so it is deliberately unglamorous and deliberately measurable.

**Weekends — mathematics.** Length set by the diagnostic (4 / 8 / 12 / 16 weeks). Priority order, because this is a microstructure plan and not a derivatives plan:

1. **Probability** — the working mathematics of this whole field, and the piece physics undergrads are reliably weakest at. Random variables, expectation, conditional expectation and the tower property, common distributions, LLN and CLT, random walks, martingales.
2. **Statistics** — estimators, bias/variance, hypothesis testing, confidence intervals, regression. Enough to not fool myself with a backtest.
3. **Linear algebra refresh** — eigen-decomposition, PSD matrices, covariance, SVD. Fast, it comes back quickly.
4. **Calculus refresh** — targeted only. Look up what breaks, don't re-take the course.

**Weekdays — C++ from zero.** `learncpp.com` front to back is the spine. Then *A Tour of C++*.

Non-negotiable habits from day one, because these are what actually separate a professional from a hobbyist:
- Every project builds with CMake
- Every non-trivial function has a test
- ASan and UBSan run in CI from the very first commit
- No raw `new`/`delete` — RAII, smart pointers, value semantics

**Week 14:** English recording track begins. 15 minutes, once a week, unscripted, explaining a technical decision out loud. Listen back. The first ten will be painful; that is the point.

**Milestone M1 (Week 14)**
- Retake the diagnostic. Target ≥85% closed-book.
- Write a small C++ program (a CSV parser, an LRU cache, something ordinary) that is RAII-correct, tested, ASan-clean, and reviewed by me a week later without embarrassment.
- Committed to the repo.

---

## Phase 2 — C++ depth + market mechanics (Weeks 15–30)

**Weekdays — modern C++ that a trading firm cares about.**
- Move semantics, perfect forwarding, value categories
- Templates, and enough of the STL's internals to reason about allocation
- *Effective Modern C++*, Meyers
- *C++ Concurrency in Action*, Williams — memory model, atomics, lock-free basics. My Java threading experience transfers conceptually and misleads in the details; expect that.
- CppCon "Back to Basics" talks on weekday evenings when too tired to code

**Weekends — how markets actually work.**
- Harris, *Trading and Exchanges*, properly this time. This is the single most important book in the plan.
- Order types, matching rules, price-time priority, auctions, halts
- Market makers, liquidity, adverse selection, the bid-ask spread and what it is compensation for
- Exchange protocols: read an actual ITCH and an actual FIX specification
- IDX's own rulebook and microstructure — this is a genuine local edge in Jakarta interviews that no imported curriculum will give me
- Gould et al., *Limit Order Books* (arXiv survey) — read it twice

**Milestone M2 (Week 26) — exit criterion γ**

Publish a 2,000-word explainer: *what actually happens when a retail equity order is submitted, from click to settlement*. Order routing, the book, matching, priority, fees, clearing. Public, in English, in this repo.

If I cannot write that without looking things up constantly, I do not understand markets yet and Phase 3 waits.

**Week 34 — the C++ off-ramp checkpoint.** Honest question: is C++ still mud? If yes, switch to JVM-first, target banks/exchanges/asset-manager platform teams, and add C++ later from inside a job. This is a planned branch, not a failure.

---

## Phase 3 — Flagship: limit order book + matching engine (Weeks 31–52)

The project that makes a recruiter open my GitHub. Also my C++ learning vehicle — I stop doing exercises and start doing engineering.

Built in versions, each one shipped and tagged:

**v0 (Weeks 31–35) — naive and correct.** `std::map` of price levels, FIFO queues, limit and market orders, cancels. Ugly and right.

**v1 (Weeks 36–41) — trustworthy.** Property-based tests, invariant checking (book always crossed-free, quantities conserved), replay of a recorded session, deterministic and reproducible. **This is the version that matters.** Anyone can write a fast wrong book.

**v2 (Weeks 42–47) — measured.** Google Benchmark. Latency percentiles, not averages — p50, p99, p99.9. Throughput under realistic message mixes. Publish the numbers *before* optimizing, so the improvement is provable.

**v3 (Weeks 48–52) — optimized.** Intrusive lists, arena allocation, cache-friendly layouts, branch prediction, avoiding allocation on the hot path. Every optimization justified by a measurement, and every one written up.

**Weekday reading:** Agner Fog's optimization manuals, Carl Cook's *When a Microsecond Is an Eternity*, `perf`/Instruments profiling.

**From Week 36 (~month 9): begin applying for stepping-stone roles.** Fintech backend, bank analytics/risk engineering, broker platform teams, exchange technology, data engineering at an asset manager. Low effort, ongoing, in the background. Any pay. Being inside the industry beats being outside it with better notes.

**Milestone M3 (Week 52)** — one year in. The engine handles a replayed real trading day, passes property tests, and has published latency percentiles with a before/after optimization write-up.

---

## Phase 4 — Live data + book reconstruction (Weeks 53–68)

Real data, real production pressure, no permission needed and no money spent.

- WebSocket feed handler in C++ against a crypto venue's L2 stream. Crypto because it is the only free full-depth real-time market data on earth. The CV says equities; nobody cares which venue's bytes the engine parsed.
- Order book reconstruction from incremental updates
- The things that actually bite: sequence gaps, out-of-order messages, reconnection and resnapshotting, clock skew, backpressure
- Cross-validate reconstructed books against exchange snapshots — an automated correctness check, running continuously
- Feed the reconstructed stream into the Phase 3 engine

**Milestone M4 (Week 68) — exit criterion β**

Flagship is shipped, documented, benchmarked, and written up publicly. A README a stranger can read in five minutes and understand what was built and why it is good. Applications now go out with a link attached instead of a hope.

---

## Phase 5 — Exchange simulator + execution algorithms (Weeks 69–88)

The capstone, and the strongest interview story in the plan.

- Extend the matching engine into a **realistic exchange simulator**: latency modelling (network + matching + response), queue position tracking, fee/rebate tiers, partial fills, order rejects
- Implement execution algorithms against it: **TWAP, VWAP, POV, implementation shortfall**
- Measure them properly: slippage vs arrival price, market impact, fill rates, queue position decay
- Read Almgren–Chriss and implement the optimal execution schedule. Compare it to the naive algorithms and explain the difference in my own words.
- Weekend reading: Cartea/Jaimungal/Penalva (selectively), Hasbrouck. Plus **derivatives literacy** — Hull chapters 1–15, enough to discuss options, greeks and hedging credibly. Not enough to price exotics, and that is deliberate.

**Milestone M5 (Week 88)** — a public write-up: *"I built an exchange simulator with realistic queue dynamics and measured four execution algorithms against it."* That sentence opens doors at prop shops and at buy-side execution desks alike.

---

## Phase 6 — Conversion (Weeks 89–104)

Study stops being the point. Getting hired becomes the point.

**Weekdays**
- C++ interview questions, hard ones — object lifetime, virtual dispatch cost, memory model, undefined behaviour
- Concurrency problems
- LeetCode medium, in C++, timed. Not grinding for its own sake — for fluency under pressure.
- Probability puzzles: *Heard on the Street*, the Green Book

**Weekends**
- Systems design practice, framed around trading systems
- Mock interviews in English. Record every one. This is where the Week 14 recording habit pays off.
- Rewrite the CV around the projects, not the years
- Applications at volume: prop shops, exchanges, banks, brokers, asset managers, Singapore and remote

**Milestone M6 (Week 104) — exit criterion α**

Passing technical screens. Not necessarily an offer — offers depend on luck and timing — but the screen is a skill test, and passing it is the thing actually under my control.

---

## The weekly rhythm

- **Mon–Fri, 1 hr** — C++ practice, or reading, or (one day a week) a 15-minute English recording
- **Saturday, 2–3 hrs** — the hard block. New mathematics or hard project work. Never admin.
- **Sunday, 2–3 hrs** — project work, then **write the log entry and commit it**

The Sunday commit is the only truly non-negotiable item in this document.

---

## Monthly checkpoint protocol

Last Sunday of every month, answer five questions in the log:

1. Hours actually spent, versus ~44 planned.
2. Is the current milestone on track, ahead, or behind?
3. What was hard in a way I did not expect?
4. What should be **dropped**?
5. Is the C++ pivot still the right call?

**Question 4 is the important one.** A plan without a mechanism for cutting scope is a plan that gets abandoned wholesale instead of trimmed.

**Rescope triggers:**
- 3 consecutive missed log entries → the plan is wrong, rewrite it, do not "try harder"
- A milestone more than 6 weeks late → cut scope from the *next* phase, do not compress
- Week 34: the C++ off-ramp decision
- A stepping-stone job offer at any point → **take it**, and rebuild this plan around having less time and vastly better information

---

## What is deliberately not in this plan

Named so that leaving them out is a decision rather than an oversight:

- **Stochastic calculus beyond literacy.** Shreve Volume 2, measure theory, PDE methods for exotics. Wrong specialization, and it would eat six months.
- **Machine learning / alpha research.** That is the quant *researcher* path. Deliberately not my target.
- **Certifications — CQF and similar.** For a quant developer, shipped code beats certificates, and the money is not there anyway.
- **A master's degree, for now.** Revisit once inside the industry, ideally employer-sponsored or scholarship-funded.
- **Crypto as a career target.** Data source only.
- **Breadth.** At ~5 hours of new-concept capacity per week, going wide means arriving at Week 104 with nothing anyone will pay for.
