# Mex Grid Construction

Your task is to construct an `n × n` grid where each square holds the smallest nonnegative integer that does not appear to its left on the same row or above it in the same column.

## Input

The only line has an integer `n`.

## Output

Print the grid: `n` lines, each with `n` integers separated by spaces.

## Constraints

- 1 ≤ n ≤ 100

## Example

**Input:**
```
5
```

**Output:**
```
0 1 2 3 4
1 0 3 2 5
2 3 0 1 6
3 2 1 0 7
4 5 6 7 0
```

---

*Adapted from [Mex Grid Construction](https://cses.fi/problemset/task/3419) in the [CSES Problem Set](https://cses.fi/problemset/) by Antti Laaksonen, licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Changes: statement edited; test cases are our own.*
