# AI Writing Skills Workshop

Turn your editorial experience into a reusable writing skill for an AI agent, through small experiments you can check. Start with an awkward explanation, record a baseline, add one rule, load a reference, try a mechanical checker and test the result on a different task.

The workbook is for people new to agent skills. You do not need Python: OpenCode Desktop and a plain text editor are enough, and the optional punctuation checker runs in a browser, or with Node.js if you already have it.

**[How the skill works](articles/from-feedback-to-a-skill.md)** / **[The experiment plan](articles/workbook.md)** / **[Ready prompts](prompts/README.md)** / **[Ready SKILL.md](skill/write-clear-english/SKILL.md)** / **[Download the complete skill](downloads/write-clear-english.zip)**

## Lessons

| Step | Lesson | Starter |
|---|---|---|
| 0 | [Prepare the workspace](lessons/00-setup.md) | [writing-00-setup](downloads/writing-00-setup.zip) |
| 1 | [Record a baseline edit](lessons/01-baseline.md) | [writing-01-baseline](downloads/writing-01-baseline.zip) |
| 2 | [Create the first SKILL.md](lessons/02-first-skill.md) | [writing-02-first-skill](downloads/writing-02-first-skill.zip) |
| 3 | [Explain the data before the selection rule](lessons/03-reader-context.md) | [writing-03-reader-context](downloads/writing-03-reader-context.zip) |
| 4 | [Move a useful example into a reference](lessons/04-references.md) | [writing-04-references](downloads/writing-04-references.zip) |
| 5 | [Separate a mechanical check from an editorial judgment](lessons/05-checks.md) | [writing-05-checks](downloads/writing-05-checks.zip) |
| 6 | [Try the skill on a different explanation](lessons/06-transfer.md) | [writing-06-transfer](downloads/writing-06-transfer.zip) |

The starters hold different stages of the skill on purpose, so keep each extracted step in its own folder. Check in the activity trace that the skill and its references were actually loaded; an agent saying it used a skill does not show that.

The ready skill targets clear English explanations and teaches a model to avoid the patterns that make text sound machine-written. It adapts editorial principles from a separate Russian project rather than translating its wording. Free model offerings change over time; the setup lesson links to the current official catalog.
