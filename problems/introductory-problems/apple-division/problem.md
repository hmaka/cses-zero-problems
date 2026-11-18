# Apple Division

There are `n` apples with known weights. Your task is to divide the apples into two groups so that the difference between the weights of the groups is minimal.

## Input

The first input line has an integer `n`: the number of apples.

The next line has `n` integers `p_1, p_2, ..., p_n`: the weight of each apple.

## Output

Print one integer: the minimum difference between the weights of the groups.

## Constraints

- 1 ≤ n ≤ 20
- 1 ≤ p_i ≤ 10^9

## Example

**Input:**
```
5
3 2 7 4 1
```

**Output:**
```
1
```

One way: the first group has weights 2, 3 and 4 (total 9), and the second has 1 and 7 (total 8).

---

*Adapted from [Apple Division](https://cses.fi/problemset/task/1623) in the [CSES Problem Set](https://cses.fi/problemset/) by Antti Laaksonen, licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Changes: statement edited; test cases are our own.*
