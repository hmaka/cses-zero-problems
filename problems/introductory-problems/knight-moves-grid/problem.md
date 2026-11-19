# Knight Moves Grid

There is a knight on an `n × n` chessboard. For each square, print the minimum number of moves the knight needs to reach the top-left corner.

## Input

The only line has an integer `n`.

## Output

Print `n` lines, each with `n` integers: the number of moves for each square.

## Constraints

- 4 ≤ n ≤ 1000

## Example

**Input:**
```
8
```

**Output:**
```
0 3 2 3 2 3 4 5
3 4 1 2 3 4 3 4
2 1 4 3 2 3 4 5
3 2 3 2 3 4 3 4
2 3 2 3 4 3 4 5
3 4 3 4 3 4 5 4
4 3 4 3 4 5 4 5
5 4 5 4 5 4 5 6
```

---

*Adapted from [Knight Moves Grid](https://cses.fi/problemset/task/3217) in the [CSES Problem Set](https://cses.fi/problemset/) by Antti Laaksonen, licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Changes: statement edited; test cases from CSES.*
