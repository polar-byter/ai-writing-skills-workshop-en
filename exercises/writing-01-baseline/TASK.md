# Record a baseline edit

Before adding a rule, we need a comparison. The draft is deliberately abrupt: it mentions table fields without explaining them and changes an age threshold without a transition. We will ask for an edit with the facts supplied, then inspect what the model improves and what it still leaves unclear.

## Open this experiment

Download [writing-01-baseline](https://github.com/polar-byter/ai-writing-skills-workshop-en/blob/main/downloads/writing-01-baseline.zip), extract it into its own folder and open that folder in OpenCode. Use a plain text editor for the lesson files. Earlier parts are prepared; the current change is yours to make. Keep previous outputs in their original folders so comparisons remain possible.

## Perform the experiment

Open this independent starter as the project and create a new session with the same model used in setup. There is no local skill yet. Open `PROMPT.md`, copy its entire content and send it in the chat. The source and facts are already included in that prompt, so this first experiment does not depend on whether the application reads a separate attachment.

Read the answer against `facts.md` and the two rows in `requests.csv`. We are selecting requests that are not approved and are older than two days. A-17 is new and three days old, so it qualifies. A-18 is approved and one day old, so it does not. The second five-day experiment should be announced and should exclude both rows.

Save the actual answer as `results/baseline.md`. In `results/observations.md`, note whether both conditions are explained, whether the changed threshold is introduced, and whether the text invents an application button or a measured benefit. Do not edit the saved answer to make the comparison look cleaner.

A good baseline is a useful result too. It may mean that your prompt and model already handle this example well; it does not prove that a skill is unnecessary on every future task. Keep the same input for the next experiment.

## What to record

The baseline answer and model name are saved. You can identify which claims match the supplied facts and which details, if any, were invented. No skill-loading claim is made at this stage.

Use `results/observations.md` to separate the changed instruction, observed loading and actual output. Do not claim a model comparison from file validation alone.

[All lessons](https://github.com/polar-byter/ai-writing-skills-workshop-en/blob/main/README.md#lessons).
