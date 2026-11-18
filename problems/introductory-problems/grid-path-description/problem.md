# Grid Path Description

There are 88418 paths in a `7 × 7` grid that start at the upper-left square, end at the lower-left square, and visit every square exactly once. Each path corresponds to a 48-character description of its moves: `D` (down), `U` (up), `L` (left) and `R` (right).

For example, the description `DRURRRRRDDDLUULDDDLDRRURDDLLLLLURULURRUULDLLDDDD` is one such path.

You are given a description of a path that may also contain the character `?` (any direction). Your task is to calculate the number of paths that match the description.

## Input

The only input line has a 48-character string of the characters `?`, `D`, `U`, `L` and `R`.

## Output

Print one integer: the number of matching paths.

## Example

**Input:**
```
??????R??????U??????????????????????????LD????D?
```

**Output:**
```
201
```

---

*Adapted from [Grid Path Description](https://cses.fi/problemset/task/1625) in the [CSES Problem Set](https://cses.fi/problemset/) by Antti Laaksonen, licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Changes: statement edited; time limit raised to 2 s for our slower judge hardware; test cases are our own.*
