# Permutations

A permutation of the integers `1, 2, ..., n` is called *beautiful* if no two adjacent elements differ by exactly 1.

Given `n`, construct a beautiful permutation, if one exists.

## Input

The only input line contains an integer `n`.

## Output

Print a beautiful permutation of `1, 2, ..., n`, with the numbers separated by spaces. If there are several, you may print any of them. If none exists, print `NO SOLUTION`.

## Constraints

- 1 ≤ n ≤ 10^5

## Examples

**Input:**
```
5
```

**Output:**
```
4 2 5 3 1
```

**Input:**
```
3
```

**Output:**
```
NO SOLUTION
```

---

*Adapted from [Permutations](https://cses.fi/problemset/task/1070) in the [CSES Problem Set](https://cses.fi/problemset/) by Antti Laaksonen, licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Changes: statement edited; smaller maximum n; test cases are our own.*
