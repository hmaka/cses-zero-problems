# Checker for Two Sets: any split of 1..n into two sets with equal sums.
# Runs in Python 3.8. See the README's checker/ contract.


def read_set(tokens, pos, name):
    k = int(tokens[pos])
    items = [int(x) for x in tokens[pos + 1:pos + 1 + k]]
    if len(items) != k:
        raise ValueError("%s set says %d elements but the output ends early" % (name, k))
    return k, items, pos + 1 + k


def check(input, output, answer):
    n = int(input)
    want = answer.split()[0]
    t = output.split()
    if not t or t[0] not in ("YES", "NO"):
        return False, "output must start with YES or NO"
    if t[0] != want:
        return False, "expected %s" % want
    if want == "NO":
        return len(t) == 1, "nothing may follow NO"

    k1, a, pos = read_set(t, 1, "first")
    k2, b, pos = read_set(t, pos, "second")
    if pos != len(t):
        return False, "unexpected extra output after the second set"
    seen = set(a) | set(b)
    if k1 + k2 != n or len(seen) != n or seen != set(range(1, n + 1)):
        return False, "the two sets must contain each of 1..%d exactly once" % n
    if sum(a) != sum(b):
        return False, "set sums differ: %d vs %d" % (sum(a), sum(b))
    return True, ""
