# Tower of Hanoi

The Tower of Hanoi game consists of three stacks (left, middle and right) and `n` round disks of different sizes. Initially, the left stack has all the disks, in increasing order of size from top to bottom.

The goal is to move all the disks to the right stack using the middle stack. On each move you can move the uppermost disk from one stack to another. It is not allowed to place a larger disk on a smaller disk.

Your task is to find a solution that minimizes the number of moves.

## Input

The only input line has an integer `n`: the number of disks.

## Output

First print an integer `k`: the minimum number of moves.

After this, print `k` lines that describe the moves. Each line has two integers `a` and `b`: you move a disk from stack `a` to stack `b`. The stacks are numbered 1 (left), 2 (middle) and 3 (right).

## Constraints

- 1 ≤ n ≤ 16

## Example

**Input:**
```
2
```

**Output:**
```
3
1 2
1 3
2 3
```

---

*Adapted from [Tower of Hanoi](https://cses.fi/problemset/task/2165) in the [CSES Problem Set](https://cses.fi/problemset/) by Antti Laaksonen, licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Changes: statement edited; test cases are our own.*
