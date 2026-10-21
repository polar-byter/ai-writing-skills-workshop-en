# Separate a mechanical check from an editorial judgment

A small script can check a rule more consistently than repeated visual inspection. It can also create false confidence if we ask it a question it cannot answer. We will use a punctuation checker and keep its result separate from the explanation's quality.

## Open this experiment

Download [writing-05-checks](../downloads/writing-05-checks.zip), extract it into its own folder and open that folder in OpenCode. Use a plain text editor for the lesson files. Earlier parts are prepared; the current change is yours to make. Keep previous outputs in their original folders so comparisons remain possible.

## Perform the experiment

This starter prepares the earlier skill rule and reference. Open `check-text.html` at the project root in a browser. Paste your latest edited answer into the text area and click **Check**. The page uses the same `scripts/check_text.js` function as the optional Node.js command.

The checker reports non-ASCII punctuation, symbols and separators with their line, column and Unicode code point. It does not change the file. Ordinary English letters and ordinary keyboard punctuation should not be flagged. A deliberately typographic dash can trigger a finding even in a sentence whose meaning is correct.

Now complete the marked skill paragraph: use ordinary keyboard punctuation, name the optional checker, and explicitly distinguish its result from a factual or editorial review. Link to the supplied browser page. If Node.js is already available, the alternative is `node .opencode/skills/write-clear-english/scripts/check_text.js results/article.md`, after saving a real article at that path. Node installation is not required for the browser route.

Run the same editing request in a new session and inspect the trace. If the agent executes a script, examine its actual report. If you check the output manually in the browser instead, record that. Do not describe a suggested command as an executed one.

After the punctuation report, compare the text with `facts.md` yourself. A perfectly ordinary-character sentence can still invent a benefit or fail to explain a field.

<img src="../assets/step-05.gif" width="480" alt="Experiment 5: Separate a mechanical check from an editorial judgment">

[Static alternative](../assets/step-05.png). These are illustrative values and steps, not a recorded model run.

## What to record

The checker route and report are recorded. The facts and selection logic are reviewed separately. Neither an empty report nor the agent saying "checked" substitutes for observing what ran.

Use `results/observations.md` to separate the changed instruction, observed loading and actual output. Do not claim a model comparison from file validation alone.

[All lessons](../README.md#lessons).
