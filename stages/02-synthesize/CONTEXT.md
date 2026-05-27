# Stage 02: Synthesize

Read the full source notes from Stage 01 and produce a structured study-guide.md following the 6-section format defined in SYSTEM_PROMPT.md.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Previous stage | `../01-research/output/source-notes.md` | Full file | Full per-file extraction — source material for synthesis |
| Brand vault | `../../brand-vault/CONTEXT.md` | Theological Guardrails, Tone & Voice | Ensure synthesis respects doctrine and tone |
| Output conventions | `../../shared/output-conventions.md` | Full file | Know where to write the output |
| Module index | `../../shared/content-map.md` | Matching module row | Map module to output folder path |

## Process

1. Read the full source notes from Stage 01 output.
2. Read the brand vault guardrails section from SYSTEM_PROMPT.md lines 18-33 (via brand-vault routing).
3. Synthesize the research into a structured study guide with these 6 sections:
   - Core Definition
   - Key Biblical Truths (with scripture references marked [VERIFY])
   - Common Misconceptions
   - Practical Application Angles
   - Key Terms & Definitions
   - Suggested Memory Verses (primary and secondary, marked [VERIFY])
4. Create the output folder under `content/` (per shared/content-map.md) if it does not exist.
5. **[Checkpoint]** — Present the study guide sections to the user. Ask: Any gaps or adjustments needed?
6. Run the audit checks below. If any fail, revise before saving.
7. Save as `study-guide.md` to the module's output folder under `content/`.

## Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 5 | Draft study guide — all 6 sections | Whether content is theologically sound and complete |

## Audit

| Check | Pass Condition |
|-------|---------------|
| Section count | All 6 sections present (Core Definition through Suggested Memory Verses) |
| Scripture refs | Every scripture reference is marked [VERIFY] |
| No duplication | Content is synthesized (not copied verbatim from source files) |
| Output path | study-guide.md is written to the correct `content/{level}/{module}/` folder |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Study guide | `../../content/{level}/{module}/study-guide.md` | 6-section markdown document |
