# AI Writing Skills Workshop

Build a reusable writing skill through small, observable experiments. Start with a rough explanation, record a baseline, add one rule, load a reference, try a mechanical checker and test the result on a different task.

This English edition is for people new to agent skills. You do not need to install Python for the main workbook. Use OpenCode Desktop and a plain text editor; the optional punctuation checker works in a browser, with a Node.js alternative if already available.

**[How the skill works](articles/from-feedback-to-a-skill.md)** / **[The experiment plan](articles/workbook.md)** / **[Ready prompts](prompts/README.md)** / **[Ready SKILL.md](skill/write-clear-english/SKILL.md)** / **[Download the complete skill](downloads/write-clear-english.zip)**

## Lessons

| Step | Lesson | Independent starter |
|---|---|---|
| 0 | [Prepare the workspace](lessons/00-setup.md) | [writing-00-setup](downloads/writing-00-setup.zip) |
| 1 | [Record a baseline edit](lessons/01-baseline.md) | [writing-01-baseline](downloads/writing-01-baseline.zip) |
| 2 | [Create the first SKILL.md](lessons/02-first-skill.md) | [writing-02-first-skill](downloads/writing-02-first-skill.zip) |
| 3 | [Explain the data before the selection rule](lessons/03-reader-context.md) | [writing-03-reader-context](downloads/writing-03-reader-context.zip) |
| 4 | [Move a useful example into a reference](lessons/04-references.md) | [writing-04-references](downloads/writing-04-references.zip) |
| 5 | [Separate a mechanical check from an editorial judgment](lessons/05-checks.md) | [writing-05-checks](downloads/writing-05-checks.zip) |
| 6 | [Try the skill on a different explanation](lessons/06-transfer.md) | [writing-06-transfer](downloads/writing-06-transfer.zip) |

The starter stages intentionally differ from the final package. Keep each extracted experiment separate and inspect actual loading in the activity trace. A model's claim that it used a skill is not evidence that the instructions or reference were loaded.

The ready skill targets clear English explanations. It adapts editorial principles from a separate Russian project rather than translating Russian-specific wording literally. Its final package remains separate from learner work.

Repository checks validate navigation, stage packaging and checker behavior. They do not perform or claim a live OpenCode writing comparison. Free model offerings can change; the setup lesson links to the current official catalog.
