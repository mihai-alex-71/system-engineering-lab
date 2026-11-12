# Exercise 3 – Defect density

| Module | Defects | LOC | Defect density |
|---|---|---|---|
| M3 | 25 | 5 | 5.00 |
| M1 | 40 | 20 | 2.00 |
| M4 | 10 | 10 | 1.00 |
| M8 | 5 | 5 | 1.00 |
| M9 | 7 | 10 | 0.70 |
| M10 | 14 | 20 | 0.70 |
| M2 | 15 | 30 | 0.50 |
| M5 | 8 | 20 | 0.40 |
| M7 | 10 | 30 | 0.33 |
| M6 | 4 | 20 | 0.20 |

Chart: `defect_density_chart.png`

**Most defects vs highest density.** M1 has the most defects in absolute terms (40), but M3 has the
highest density (5 defects per line, 2.5x more than M1) even though it has only 25 defects. Counting
defects alone favours large modules; density shows where the code is actually of poor quality.

**Where we'd put the next testing effort.** First in M3: it is small (5 LOC), so reviewing / rewriting it
is cheap, and with 5 defects/LOC almost every line is wrong, so it is the riskiest module.
Then M1 (2.0, and the largest number of defects that could reach users), then M4 and M8 (1.0).
M6, M7 and M5 are under 0.5 and can stay at regular testing.
