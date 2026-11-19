# Creating Strings

Given a string, your task is to generate all different strings that can be created using its characters.

## Input

The only input line has a string of length `n`. Each character is between `a` and `z`.

## Output

First print an integer `k`: the number of strings. Then print `k` lines: the strings in alphabetical order.

## Constraints

- 1 ≤ n ≤ 8

## Example

**Input:**
```
aabac
```

**Output:**
```
20
aaabc
aaacb
aabac
aabca
aacab
aacba
abaac
abaca
abcaa
acaab
acaba
acbaa
baaac
baaca
bacaa
bcaaa
caaab
caaba
cabaa
cbaaa
```

---

*Adapted from [Creating Strings](https://cses.fi/problemset/task/1622) in the [CSES Problem Set](https://cses.fi/problemset/) by Antti Laaksonen, licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Changes: statement edited; test cases from CSES.*
