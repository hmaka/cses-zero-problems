#!/usr/bin/env python3
"""Self-test every problem's checker. CI runs this on Python 3.8 (the judge's
version) for every PR; run it locally with `python3 scripts/check_checkers.py`.

For each problems/<category>/<slug>/checker/checker.py:
  - every reference output tests/<n>.out must be ACCEPTED   (not too strict)
  - every checker/valid/<n>-<label>.out must be ACCEPTED    (other correct answers)
  - every checker/wrong/<n>-<label>.out must be REJECTED    (not too lenient)

Semantics match the judge's harness: an exception inside check() counts as a
rejection (usually unparseable output), and check() must return bool or
(bool, message).
"""
import importlib.util
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent


def load_check(path):
    spec = importlib.util.spec_from_file_location("checker", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.check


def run(check, inp, out, ans):
    try:
        res = check(inp, out, ans)
    except Exception as e:  # the judge treats this as Wrong Answer
        return False, "raised %s: %s" % (type(e).__name__, e)
    if isinstance(res, bool):
        return res, ""
    if isinstance(res, tuple) and len(res) == 2 and isinstance(res[0], bool):
        return res[0], str(res[1])
    raise TypeError("check() must return bool or (bool, str), got %r" % (res,))


def test_number(path):
    """'4-adjacent.out' -> 4"""
    return int(path.name.split("-", 1)[0])


def main():
    failures = 0
    checkers = sorted(ROOT.glob("problems/*/*/checker/checker.py"))
    for checker_py in checkers:
        problem = checker_py.parent.parent
        name = problem.relative_to(ROOT / "problems")
        check = load_check(checker_py)
        tests = problem / "tests"
        read = lambda p: p.read_text(encoding="utf-8")

        cases = [("reference", p, int(p.stem), True) for p in sorted(tests.glob("*.out"), key=lambda p: int(p.stem))]
        cases += [("valid", p, test_number(p), True) for p in sorted((checker_py.parent / "valid").glob("*.out"))]
        cases += [("wrong", p, test_number(p), False) for p in sorted((checker_py.parent / "wrong").glob("*.out"))]

        for kind, path, n, want in cases:
            inp, ans = tests / ("%d.in" % n), tests / ("%d.out" % n)
            if not inp.exists() or not ans.exists():
                print("FAIL %s: %s refers to test %d, which doesn't exist" % (name, path.name, n))
                failures += 1
                continue
            ok, msg = run(check, read(inp), read(path), read(ans))
            if ok != want:
                failures += 1
                print("FAIL %s: %s %s was %s%s" % (name, kind, path.name,
                      "accepted" if ok else "rejected", ": " + msg if msg else ""))
        print("%s %s: %d cases" % ("ok  " if failures == 0 else "....", name, len(cases)))

    if not checkers:
        print("no checkers found")
    if failures:
        print("%d failure(s)" % failures)
        sys.exit(1)


if __name__ == "__main__":
    main()
