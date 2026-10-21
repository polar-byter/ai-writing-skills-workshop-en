# Build a writing skill one change at a time

We will edit an explanation about approval requests. The facts are small enough to check directly: A-17 is new and three days old; A-18 is approved and one day old. The original rule selects requests that are not approved and are older than two days. A second experiment raises the threshold to five days, excluding both current records.

The poor draft does not explain that setting clearly. It names fields abruptly, changes the threshold and claims an efficiency gain that has not been measured. We will preserve the facts while gradually improving the reusable editorial instructions.

## The experiment sequence

| Step | What changes | What stays fixed |
|---|---|---|
| [0. Workspace](../lessons/00-setup.md) | Confirm the application and model connection | No skill yet |
| [1. Baseline](../lessons/01-baseline.md) | Save an ordinary edit | Draft, facts and model |
| [2. First skill](../lessons/02-first-skill.md) | Add discovery metadata and one rule | Same editing request |
| [3. Reader context](../lessons/03-reader-context.md) | Add one observable explanation criterion | Same records and thresholds |
| [4. Reference](../lessons/04-references.md) | Move a detailed example and route to it | Same acceptance criteria |
| [5. Checker](../lessons/05-checks.md) | Add a mechanical punctuation check | Separate factual review |
| [6. Transfer](../lessons/06-transfer.md) | Try a different explanation and project folder | Record actual loading and output |

Each lesson includes its own archive and a visible folder under [exercises](../exercises/README.md). Extract a starter into a separate folder rather than overwriting your earlier experiment. Earlier parts are prepared; the current change remains marked for you to write.

<img src="../assets/experiment-cycle.gif" width="480" alt="One changed instruction with a recorded comparison">

[Static alternative](../assets/experiment-cycle.png). The illustration shows the experiment design, not observed model results.

## What to save

Record the model, application version, date, changed instruction, evidence of loading, actual output and unresolved questions. Save baseline and revised answers separately. Do not clean up the old answer before comparing it with a new one.

Judge the explanation against the facts. Can a reader identify what status and elapsed_days mean, reconstruct both conditions and explain the second threshold? Did the answer invent a button, service or measured benefit? These checks are more informative than a general impression that the prose sounds better.

## What a result means

If a reference was loaded but the answer is unchanged, record both facts. Loading is not proof of improvement. If a model already produces a good baseline, the lack of visible change does not make the run a failure. If the new task exposes a rule tied to the old row ID, revise the scope of the instruction rather than hiding the result.

The workbook gives you a repeatable method for developing a skill, not a deterministic recipe for identical generated paragraphs. No live OpenCode comparison is claimed merely because the packaged files and checker pass automated tests.

Start with [workspace setup](../lessons/00-setup.md), or inspect the [ready skill](../skill/write-clear-english/SKILL.md) separately when you want to see the final organization.
