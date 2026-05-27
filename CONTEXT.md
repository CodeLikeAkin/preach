# PREACH — Content Drafting Workspace

Draft lesson content for the PREACH discipleship app through a 5-stage pipeline. All source material lives in `resources/` (read-only). All final output goes to `content/` following the naming rules in `shared/output-conventions.md`.

## Task Routing

| Task Type | Go To | Description |
|-----------|-------|-------------|
| Draft a single module | `stages/01-research/CONTEXT.md` | Read sources, synthesize, draft lessons, flashcards, review |
| Process all 27 modules | `shared/content-map.md` with `batch` trigger | Iterate every module through all 5 stages |
| Check stage completion | `stages/*/output/` scan (or type `status`) | See which stages have output for the current module |

## Shared Resources

| Resource | Location | Contains |
|----------|----------|----------|
| System prompt (canonical) | `SYSTEM_PROMPT.md` | Theological guardrails, tone/voice, lesson format, output rules |
| Product requirements | `PREACH_PRD (1).md` | Full PRD v1.4 — app structure, levels, modules |
| Module index | `shared/content-map.md` | All 27 modules with resource paths and output paths |
| Output conventions | `shared/output-conventions.md` | Folder naming, file naming, numbering rules |
| Brand vault routing | `brand-vault/CONTEXT.md` | Routes agents to SYSTEM_PROMPT.md sections |
