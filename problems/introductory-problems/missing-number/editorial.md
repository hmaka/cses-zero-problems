# Editorial: Missing Number

## Idea

The numbers `1..n` have a known sum, `n(n + 1) / 2`. If exactly one number is missing,
the input sums to that total minus the missing number. So:

```
missing = n(n + 1) / 2 - (sum of the input)
```

This is **O(n)** time and **O(1)** extra memory, with no sorting and no hash set.

## Pitfall

With `n = 2 · 10^5` the total is about `2 · 10^10`, which overflows a 32-bit integer.
Use 64-bit integers (`long long` in C++, `long` in Java).

## Alternative

XOR all of `1..n` together with all of the input numbers. Every number that appears twice cancels
out, which leaves only the missing one. This avoids overflow entirely.

## Reference (C++)

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    long long n; cin >> n;
    long long sum = 0;
    for (int i = 0; i < n - 1; i++) { long long x; cin >> x; sum += x; }
    cout << n * (n + 1) / 2 - sum << "\n";
}
```
