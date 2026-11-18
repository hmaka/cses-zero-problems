# Checker for Grid Coloring I: every cell changed to A-D, and no two adjacent cells equal.
# (A solution always exists, so the reference answer never says IMPOSSIBLE.)
# Runs in Python 3.8. See the README's checker/ contract.


def check(input, output, answer):
    t = input.split()
    n, m = int(t[0]), int(t[1])
    g = t[2:2 + n]
    h = output.split()
    if answer.strip() == "IMPOSSIBLE":
        return h == ["IMPOSSIBLE"], "expected IMPOSSIBLE"
    if h == ["IMPOSSIBLE"]:
        return False, "printed IMPOSSIBLE, but a coloring exists"
    if len(h) != n:
        return False, "expected %d rows, got %d" % (n, len(h))
    for i in range(n):
        row = h[i]
        if len(row) != m:
            return False, "row %d has %d characters, expected %d" % (i + 1, len(row), m)
        for j in range(m):
            c = row[j]
            if c not in "ABCD":
                return False, "row %d, column %d: %r is not one of A-D" % (i + 1, j + 1, c)
            if c == g[i][j]:
                return False, "row %d, column %d still has %s" % (i + 1, j + 1, c)
            if j + 1 < m and c == row[j + 1]:
                return False, "row %d: columns %d and %d are both %s" % (i + 1, j + 1, j + 2, c)
            if i + 1 < n and c == h[i + 1][j:j + 1]:
                return False, "column %d: rows %d and %d are both %s" % (j + 1, i + 1, i + 2, c)
    return True, ""
