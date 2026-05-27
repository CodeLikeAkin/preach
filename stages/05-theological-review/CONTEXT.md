# Stage 05: Theological Review

Run a doctrinal and format validation against the module's 3 output files. Flag any issues for the human reviewer.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Study guide | `../../content/{module_output}/study-guide.md` | Full file | Verify doctrine and scripture |
| Lessons | `../../content/{module_output}/lessons.md` | Full file | Verify format, doctrine, scripture |
| Flashcards | `../../content/{module_output}/flashcards.md` | Full file | Verify doctrinal accuracy of answers |
| Module index | `../../shared/content-map.md` | Matching module row | Map module to output folder path |
| Brand vault | `../../brand-vault/CONTEXT.md` | Theological Guardrails, What You Must Never Do, Lesson Format | The standards to validate against |

## Process

1. Read all 3 output files from the module's content folder.
2. Run doctrine audit: scan for any statement that contradicts the theological guardrails (exclusivity of Christ, cross/resurrection, God's attributes, no moralism).
3. Run scripture audit: list every [VERIFY] reference for human review.
4. Run format audit: check that lessons.md follows all 6 sections per lesson, that Hook has no verses, that Core Teaching is prose-only, that Practical Application is specific.
5. Run naming audit: check that no teacher/preacher/author is named anywhere.
6. Compile review report with pass/fail for each check. List all [VERIFY] references, and flag any theological concerns.
7. If any check fails, flag it in the report and ask the user if they want fixes applied automatically or manually.
8. Run the audit checks below. If any fail, note them in the report.
9. Save the review report to output.

## Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 6 | Review report with pass/fail per check, all [VERIFY] references listed, doctrinal flags | Whether to apply fixes automatically or manually |

## Audit

| Check | Pass Condition |
|-------|---------------|
| Doctrinal soundness | No contradiction of theological guardrails (exclusivity of Christ, cross/resurrection, attribute balance, no moralism) |
| Scripture verification readiness | Every [VERIFY] reference is listed in the report for the human reviewer |
| Hook integrity | No lesson starts its Hook with a Bible verse |
| Prose-only Core Teaching | No bullet points, numbered lists, or subheadings in any Core Teaching section |
| Named references | No teacher, preacher, or author is named anywhere in any file |
| Application specificity | No Practical Application says "pray more" or "read your Bible" |
| Complete output | All 3 files exist (study-guide.md, lessons.md, flashcards.md) |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Review report | `output/review-report.md` | Pass/fail checklist, all [VERIFY] refs listed, doctrinal flags, format issues |
