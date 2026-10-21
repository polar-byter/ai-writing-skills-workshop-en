# Explain the data before the selection rule

> **Where we are.** The skill loads and holds one general rule. Now we spell out what exactly the reader needs explained about the data.

"Write clearly" does not tell the model what kind of explanation our reader needs. We make the requirement concrete on the familiar table: a first-time reader should understand the fields and be able to say why A-17 is selected. Those are the signs we will look for in the edit.

## Open this step

Download [writing-03-reader-context](https://github.com/polar-byter/ai-writing-skills-workshop-en/blob/main/downloads/writing-03-reader-context.zip), extract it into its own folder and open that folder in OpenCode with the same model.

## Do the experiment

In this step's `SKILL.md` (under `.opencode/skills/write-clear-english`), the basic rule from last time is ready. Find the marked place and add a short paragraph with three requirements:

1. Establish the reader's task before naming any field.
2. Show the meaning of `status` and `elapsed_days` on the actual records, and keep both selection conditions: A-17 is `new`, that is, not yet approved, and `elapsed_days=3` means three days since it was submitted.
3. Before a threshold or data set changes, say what changes and why: the five-day experiment uses the same rows, and none of them qualifies.

Write the requirement, not a favorite sentence. It should still work if a future text has other row IDs or another task; A-17 is only today's example. And no unsupported claim about efficiency.

Save, create a new session, choose the same model and send `PROMPT.md` as before. Do not paste your new rule into the request: it has to arrive from the changed skill. Check the loading in the trace and save the answer as a new result.

Read it against the facts. Can you find an explanation of both fields and of why A-17 is selected? Is the five-day threshold introduced as a separate experiment? If the model dropped the second experiment altogether, note it separately: the facts allow it, but it is not required.

## Before the next step

The model and input are unchanged. A reader can reconstruct the selection from the actual records, and the threshold no longer changes silently. Write down the gaps that remain rather than treating a smooth paragraph as proof that it is correct.

Next: [move a useful example into a reference](https://github.com/polar-byter/ai-writing-skills-workshop-en/blob/main/lessons/04-references.md). [All lessons](https://github.com/polar-byter/ai-writing-skills-workshop-en/blob/main/README.md#lessons).
