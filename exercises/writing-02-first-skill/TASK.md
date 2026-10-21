# Create the first SKILL.md

Repeating a preference in every request is awkward. A skill gives the application a named place to discover reusable guidance. We will add one editorial rule and verify that its content actually reaches the model.

## Open this experiment

Download [writing-02-first-skill](https://github.com/polar-byter/ai-writing-skills-workshop-en/blob/main/downloads/writing-02-first-skill.zip), extract it into its own folder and open that folder in OpenCode. Use a plain text editor for the lesson files. Earlier parts are prepared; the current change is yours to make. Keep previous outputs in their original folders so comparisons remain possible.

## Perform the experiment

In the extracted project, open `.opencode/skills/write-clear-english/SKILL.md`. The folder name and frontmatter `name` already match. Fill the empty `description` with a specific use case, such as editing an explanation of a work task from supplied facts. Then add one rule in the marked place: preserve provided facts and do not claim measured improvement when no measurement was supplied.

Keep the `---` frontmatter delimiters and exact file name. `description` helps the application and model decide when the skill is relevant; the body contains the instructions used after loading. A file being present does not prove that its body has been loaded.

Save the file, create a new session with the same model and send all of `PROMPT.md`. The only new request is to load `write-clear-english`; the source and facts remain the same. In the activity trace, inspect the `skill` action and verify the selected name and loaded content. According to [OpenCode's skill documentation](https://opencode.ai/docs/skills/), project skills can be loaded through that native tool.

If the agent only reads the file with an ordinary file-reading operation, record that distinction: the text may have reached context, but native skill discovery has not been demonstrated. If it finds nothing, check the project folder, `.opencode/skills` path, exact name, frontmatter and permissions. Try a fresh session after saving.

Save the new output separately. Compare it with the baseline; do not require identical wording or claim that loading a rule guarantees compliance.

## What to record

The trace shows what was loaded and how. The edited explanation preserves the facts and does not invent measured gains. An unchanged answer is a valid observation if the baseline already met that criterion.

Use `results/observations.md` to separate the changed instruction, observed loading and actual output. Do not claim a model comparison from file validation alone.

[All lessons](https://github.com/polar-byter/ai-writing-skills-workshop-en/blob/main/README.md#lessons).
