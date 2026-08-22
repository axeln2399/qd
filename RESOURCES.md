# Resources

Mapped to the phase that uses them. **Free/online sources marked ⭑** — this plan assumes no budget.

Rule: **one primary source per topic at a time.** Collecting resources is procrastination that feels like progress.

---

## Mathematics (Phase 1, weekends)

### Probability — the priority
- ⭑ **Blitzstein & Hwang, *Introduction to Probability*** — free PDF, and the Harvard **Stat 110** lecture videos are on YouTube. This is *the* book. Conditional expectation and the tower property are taught better here than anywhere.
- ⭑ Stat 110 problem sets and solutions — do the problems, not just the videos.

### Statistics
- **Wasserman, *All of Statistics*** — concise, assumes mathematical maturity, exactly right for a physics graduate. Chapters 6–13.
- ⭑ **Hyndman & Athanasopoulos, *Forecasting: Principles and Practice*** — free online. For time series, skip Tsay until actually needed.

### Linear algebra (refresh, fast)
- ⭑ **3Blue1Brown, *Essence of Linear Algebra*** — for rebuilding intuition in a weekend.
- ⭑ **MIT 18.06, Strang** — reference, not a full re-watch.

### Calculus (refresh, targeted only)
- ⭑ **Paul's Online Math Notes** — look up what breaks. Do not re-take the course.

### Stochastic calculus — literacy only
- **Shreve, *Stochastic Calculus for Finance I*** (the binomial volume). **Volume II is explicitly out of scope.**

---

## C++ (Phases 1–3, weekday evenings)

### Learning, in order
1. ⭑ **learncpp.com** — free, structured, current. Front to back. This is the spine.
2. **Stroustrup, *A Tour of C++* (3rd ed.)** — short, dense, after learncpp.
3. **Meyers, *Effective Modern C++*** — Phase 2. Read one item per evening.
4. **Williams, *C++ Concurrency in Action* (2nd ed.)** — Phase 2. The memory model chapter is the important one, and JVM instincts will actively mislead here.
5. **Guntheroth, *Optimized C++*** and ⭑ **Agner Fog's optimization manuals** — Phase 3 only, once there is something to measure.

### Talks (weekday evenings, too tired to code)
- ⭑ **CppCon "Back to Basics" series** — the best free structured C++ content available.
- ⭑ **Carl Cook, *When a Microsecond Is an Eternity*** (CppCon) — the low-latency trading classic. Watch it twice.
- ⭑ **Chandler Carruth on performance and data structures**

### Tools — set up in Phase 0
- ⭑ CMake · GoogleTest or Catch2 · Google Benchmark
- ⭑ ASan / UBSan / TSan — enabled from the first commit, not retrofitted
- ⭑ **Compiler Explorer** (godbolt.org) — for actually seeing what the compiler does
- ⭑ `perf` (Linux) / Instruments (macOS)
- ⭑ clang-tidy, clang-format

### Practice
- ⭑ **exercism.org C++ track** — for the first weeks
- ⭑ **Advent of Code in C++** — good weekday evening drilling
- After Week 31, the flagship project *is* the practice. Stop doing exercises.

---

## Market microstructure (Phase 2 onward, weekends)

### The core
- **Harris, *Trading and Exchanges: Market Microstructure for Practitioners*** — the single most important book in this plan. Readable, non-mathematical, and it is what practitioners actually mean when they say someone "understands markets."
- ⭑ **Gould et al., *Limit Order Books*** (arXiv survey) — read it twice, at the start and end of Phase 2.

### Deeper
- **Cartea, Jaimungal & Penalva, *Algorithmic and High-Frequency Trading*** — mathematical. Selective reading in Phase 5.
- ⭑ **Bouchaud, Bonart, Donier & Gould, *Trades, Quotes and Prices*** — excellent, advanced, draft chapters circulate freely.
- **Hasbrouck, *Empirical Market Microstructure*** — for the measurement side.
- ⭑ **Almgren & Chriss, *Optimal Execution of Portfolio Transactions*** — the execution paper. Implemented in Phase 5.

### Protocols and real specs — read actual documents, not summaries
- ⭑ **NASDAQ TotalView-ITCH specification** — publicly available
- ⭑ **FIX protocol specification**
- ⭑ **IDX (Bursa Efek Indonesia) rulebook and trading regulations** — the local edge. No imported curriculum covers Jakarta's microstructure, and every local interview will.

### Blogs and ongoing reading (weekday evenings)
- ⭑ Databento blog — genuinely good on market data mechanics
- ⭑ Mechanical Markets
- ⭑ Quantitative Brokers / Proof Trading research posts
- ⭑ r/quant, QuantNet forums, Wilmott — for sensing the market, not for learning

---

## Derivatives — literacy only (Phase 5)

- **Hull, *Options, Futures and Other Derivatives*** — chapters 1–15 only. Enough to discuss options, greeks and hedging credibly in an interview. Deliberately not enough to price exotics.

---

## Systematic infrastructure — secondary (Phase 5, light)

- **López de Prado, *Advances in Financial Machine Learning*** — read the chapters on backtest overfitting and cross-validation pitfalls. Read the rest sceptically.
- ⭑ Anything on look-ahead bias, survivorship bias, and multiple-testing in backtests.

---

## Data sources — all free

- ⭑ **Binance / OKX / Coinbase WebSocket L2 feeds** — the only free full-depth real-time order book data available to an individual. This is why crypto is in the plan as data.
- ⭑ **LOBSTER sample data** — free sample days of reconstructed NASDAQ limit order books. Perfect for validating the Phase 3 engine against ground truth.
- ⭑ **NASDAQ ITCH sample files** — raw protocol data.
- ⭑ **Yahoo Finance / Stooq** — daily equity bars. Fine for the secondary track, useless for order book work.
- ⭑ **IDX website** — daily summaries and market statistics.

---

## Interview preparation (Phase 6)

- **Crack, *Heard on the Street*** — the classic brainteaser and probability book.
- **Zhou, *A Practical Guide to Quantitative Finance Interviews*** — "the green book."
- **Joshi, *Quant Job Interview Questions and Answers*** — more C++/implementation flavoured, which suits a QD target.
- **Kleppmann, *Designing Data-Intensive Applications*** — for systems design rounds. Likely already familiar; skim rather than read.
- ⭑ LeetCode — medium difficulty, in C++, timed. For fluency under pressure, not for grinding.

---

## English speaking (weekly, from Week 14)

No resource needed. **15 minutes, once a week, recorded:** pick a technical decision made that week, explain it out loud unscripted as if to an interviewer, then listen back.

The listening back is the entire exercise. It will be uncomfortable for roughly ten weeks and then it will not be.

---

## Deliberately excluded

- **CQF, and all paid certifications** — for a quant developer, shipped code beats certificates.
- **Shreve Volume II, measure-theoretic probability** — wrong specialization, six-month cost.
- **Machine learning courses** — that is the researcher path.
- **Paid market data** — everything above is free, and free is sufficient for everything in this plan.
- **Python-based "quant finance" bootcamps and Udemy courses** — the target is quant *developer*. Systems engineering in C++ is the differentiator; another pandas tutorial is not.
