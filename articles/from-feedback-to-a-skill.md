# From editorial corrections to a reusable skill

A model can produce an appealing paragraph and then lose the qualities you liked in the next draft. Repeating a long history of corrections is a cumbersome way to recover them. In this workshop we turn that editorial experience into a small skill whose instructions and resources can be inspected, tested and carried into another project.

The starting problem is familiar: a technical explanation names fields before explaining their meaning, changes examples without a transition and replaces a useful reason with a promise of efficiency. Correcting one paragraph helps that paragraph. A reusable instruction needs to capture why the passage failed without forcing its exact words or example into every future article.

## What a skill changes

Consider a request such as "Edit this explanation for an analyst seeing the table for the first time." That request describes the current job. The skill can supply recurring editorial criteria: establish the task, show actual field values, preserve the selection conditions and introduce a changed threshold before using it.

In [OpenCode's documented skill mechanism](https://opencode.ai/docs/skills/), the application discovers a folder's name and description, and the native skill tool can load its instruction body. The model can then read a reference or use a provided script when the task calls for it. These are separate events, not an automatic consequence of saving a Markdown file.

<img src="../assets/skill-workflow.gif" width="480" alt="A request, skill loading and a checkable answer">

[Static alternative](../assets/skill-workflow.png). This is a conceptual route, not a recorded model experiment.

An AGENTS.md file has a related but different role: an application can read it as project guidance. Neither that file nor SKILL.md becomes a universal system instruction merely because of its name. The surrounding application determines what is read, how it is included and which tools can run.

## Start with the cause of a confusing passage

"The search results remained in Python" sounds as though it identifies a location, but the missing explanation is an operation: the program returned a list and has not included it in a model request yet. The useful rule is to identify the actual actor, transfer and result. Banning the word "inside" would not solve that wider problem.

Likewise, a threshold can change from two days to five without being a bad example. The reader needs a transition explaining the new experiment and its purpose. A rule requiring one fixed threshold everywhere would prevent useful comparisons instead of making them clearer.

The final skill therefore works on reasoning and continuity, not a list of forbidden phrases. It distinguishes facts from interpretations, checks whether a conclusion follows and asks whether a shortened sentence has lost an important condition. It allows different lengths and voices when they serve the reader.

## Keep the package understandable

The ready package contains these parts:

```text
write-clear-english/
|-- SKILL.md
|-- references/
|   |-- reader-first.md
|   |-- hands-on-lessons.md
|   `-- examples.md
|-- scripts/check_text.js
|-- assets/check-text.html
`-- agents/openai.yaml
```

SKILL.md contains the essential workflow and routes to relevant detail. The references explain the reasoning and show revisions. The script checks ordinary keyboard punctuation; the browser page exposes that same check without requiring Node.js. The optional OpenAI interface metadata describes the package to a supporting application; it is not extra prose the learner must insert into every request.

Scripts belong to a skill when they implement a concrete repeated operation. In this package, the script can identify characters and their positions. It cannot establish that the argument is sound, an example is true or a paragraph is natural. The skill therefore tells the editor to compare the explanation with its facts after a mechanical check.

## Check loading separately from quality

There are at least three useful observations: the application discovered the skill, its body or reference reached the model context, and the resulting text met a defined criterion. The statement "I used the skill" is not enough to establish any of them by itself.

Inspect the activity trace and save the actual output. Keep the model and input fixed when testing a new rule, and use a fresh session to reduce carry-over from previous instructions. The resulting prose still need not match word for word. We can make inputs and comparisons explicit without making generation deterministic.

One successful example is also too narrow. The final exercise changes the subject from request filtering to an answer based on a policy fragment. If the skill insists on mentioning A-17 in that new setting, it has preserved the example rather than the principle.

## Use the ready package or build your own

To try the ready version, download [write-clear-english.zip](../downloads/write-clear-english.zip), extract the folder and copy it into your project's `.opencode/skills` directory. Open that project, start a fresh session and explicitly request the skill. This is a project-local installation; nothing in the course installs it globally.

For the experiment itself, follow the [seven-lesson workbook](workbook.md). Its independent starters intentionally contain different stages. Do not replace all of them with the final package: doing so would remove the changes the lessons are meant to reveal.
