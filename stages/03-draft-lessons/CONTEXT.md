# Stage 03: Draft Lessons

Using the study-guide.md as the theological foundation, draft all 7 lessons in full PREACH format (6 sections each).

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Previous stage | `../../content/{module_output}/study-guide.md` | Full file | Theological foundation for lessons |
| Brand vault | `../../brand-vault/CONTEXT.md` | Theological Guardrails, Tone & Voice, Lesson Format | Ensure every lesson follows format and stays on doctrine |
| Output conventions | `../../shared/output-conventions.md` | Full file | Know where to write the output |
| Module index | `../../shared/content-map.md` | Matching module row | Map module to output folder path |
| Questionnaire flags | `../../setup/questionnaire.md` | Q5 flags (if any) | Additional emphasis instructions |

## Process

1. Read the study-guide.md from `content/{level}/{module}/study-guide.md`.
2. Read the brand vault: guardrails (lines 18-33), tone (lines 37-53), lesson format (lines 59-97), what never to do (lines 160-173).
3. Determine lesson titles. Title them to flow logically through the module's content.
4. Draft Lessons 1-4. Each lesson must contain all 6 sections: Hook, Core Teaching, Key Scriptures, Practical Application, Summary, Next Lesson Preview.
5. **[Checkpoint]** — Present Lessons 1-4 to the user. Ask: Are the titles right? Any lesson that feels off? Adjustments before continuing?
6. Draft Lessons 5-7 based on any checkpoint feedback.
7. Run the audit checks below. If any fail, revise before saving.
8. Save as `lessons.md` to the module's output folder under `content/`.

## Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 5 | Lessons 1-4 with titles and full 6-section content | Whether to adjust titles, depth, tone, or any specific lessons before continuing |

## Audit

| Check | Pass Condition |
|-------|---------------|
| Lesson count | Exactly 7 lessons |
| Section count | Each lesson has all 6 sections in order: Hook, Core Teaching, Key Scriptures, Practical Application, Summary, Next Lesson Preview |
| Hook starts without verse | No lesson opens its Hook with a Bible verse |
| Core Teaching is prose | No bullet points, numbered lists, or subheadings in Core Teaching |
| Illustration present | Each Core Teaching contains at least one everyday life illustration |
| No named teachers | No teacher, preacher, or author referenced by name anywhere |
| Scripture marked | Every verse is marked [VERIFY] |
| Practical Application is specific | Not "pray more" or "read your Bible" — must be measurable and actionable this week |
| Gospel connection | Every Core Teaching connects the theological truth to the gospel |
| Output path | lessons.md is written to the correct `content/{level}/{module}/` folder |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Lessons | `../../content/{level}/{module}/lessons.md` | 7 lessons in full PREACH format |
