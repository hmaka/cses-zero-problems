# Weird Algorithm

Consider an algorithm that takes as input a positive integer `n`. If `n` is even, the algorithm divides it by two, and if `n` is odd, the algorithm multiplies it by three and adds one. The algorithm repeats this, until `n` is one.

Your task is to simulate the execution of the algorithm for a given value of `n`.

## Input

The only input line contains an integer `n`.

## Output

Print a line that contains all values of `n` during the algorithm, separated by spaces.

## Constraints

- 1 ≤ n ≤ 10^6

## Example

**Input:**

```
3
```

**Output:**

```
3 10 5 16 8 4 2 1
```

---

*Adapted from [Weird Algorithm](https://cses.fi/problemset/task/1068) in the [CSES Problem Set](https://cses.fi/problemset/) by Antti Laaksonen, licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Changes: statement edited; test cases are our own.*
