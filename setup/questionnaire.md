# Onboarding Questionnaire: PREACH Module Drafting

Ask ALL questions below in a single conversational pass. The user should be able to answer everything in one message. These answers inform stage 01 and determine which resource folder to read and which output folder to write to.

---

### Q1: Which level is this module in?
- **Options:** Level 1 — Foundations, Level 2 — Evangelism, Level 3 — Apologetics
- **Purpose:** Determines the level folder in both resources/ and content/

### Q2: Which module number?
- **Options:** Level 1: 1-10, Level 2: 1-12, Level 3: 1-5
- **Purpose:** Maps to the folder number in resources/ and the zero-padded number in content/

### Q3: What is the module name?
- **Examples:** "who-is-god", "the-trinity", "creation"
- **Type:** free text (kebab-case)
- **Purpose:** Completes the resource path and output path

### Q4: Is this a batch run or single module?
- **Options:** Single module, Batch (all modules in a level or all 27)
- **Purpose:** Single routes through stages 01-05 once. Batch iterates all modules.

### Q5: Any flags or special instructions?
- **Examples:** "Emphasize grace", "Light on apologetics depth", "Focus on application"
- **Type:** free text (optional)
- **Purpose:** Passed to stage 03 as an additional input for lesson drafting

---

## After Onboarding

Tell the user: "Got it. When you are ready, start with Stage 01 — Research. I will read every source file in the module's resource folder and produce a research summary."

Then point them to `stages/01-research/CONTEXT.md`.
