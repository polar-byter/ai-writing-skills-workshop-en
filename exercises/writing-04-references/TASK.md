# Move a useful example into a reference

A growing collection of examples can make the main instruction hard to navigate. We will move a specific example into a neighboring reference and tell the agent when to read it. This reveals the difference between discovering a folder and loading the resources relevant to a task.

## Open this experiment

Download [writing-04-references](https://github.com/polar-byter/ai-writing-skills-workshop-en/blob/main/downloads/writing-04-references.zip), extract it into its own folder and open that folder in OpenCode. Use a plain text editor for the lesson files. Earlier parts are prepared; the current change is yours to make. Keep previous outputs in their original folders so comparisons remain possible.

## Perform the experiment

Open `.opencode/skills/write-clear-english/references/reader-first.md`. Complete the marked example: explain the original two-day selection, announce a second experiment at five days using the same records, and state the new outcome. Do not introduce new rows or measured benefits.

Then open `SKILL.md`. At the marked location, add a Markdown link to `references/reader-first.md` and say when it should be read: before explaining unfamiliar fields or changing the example. The path is relative to the skill folder. A link names the resource, while the surrounding instruction supplies its purpose.

In a new session, send the unchanged `PROMPT.md`. Inspect two separate events: loading the skill body and reading the reference. A neighboring file is not automatically part of the model input. If the reference is not read, check the path and loading condition before adding more prose.

Compare the result with the same criteria as the previous lesson. Moving the example to a file need not improve the output by itself. This experiment checks whether guidance can be organized and loaded deliberately.

## What to record

The skill and reference load are separately observable. The edited answer still explains the original data and announces the second experiment. No improvement is claimed solely because a resource was reorganized.

Use `results/observations.md` to separate the changed instruction, observed loading and actual output. Do not claim a model comparison from file validation alone.

[All lessons](https://github.com/polar-byter/ai-writing-skills-workshop-en/blob/main/README.md#lessons).
