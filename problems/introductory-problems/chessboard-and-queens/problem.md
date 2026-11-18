# Chessboard and Queens

Your task is to place eight queens on a chessboard so that no two queens attack each other. As an additional challenge, each square is either free or reserved, and you can only place queens on free squares. The reserved squares do not prevent queens from attacking each other.

How many possible ways are there to place the queens?

## Input

The input has eight lines, and each of them has eight characters. Each square is either free (`.`) or reserved (`*`).

## Output

Print one integer: the number of ways you can place the queens.

## Example

**Input:**
```
........
........
..*.....
........
........
.....**.
...*....
........
```

**Output:**
```
65
```

---

*Adapted from [Chessboard and Queens](https://cses.fi/problemset/task/1624) in the [CSES Problem Set](https://cses.fi/problemset/) by Antti Laaksonen, licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Changes: statement edited; test cases are our own.*
