# cses-zero-problems

Problem definitions for [CSES-ZERO](https://github.com/hmaka/CSES-ZERO), a multi-language competitive programming judge.

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
            └── checker.<lang>       # contract TBD
```

`<category-slug>` and `<problem-slug>` must be lowercase, hyphen-separated, and unique. They serve as the problem's identity — renaming a folder renames the slug.

## File Contracts

### `problem.md`

Markdown statement, rendered with [goldmark](https://github.com/yuin/goldmark) in safe mode (no raw HTML). Worked examples should be written inline in prose — the `tests/` folder is for judging only, not display.

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

For problems with multiple valid correct outputs (e.g. "print any valid path"). Contract TBD — not yet implemented. Reserved for future use.

## Sync to Judge

On every merge to `main`, a GitHub webhook notifies the CSES-ZERO judge, which clones this repository and upserts problems into its database. Problems go live within seconds of merge. A daily safety-net job re-syncs everything in case a webhook was missed.

## Contributing

Open a PR. PRs are reviewed before merge — both for content quality and for catching malformed `meta.json` or test cases.
