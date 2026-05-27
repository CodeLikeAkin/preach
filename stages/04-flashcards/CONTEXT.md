# Stage 04: Flashcards

Generate 10 question-and-answer flashcard pairs plus the memory verse drill (primary + secondary verse) for the module.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Study guide | `../../content/{module_output}/study-guide.md` | Full file | Doctrinal backbone for question content |
| Lessons | `../../content/{module_output}/lessons.md` | Full file | Key truths distilled in each lesson |
| Source notes | `../01-research/output/source-notes.md` | Scripture references section | Additional verses for memory drill |
| Output conventions | `../../shared/output-conventions.md` | Full file | Know where to write the output |
| Module index | `../../shared/content-map.md` | Matching module row | Map module to output folder path |
| Brand vault | `../../brand-vault/CONTEXT.md` | Module Output Structure section | Flashcard format rules |

## Process

1. Read the study-guide.md and lessons.md from the module's content folder.
2. Read the research summary from Stage 01 for additional scripture references.
3. Identify the 10 most important doctrinal questions the module answers. Questions should test comprehension, not trivia.
4. Write each card: question on one side, concise answer (1-3 sentences) on the other.
5. Select the primary and secondary memory verses from the study guide's Suggested Memory Verses section.
6. Run the audit checks below. If any fail, revise before saving.
7. Save as `flashcards.md` to the module's output folder under `content/`.

## Audit

| Check | Pass Condition |
|-------|---------------|
| Card count | Exactly 10 flashcard pairs |
| Answer length | Each answer is 1-3 sentences (concise and memorable) |
| Question quality | Questions test doctrinal comprehension, not trivial facts |
| Memory verses | Primary and secondary verses both present, with full NKJV text and [VERIFY] mark |
| Output path | flashcards.md is written to the correct `content/{level}/{module}/` folder |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Flashcards | `../../content/{level}/{module}/flashcards.md` | 10 Q&A pairs + Memory Verse Drill |
