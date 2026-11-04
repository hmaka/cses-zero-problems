# Checker for Permutations: any beautiful permutation is accepted.
# Runs in Python 3.8. See the README's checker/ contract.


def check(input, output, answer):
    n = int(input)
    if answer.strip() == "NO SOLUTION":
        return output.strip() == "NO SOLUTION", "expected NO SOLUTION"
    if output.strip() == "NO SOLUTION":
        return False, "printed NO SOLUTION, but a beautiful permutation exists"

    p = [int(t) for t in output.split()]
    if len(p) != n:
        return False, "expected %d numbers, got %d" % (n, len(p))
    if sorted(p) != list(range(1, n + 1)):
        return False, "not a permutation of 1..%d" % n
    for i in range(n - 1):
        if abs(p[i] - p[i + 1]) == 1:
            return False, "positions %d and %d hold %d and %d, which differ by 1" % (i + 1, i + 2, p[i], p[i + 1])
    return True, ""
