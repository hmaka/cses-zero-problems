# Two Sets

Your task is to divide the numbers `1, 2, ..., n` into two sets of equal sum.

## Input

The only input line contains an integer `n`.

## Output

Print `YES` if the division is possible, and `NO` otherwise.

If the division is possible, then also print an example of how to create the sets. First print the number of elements in the first set, followed by its elements on a separate line. Then print the second set in the same way. If there are several divisions, you may print any of them.

## Constraints

- 1 ≤ n ≤ 10^5

## Examples

**Input:**
```
7
```

**Output:**
```
YES
4
1 2 4 7
3
3 5 6
```

**Input:**
```
6
```

**Output:**
```
NO
```

---

*Adapted from [Two Sets](https://cses.fi/problemset/task/1092) in the [CSES Problem Set](https://cses.fi/problemset/) by Antti Laaksonen, licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Changes: statement edited; smaller maximum n; test cases are our own.*
