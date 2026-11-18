# Checker for Raab Game I: for each test, YES/NO must match, and a YES game must be two
# permutations of 1..n in which player 1 wins a rounds and player 2 wins b rounds.
# Runs in Python 3.8. See the README's checker/ contract.


def check(input, output, answer):
    v = [int(x) for x in input.split()]
    tests = [v[1 + 3 * i:4 + 3 * i] for i in range(v[0])]
    out, ans = output.split(), answer.split()
    po = pa = 0
    for i, (n, a, b) in enumerate(tests, 1):
        want = ans[pa]
        pa += 1 + (2 * n if want == "YES" else 0)
        if po >= len(out):
            return False, "test %d: output ended early" % i
        got = out[po]
        po += 1
        if got not in ("YES", "NO"):
            return False, "test %d: expected YES or NO, got %s" % (i, got[:20])
        if got != want:
            return False, "test %d (n=%d, a=%d, b=%d): expected %s" % (i, n, a, b, want)
        if got == "NO":
            continue
        cards = [int(x) for x in out[po:po + 2 * n]]
        po += 2 * n
        if len(cards) != 2 * n:
            return False, "test %d: expected two lines of %d cards" % (i, n)
        p, q = cards[:n], cards[n:]
        for who, hand in (("player 1", p), ("player 2", q)):
            if sorted(hand) != list(range(1, n + 1)):
                return False, "test %d: %s's cards are not a permutation of 1..%d" % (i, who, n)
        sa = sum(x > y for x, y in zip(p, q))
        sb = sum(y > x for x, y in zip(p, q))
        if (sa, sb) != (a, b):
            return False, "test %d: that game scores %d-%d, not %d-%d" % (i, sa, sb, a, b)
    if po != len(out):
        return False, "unexpected extra output after the last test"
    return True, ""
