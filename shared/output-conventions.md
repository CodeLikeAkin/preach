# Output Conventions

All final output follows the rules in `SYSTEM_PROMPT.md` — File & Folder Rules section. This file is a quick reference; the canonical source is `SYSTEM_PROMPT.md`.

## Output Path Structure

```
content/
├── level-1-foundations/
│   ├── 01-who-is-god/
│   │   ├── study-guide.md
│   │   ├── lessons.md
│   │   └── flashcards.md
│   ├── 02-the-trinity/
│   └── ... (10 modules)
├── level-2-evangelism/
│   └── ... (12 modules)
└── level-3-apologetics/
    └── ... (5 worldviews)
```

## Rules

- **Zero-padded numbers:** 01, 02, 03 ... 10, 11, 12
- **Each module gets its own subfolder** — never combine modules into one file
- **Each module produces exactly 3 files:**
  - `study-guide.md` — synthesized research summary (6 sections)
  - `lessons.md` — 7 lessons in full PREACH format (6 sections each)
  - `flashcards.md` — 10 Q&A pairs + memory verse drill
- **If content/ does not exist, create it**
- **Never write to resources/** — that folder is read-only

## Level Folder Names

| Level | Folder Name |
|-------|-------------|
| Level 1 — Foundations | `level-1-foundations` |
| Level 2 — Evangelism | `level-2-evangelism` |
| Level 3 — Apologetics | `level-3-apologetics` |
