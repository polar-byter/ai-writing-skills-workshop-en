---
name: write-clear-english
description: "Write and edit clear English articles, practical lessons and working instructions. Use when an explanation is hard to follow, a draft needs coherent reasoning, or a tutorial needs a concrete path from the reader's task to a checkable result."
---

# Write for someone who wants to understand

Help the intended reader understand the point, follow what happens and take the next useful step. Work on the explanation and its reasoning, not just sentence polish. The author's current request and constraints determine the assignment.

## Choose the relevant guidance

- For an article or substantial edit, read [reader-first.md](references/reader-first.md): reader interest, argument, transitions and voice.
- For a practical lesson or setup guide, also read [hands-on-lessons.md](references/hands-on-lessons.md): concrete data, partial implementations and observable checks.
- For examples of a revision technique, consult [examples.md](references/examples.md). Transfer the technique rather than repeating the same wording everywhere.
- For a spelling-only request, preserve meaning, scope and structure unless a correction requires a local adjustment.

Do not load every reference or turn a short answer into a chapter automatically.

## Recover the situation

Identify the reader, what they already know, the result they need and the role of this passage. Distinguish the author's background from the audience's. A programmer new to Python and an analyst new to code need different starting explanations.

Separate the purpose from the means. Writing a function may be an exercise for understanding an agent; launching an application may only be a way to observe a result. Make the title match what the material actually helps the reader understand or do.

Use supplied facts and inspect available current files when relevant. Do not restart completed work, ask for output you can read, invent UI labels or assume an experiment succeeded. Ask briefly for a consequential missing condition; for a harmless assumption, name it and continue.

These are editorial questions, not a questionnaire to print before every draft.

## Develop the explanation

Start with a recognizable situation and a concrete reason for the next action. Connect local work with the overall task. Job titles, business language and generic promises of efficiency do not establish a benefit on their own.

Before polishing a claim, check its basis and how the next sentence follows from it. A transition can explain, illustrate, compare or draw a supported conclusion. Do not invent motives, causes or a mechanism just to make the paragraph flow. A single example does not establish a universal rule.

Show the phenomenon or values before naming the concept. Use an example or comparison when it reveals the reason for an operation. Label an illustration as an illustration; an actual experiment requires an actual observation.

Write connected paragraphs. Join parts of the same thought with straightforward relationships, and pause when the thought changes. Simplicity does not require a separate short sentence for every fact. Avoid replacing choppy prose with long chains of subordinate clauses.

Before changing a query, data set, variable name, application or level of detail, explain what changes and why. Reconnect a side example with the main task afterward. A reader should not need to infer a missing transition.

## Preserve a human voice

Use precise verbs and meaningful names. Remove repetition and irrelevant detours rather than the explanation that supports the next step. Avoid textbook fragments, promotional claims, artificial aphorisms and professional shorthand that hides an operation.

Identify who acts, what they receive and what happens as a result. Add words such as "function", "file" or "dictionary" when a code identifier alone leaves its role unclear. Do not repeat those labels mechanically once the context is established.

Check what each modifier belongs to and which actions are being compared. Preserve distinctions between requesting, being allowed to act and actually acting. Do not describe an action and its purpose as two independent operations.

First-person authorship, a direct address to the reader and light humor can suit a tutorial. Do not invent the author's biography, measurements or experience. Preserve an agreed voice rather than normalizing it without a reason.

Use ordinary keyboard punctuation: straight quotes and apostrophes, hyphens, `->`, `<-` and `...`. Preserve valid Markdown, YAML, JSON and Python. Apply the same care to diagram labels. Do not silently change someone else's quotation; paraphrase when needed.

## Check the result

Read the passage with its neighboring sections. Are the source, actor, operation, reason and expected outcome clear? Do examples match the files? Does a title describe what follows? Has a useful distinction disappeared during shortening?

The optional [browser checker](assets/check-text.html) or `node scripts/check_text.js article.md` detects unusual punctuation. It does not edit files or assess meaning, factual accuracy, coherence or whether a skill was loaded.

Preserve the author's exercise implementations and intentional comments. Do not publish, install a skill globally or contact another service merely because a lesson describes doing so. Report the actual revision and checks separately from unperformed experiments.
