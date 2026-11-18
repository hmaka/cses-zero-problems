# Checker for Palindrome Reorder: any palindrome using exactly the input's letters.
# Runs in Python 3.8. See the README's checker/ contract.
from collections import Counter


def check(input, output, answer):
    s = input.strip()
    out = output.strip()
    if answer.strip() == "NO SOLUTION":
        return out == "NO SOLUTION", "expected NO SOLUTION"
    if out == "NO SOLUTION":
        return False, "printed NO SOLUTION, but a palindrome exists"
    if len(out.split()) != 1:
        return False, "print the palindrome as a single string"
    if len(out) != len(s):
        return False, "expected %d characters, got %d" % (len(s), len(out))
    if Counter(out) != Counter(s):
        return False, "does not use exactly the letters of the input"
    if out != out[::-1]:
        i = next(i for i in range(len(out)) if out[i] != out[-1 - i])
        return False, "not a palindrome: position %d is %s but position %d is %s" % (i + 1, out[i], len(out) - i, out[-1 - i])
    return True, ""
