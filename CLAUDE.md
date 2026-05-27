# PREACH — Content Drafting Workspace

Draft doctrinally sound lesson content for the PREACH discipleship mobile app through a structured 5-stage pipeline.

## Folder Map

```
preach-ide/
├── CLAUDE.md                    (you are here)
├── CONTEXT.md                   (task routing and shared resources)
├── SYSTEM_PROMPT.md             (canonical: guardrails, tone, lesson format)
├── MODULE_BOUNDARIES.md         (what each module covers and does not cover)
├── PREACH_PRD (1).md            (product requirements reference)
├── setup/
│   └── questionnaire.md         (onboarding — select module, level, flags)
├── brand-vault/
│   └── CONTEXT.md               (routes to SYSTEM_PROMPT.md sections)
├── shared/
│   ├── content-map.md           (all 27 modules with paths)
│   └── output-conventions.md    (folder/file naming rules)
├── Resources/                   (read-only source files — 242 files across 27 modules)
├── content/                     (final output — created by pipeline)
├── stages/
│   ├── 01-research/             (read all source files — full per-file extraction)
│   ├── 02-synthesize/           (produce study-guide.md)
│   ├── 03-draft-lessons/        (draft 7 lessons in PREACH format)
│   ├── 04-flashcards/           (produce 10 Q&A pairs + memory drill)
│   └── 05-theological-review/   (verify doctrine, scripture, format)
├── MODULE_PROMPT.md             (retired — replaced by workspace)
└── BATCH_PROMPT.md              (retired — replaced by workspace)
```

## Triggers

| Keyword | Action |
|---------|--------|
| `setup` | Run onboarding — select module, level, any flags |
| `status` | Show pipeline completion for all five stages |
| `batch` | Process all 27 modules sequentially |

### How `status` works

Scan `stages/*/output/` folders. If output contains files other than .gitkeep, the stage is COMPLETE. Otherwise PENDING.

```
Pipeline Status: PREACH Content Drafting

  [01-research]  -->  [02-synthesize]  -->  [03-draft-lessons]  -->  [04-flashcards]  -->  [05-theological-review]
      STATUS             STATUS                STATUS                    STATUS                    STATUS
```

### How `batch` works

For each module in `shared/content-map.md`, run all 5 stages in sequence. Do not start the next module until all 3 output files (study-guide.md, lessons.md, flashcards.md) are saved and stage 05 passes. Report summary at end.

## Pre-Flight Read

Before starting any module, load and read these three files in order:
1. `SYSTEM_PROMPT.md` — guardrails, tone, lesson format
2. `MODULE_BOUNDARIES.md` — what this module covers and does not cover
3. This module's stage CONTEXT.md (e.g., `stages/01-research/CONTEXT.md`)

## Routing

| Task | Go To |
|------|-------|
| Draft a single module | `stages/01-research/CONTEXT.md` |
| Check pipeline status | `stages/*/output/` scan (or type `status`) |
| Batch draft all modules | `shared/content-map.md` + iterate stages |

## What to Load

| Task | Load These | Do NOT Load |
|------|-----------|-------------|
| Research source files | `brand-vault/CONTEXT.md`, `shared/content-map.md` | `stages/02-synthesize/` through `stages/05-theological-review/` |
| Synthesize study guide | `stages/01-research/output/`, `brand-vault/CONTEXT.md`, `shared/output-conventions.md` | `stages/03-draft-lessons/` through `stages/05-theological-review/` |
| Draft lessons | `stages/02-synthesize/output/`, `brand-vault/CONTEXT.md`, `shared/output-conventions.md` | `stages/01-research/`, `stages/04-flashcards/`, `stages/05-theological-review/` |
| Generate flashcards | `stages/02-synthesize/output/`, `stages/03-draft-lessons/output/`, `stages/01-research/output/` | `stages/05-theological-review/` |
| Theological review | `stages/02-synthesize/output/`, `stages/03-draft-lessons/output/`, `stages/04-flashcards/output/`, `brand-vault/CONTEXT.md` | `stages/01-research/` |

## Stage Handoffs

Each stage writes its output to its own `output/` folder. The next stage reads from there.
