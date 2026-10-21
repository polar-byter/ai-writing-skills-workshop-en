# Prompts for using the ready skill

Use these after checking that your application can load `write-clear-english`. Replace bracketed fields with actual material. A prompt specifies the current task; it does not prove the skill or its references were loaded.

## Edit an explanation

```text
Load the write-clear-english skill. Edit the draft below for [reader] who wants to [task].
Use only the supplied facts. Preserve the important conditions and examples.
Make the reasoning and transitions clear without expanding it into a reference manual.
If a cause or measurement is not supplied, do not invent one to make the text persuasive.

Facts:
[facts]

Draft:
[draft]

Return the edited text, followed by a short note about any factual gap that still affects it.
```

## Write a practical lesson

```text
Load write-clear-english and its hands-on lesson guidance.
The reader is [background]. We are building [application].
The current function is [name] in [file]. Its input is [actual values].
Previous components are [prepared components]. The current starter is [folder].

Explain why this step is needed, show the data, provide a small unfinished function
and give a concrete hint for each blank. Name the exact file, Run action and expected
observable result. Keep broader language detail in a short optional note.
Do not implement the learner's saved exercise or claim a run that has not occurred.
```

## Explain a ready-made helper

```text
Load write-clear-english. The reader last saw this project some time ago.
Briefly restore the task and data path before introducing the helper below.
Trace its input, meaningful operations, returned value and what the caller does next.
Distinguish file access, network sending, parsing and tool execution.

Project context:
[context]

Code:
[code]
```

## Review a draft without rewriting it first

```text
Load write-clear-english. Review this passage for a reader with [background].
Identify concrete gaps in reasoning, missing context, unexplained example changes
and professional shorthand that hides the operation. Preserve the author's intent.
For each important issue, explain the missing relationship and suggest a local revision.
Keep observations separate from assumptions. Do not turn one awkward phrase into a
universal ban or claim that a punctuation check establishes editorial quality.

[passage]
```
