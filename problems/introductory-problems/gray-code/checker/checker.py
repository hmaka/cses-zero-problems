# Checker for Gray Code: any list of all 2^n n-bit strings where successive ones differ in one bit.
# Runs in Python 3.8. See the README's checker/ contract.


def check(input, output, answer):
    n = int(input)
    codes = output.split()
    if len(codes) != 1 << n:
        return False, "expected %d strings, got %d" % (1 << n, len(codes))
    for i, c in enumerate(codes):
        if len(c) != n or set(c) - set("01"):
            return False, "line %d is not a %d-bit string: %s" % (i + 1, n, c[:40])
    if len(set(codes)) != len(codes):
        return False, "some bit string appears twice"
    for i in range(len(codes) - 1):
        a, b = codes[i], codes[i + 1]
        if sum(x != y for x, y in zip(a, b)) != 1:
            return False, "lines %d and %d (%s, %s) differ in more than one bit" % (i + 1, i + 2, a, b)
    return True, ""
