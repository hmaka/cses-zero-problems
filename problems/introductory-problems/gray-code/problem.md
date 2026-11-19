# Gray Code

A Gray code is a list of all `2^n` bit strings of length `n`, where any two successive strings differ in exactly one bit (their Hamming distance is one).

Your task is to create a Gray code for a given length `n`.

## Input

The only input line has an integer `n`.

## Output

Print `2^n` lines that describe the Gray code. You may print any valid solution.

## Constraints

- 1 ≤ n ≤ 16

## Example

**Input:**
```
2
```

**Output:**
```
00
01
11
10
```

---

*Adapted from [Gray Code](https://cses.fi/problemset/task/2205) in the [CSES Problem Set](https://cses.fi/problemset/) by Antti Laaksonen, licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Changes: statement edited; test cases from CSES.*
