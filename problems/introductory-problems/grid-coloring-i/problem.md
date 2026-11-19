# Grid Coloring I

You are given an `n × m` grid where each cell contains one of the characters `A`, `B`, `C` or `D`.

For each cell, you must change the character to `A`, `B`, `C` or `D`. The new character must be different from the old one.

Your task is to change the characters in every cell so that no two adjacent cells have the same character.

## Input

The first line has two integers `n` and `m`: the number of rows and columns.

The next `n` lines each have `m` characters: the description of the grid.

## Output

Print `n` lines, each with `m` characters: the description of the final grid. You may print any valid solution.

If no solution exists, print `IMPOSSIBLE`.

## Constraints

- 1 ≤ n, m ≤ 500

## Example

**Input:**
```
3 4
AAAA
BBBB
CCDD
```

**Output:**
```
CDCD
DCDC
ABAB
```

---

*Adapted from [Grid Coloring I](https://cses.fi/problemset/task/3311) in the [CSES Problem Set](https://cses.fi/problemset/) by Antti Laaksonen, licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Changes: statement edited; test cases from CSES.*
