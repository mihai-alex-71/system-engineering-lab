# Exercise 1 – Ishikawa diagram for the Fibonacci calculator

Fishbone: `fishbone.drawio` (open in draw.io / app.diagrams.net) and `fishbone.png` (image export).

## Test results

Convention used: F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2).

| Input | Program shows | Correct F(n) | OK? | Problem |
|---|---|---|---|---|
| 0 | F(0) = 1 | 0 | No | Wrong base case |
| 1 | F(1) = 1 | 1 | Yes | – |
| 15 | F(15) = 610 | 610 | Yes | – |
| 23 | F(23) = 28657 | 28657 | Yes | – |
| 50 | F(50) = -298632863 | 12586269025 | No | 32-bit overflow (12586269025 mod 2^32, read as signed int) |
| 98 | F(98) = -90618175 | 135301852344706746049 | No | Overflow, negative result |
| -5 | F(-5) = 0 | undefined for this program (should be rejected) | No | No validation of negative input |
| 2.5 | F(2) = 1 | not an integer (should be rejected) | No | Input silently truncated |
| abc | F(NaN) = 0 | invalid input (error message expected) | No | NaN shown as a result |
| 12abc | F(12) = 144 | invalid input (error message expected) | No | Partial parse accepted |
| (empty) | F(NaN) = 0 | invalid input (error message expected) | No | No check for empty input |

**Summary:** only 3 of 11 inputs give a correct, expected result.

## Observations

- **Correctness:** wrong base case for n = 0. Wrong (negative) values from n = 47, because
  F(47) = 2 971 215 073 is greater than the largest 32-bit signed integer (2 147 483 647).
- **Ease of use:** there are no error messages. Invalid input produces `F(NaN) = 0`, which looks like
  a valid result.
- **Source code:** the outputs show the code uses `parseInt` (2.5 → 2, "12abc" → 12) and
  32-bit integer arithmetic. The `-298632863` value is exactly F(50) wrapped to a signed 32-bit integer.
- **User expectations:** a user expects either the exact value (`BigInt`) or a clear
  "n must be an integer between 0 and N" message. The program shows neither.

## Fixes suggested

1. Use `BigInt`, or limit n to 0..78 (the largest value exactly representable as a JS Number).
2. Fix the base case: F(0) = 0.
3. Validate input with `Number.isInteger(Number(s))` and `n >= 0`, and show an error message otherwise.
4. Add unit tests for 0, 1, negative values, decimals, text, empty input and large n.
