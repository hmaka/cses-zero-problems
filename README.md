# cses-zero-problems

Problem definitions for [CSES-ZERO](https://cses-zero.fly.dev/), a multi-language competitive programming judge.

Problems are authored as plain files in this repository. Contributors are welcome to open PRs to fix typos, improve test cases, add tips, write editorials, or contribute new problems.

## Directory Layout

```
problems/
└── <category-slug>/                 # e.g. "introductory-problems"
    └── <problem-slug>/              # e.g. "weird-algorithm"
        ├── problem.md               # required — statement (Markdown)
        ├── meta.json                # required — title, limits
        ├── tests/                   # required — judged test cases
        │   ├── 1.in
        │   ├── 1.out
        │   ├── 2.in
        │   └── 2.out
        ├── tips/                    # optional — progressive hints
        │   ├── 1.md
        │   └── 2.md
        ├── editorial.md             # optional — solution writeup
        └── checker/                 # optional — for problems with multiple valid outputs
            └── checker.py           # see the checker/ contract below
```

`<category-slug>` and `<problem-slug>` must be lowercase, hyphen-separated, and unique. They serve as the problem's identity — renaming a folder renames the slug.

## File Contracts

### `problem.md`

Markdown statement, rendered with [goldmark](https://github.com/yuin/goldmark). Worked examples should be written inline in prose — the `tests/` folder is for judging only, not display.

Example skeleton:

```markdown
# Weird Algorithm

Consider an algorithm that takes a positive integer `n`...

## Input

The first input line contains an integer `n`.

## Output

Print a line that contains all values of `n` during the algorithm.

## Constraints

- 1 ≤ n ≤ 10^6

## Example

**Input:**
```
3
```

**Output:**
```
3 10 5 16 8 4 2 1
```
```

### `meta.json`

```json
{
  "title": "Weird Algorithm",
  "limits": {
    "default": { "time_ms": 1000, "memory_kb": 262144 },
    "languages": {
      "python3": { "time_ms": 3000 },
      "java":    { "time_ms": 2000 }
    }
  }
}
```

- `title` — display name shown in problem lists.
- `limits.default` — applied to languages without an override. Both `time_ms` and `memory_kb` are required here.
- `limits.languages` — optional per-language overrides. Any unspecified field inherits from `default`. Language identifiers are slugs (`"python3"`, `"cpp17"`, `"java"`), not Judge0 IDs.

### `tests/`

Numbered input/output pairs: `<n>.in` and `<n>.out`. All test cases are public. Tests are judged in numeric order. Use a fresh sequence per problem starting at `1`.

### `tips/` *(optional)*

Numbered Markdown files: `1.md`, `2.md`, ... Tips are shown collapsed on the problem page; users opt in to reveal them. **Lower-numbered tips should be gentler nudges; higher-numbered tips approach a giveaway.** Renumber if you want to insert between two existing tips.

### `editorial.md` *(optional)*

Full Markdown solution writeup. Rendered on a separate "Editorial" tab.

### `checker/` *(optional)*

Only for problems with more than one correct output (e.g. "print any valid permutation"). Without a checker, output must match `tests/<n>.out`, ignoring trailing whitespace.

```
checker/
├── checker.py              # required: defines check()
├── wrong/<n>-<label>.out   # outputs for test <n> that must be REJECTED
└── valid/<n>-<label>.out   # other correct outputs for test <n> that must be ACCEPTED
```

**`checker.py` contract.** The judge runs it with **Python 3.8**, in the sandbox.
- Define `check(input, output, answer)`. The three arguments are strings:
  - `input`: the test input;
  - `output`: the contestant's output;
  - `answer`: `tests/<n>.out`, which is *one* valid answer.
- Return `True` / `False`, or `(bool, message)`. The message is shown to the contestant when the answer is rejected, so make it specific: `"positions 3 and 4 hold 2 and 1, which differ by 1"`.
- **Verify, don't solve.** Usually you check that the output has the required properties. Take what's hard to compute from `answer`, e.g. whether a solution exists at all (`NO SOLUTION`) or the optimal value.
- **Raising an exception rejects the answer.** That's convenient when the contestant's output doesn't parse (`int("abc")`), but it also means a checker bug shows up as a rejection.
- `print()` is fine for debugging; it never affects the verdict.
- Only define functions; don't read stdin or files. An `if __name__ == "__main__":` block is fine for local experiments; the judge doesn't run it.

**Self-tests.** CI runs [`scripts/check_checkers.py`](scripts/check_checkers.py) on every PR, under Python 3.8. It checks that:
- every `tests/*.out` and `checker/valid/*` file is accepted (the checker isn't too strict);
- every `checker/wrong/*` file is rejected (the checker isn't too lenient).

Add a few `wrong/` cases for each way an answer can be wrong. A checker that accepts everything would otherwise go unnoticed, because correct submissions still pass. Run the self-tests locally with `python3 scripts/check_checkers.py`.

See `problems/introductory-problems/permutations/` for an example.

## Sync to Judge

On every merge to `main`, a GitHub webhook notifies the CSES-ZERO judge, which clones this repository and upserts problems into its database. Problems go live within seconds of merge. A daily safety-net job re-syncs everything in case a webhook was missed.

## Contributing

Open a PR. PRs are reviewed before merge — both for content quality and for catching malformed `meta.json` or test cases.
