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
- For an introduction, a "who this is for" section or any place where you explain why the reader needs the material, read [motivation.md](references/motivation.md).
- Before handing over any text, check it against [natural-voice.md](references/natural-voice.md): it lists the patterns by which readers recognize machine-written prose.
- For a spelling-only request, preserve meaning, scope and structure unless a correction requires a local adjustment.

Apart from natural-voice.md, open references when the task needs them rather than all at once, and do not turn a short answer into a chapter.

## Recover the situation

Identify the reader, what they already know, the result they need and the role of this passage. Distinguish the author's background from the audience's. A programmer new to Python and an analyst new to code need different starting explanations.

Separate the purpose from the means. Writing a function may be an exercise for understanding an agent; launching an application may only be a way to observe a result. Make the title match what the material actually helps the reader understand or do.

Use supplied facts and inspect available current files when relevant. Do not restart completed work, ask for output you can read, invent UI labels or assume an experiment succeeded. Ask briefly for a consequential missing condition; for a harmless assumption, name it and continue.

These are editorial questions, not a questionnaire to print before every draft.

## Develop the explanation

Start with a recognizable situation and a concrete reason for the next action. Connect local work with the overall task. Job titles, business language and generic promises of efficiency do not establish a benefit on their own.

A published real case with a link persuades more than an invented story. Without one, present a situation as a supposition ("Suppose...", "Imagine a team that...") and do not claim it happened. The example that opens a piece should run through it: later lessons and the conclusion return to it. Take the example's data from the reader's world.

Build motivation from what matters to the person in their role, not from usefulness in general: depth of competence for an analyst, control for a manager, responsibility for access for an administrator. See [motivation.md](references/motivation.md).

Before polishing a claim, check its basis and how the next sentence follows from it. A transition can explain, illustrate, compare or draw a supported conclusion. Do not invent motives, causes or a mechanism just to make the paragraph flow. A single example does not establish a universal rule.

Show the phenomenon or values before naming the concept. Use an example or comparison when it reveals the reason for an operation. Label an illustration as an illustration; an actual experiment requires an actual observation.

Write connected paragraphs. Join parts of the same thought with straightforward relationships, and pause when the thought changes. Simplicity does not require a separate short sentence for every fact. Avoid replacing choppy prose with long chains of subordinate clauses.

Before changing a query, data set, variable name, application or level of detail, explain what changes and why. Reconnect a side example with the main task afterward. A reader should not need to infer a missing transition.

## Preserve a human voice

Use precise verbs and meaningful names. Remove repetition and irrelevant detours rather than the explanation that supports the next step. Avoid textbook fragments, promotional claims, artificial aphorisms and professional shorthand that hides an operation.

Identify who acts, what they receive and what happens as a result. Add words such as "function", "file" or "dictionary" when a code identifier alone leaves its role unclear. Do not repeat those labels mechanically once the context is established.

Check what each modifier belongs to and which actions are being compared. Preserve distinctions between requesting, being allowed to act and actually acting. Do not describe an action and its purpose as two independent operations.

First-person authorship, a direct address to the reader and light humor can suit a tutorial. Do not invent the author's biography, measurements or experience, do not write "as a programmer, I..." on their behalf, and do not rework stories found online into their own. Preserve an agreed voice rather than normalizing it without a reason.

Use the terms readers will meet in articles and discussions: LLM, prompt, context window, tokens, RAG, hallucination, tools, function calling, MCP, agent loop, prompt injection, evals. Explain a term where there is already a concrete action behind it, and do not load one paragraph with several new terms.

The text must not read as machine-written. The most common tells: looking at "people" from outside, treating a program as a person, a disclaimer closing every paragraph, "not X, but Y" in a row, triplets, slogan conclusions, rhetorical questions answered at once, stock words such as "delve" or "seamless". The full list with fixes is in [natural-voice.md](references/natural-voice.md).

Use ordinary keyboard punctuation: straight quotes and apostrophes, hyphens, `->`, `<-` and `...`. Preserve valid Markdown, YAML, JSON and Python. Apply the same care to diagram labels. Do not silently change someone else's quotation; paraphrase when needed.

## Check the result

Read the passage with its neighboring sections. Are the source, actor, operation, reason and expected outcome clear? Do examples match the files? Does a title describe what follows? Has a useful distinction disappeared during shortening?

Read it again as a beginner who opened it after a break. Is it clear from the first lines where they are and what they are doing? Did they have to read several screens before the first action? Is usefulness argued in several paragraphs in a row? Are there more "you do not need to" lines and warnings about mistakes they have not made than instructions about what to do?

Then read it as an editor hunting for machine-written patterns from [natural-voice.md](references/natural-voice.md). For a first pass, `node scripts/check_style.js article.md` marks common stock phrases and caveats; it does not decide whether a phrase is bad, only where to look.

The optional [browser checker](assets/check-text.html) or `node scripts/check_text.js article.md` detects unusual punctuation. It does not edit files or assess meaning, factual accuracy, coherence or whether a skill was loaded.

Preserve the author's exercise implementations and intentional comments. Do not publish, install a skill globally or contact another service merely because a lesson describes doing so. Report the actual revision and checks separately from unperformed experiments.

## Check the whole publication

When a text goes into a repository, onto a site or into a lesson archive, the reader sees more than that text. Next to it are the README, maintainer notes, change logs, `TASK.md` and other files inside archives, image captions and commit messages. Machine-written phrasing survives there most often, because nobody rereads those texts as the author's own.

Before publishing, run `check_style.js` and `check_text.js` on every text file, not only the main one, and look inside the archives. When you fix a phrase in one place, find its copies: in the task hints, in the archive, in the edition in another language.

Write maintainer texts the way the author would: impersonally ("Four lessons added") or in the first person. Do not refer to the author in the third person ("the owner asked", "the author clarified", "at the author's request"): that is how an assistant reports to a client. Keep instructions for a model or agent (`AGENTS.md`, rules such as "record decisions in the log") with the working notes and out of the publication. Examples are in the section on internal notes in [natural-voice.md](references/natural-voice.md).
