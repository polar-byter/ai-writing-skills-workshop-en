# Try the skill on a different explanation

Our earlier rule helped with one table example. To see whether it expresses a transferable principle, we need another task with different data and a different possible misconception. We will also check that the skill works in a separate project folder.

## Open this experiment

Download [writing-06-transfer](../downloads/writing-06-transfer.zip), extract it into its own folder and open that folder in OpenCode. Use a plain text editor for the lesson files. Earlier parts are prepared; the current change is yours to make. Keep previous outputs in their original folders so comparisons remain possible.

## Perform the experiment

First repeat the original request using this starter's prepared skill. Record which files were loaded. Then open `transfer-source.md` and `transfer-facts.md`: the new reader is trying to understand a helper's answer from a policy fragment, not select approval records.

Create a fresh session and send `TRANSFER-PROMPT.md`. This prompt supplies its own source and facts. Check whether the explanation identifies the selected document fragment, acknowledges that a skill does not grant file access, and distinguishes a request to acknowledge missing information from guaranteed compliance.

The table row IDs should not appear in this new answer. If your rule or reference forces A-17 into every explanation, revise it to require concrete current data rather than that particular example. Repeat the transfer request while changing only that rule and keep both outputs.

For a separate discovery check, copy this starter to a new ordinary project folder and open that folder in OpenCode. Keep the local skill under `.opencode/skills/write-clear-english`, create a fresh session and inspect actual loading there. Do not install the skill globally as a shortcut; the experiment concerns portability of the local folder.

Save both actual answers and observations. This small test can expose overfitting and discovery problems, but it does not establish that the skill improves all topics or models. Keep the ready-made final package separate from the version you have built.

<img src="../assets/step-06.gif" width="480" alt="Experiment 6: Try the skill on a different explanation">

[Static alternative](../assets/step-06.png). These are illustrative values and steps, not a recorded model run.

## What to record

The new task is explained using its own facts, not the old record IDs. Loading is observed in the new project. The final report distinguishes completed checks, remaining uncertainty and model-dependent output.

Use `results/observations.md` to separate the changed instruction, observed loading and actual output. Do not claim a model comparison from file validation alone.

[All lessons](../README.md#lessons).
