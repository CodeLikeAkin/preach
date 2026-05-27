# Stage 01: Research

Read every source file in the module's resource folder. Produce a full per-file extraction of all content — nothing condensed.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| User | `setup/questionnaire.md` answers | Level, module number, module name | Determine the resource path |
| Module index | `../../shared/content-map.md` | Matching module row | Map module to resource folder path |
| Brand vault | `../../brand-vault/CONTEXT.md` | Full file | Route to guardrails and tone references |

## Process

1. Confirm module details from questionnaire answers. Read the matching row from `shared/content-map.md` to get the resource path.
2. List all files in the module's resource folder under `resources/`. Note any PDFs — these will be extracted via `python scripts/extract-pdf-text.py` in step 3.
3. Read every file. Do not skip any file. For PDFs, extract text using `python scripts/extract-pdf-text.py <path-to-pdf>` (uses PyMuPDF/fitz — already installed). Capture the full stdout output.
4. For each file, extract all content: key themes, theological concepts, scripture references cited, arguments, notable quotes — organized per file. Nothing condensed. Preserve every meaningful detail.
5. **[Checkpoint]** — Present the file count and resource path to the user. Ask: Any additional source material to include?
6. Run the audit checks below. If any fail, revise before saving.
7. Write the source notes to output.

## Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 5 | Resource path, file count, source filenames, any PDFs found | Whether to proceed or add more sources |

## Audit

| Check | Pass Condition |
|-------|---------------|
| Source coverage | Every file in the resource folder was read (zero skipped) |
| PDF extraction | PDF files were text-extracted via `scripts/extract-pdf-text.py`, not just noted |
| Module accuracy | The resource path matches the module selected during onboarding |
| Extraction completeness | Every file has a dedicated section with all content preserved — no condensation |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Source notes | `output/source-notes.md` | Per-file extraction: themes, concepts, arguments, scripture refs, quotes — full fidelity |
