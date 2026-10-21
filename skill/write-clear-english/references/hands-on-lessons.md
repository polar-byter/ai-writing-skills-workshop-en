# Practical lessons without missing steps

Use with [SKILL.md](../SKILL.md) when a reader edits a function, configures an application or performs an experiment.

## Establish the task before its implementation

Show what the current program does, where it falls short and what completing the new part will change. Explaining that a function selects a tool by name describes an operation; showing how an invented tool name is rejected explains why the check matters.

Choose the reason from the actual task. Reading lines prepares a real source for search; recording an event makes a run inspectable. Do not frame every function as a safety mechanism or promise a business improvement the exercise does not measure.

Keep practice within a meaningful target function. Avoid unrelated console experiments that interrupt the learner's current implementation. Adjust the depth of an exercise without losing its place in the application.

## Restore context after a pause

Before an optional workbook or a later session, briefly remind the reader what program they are building, what a person asks it, who performs the operation and what data is transferred. Then introduce the current component and the exercise result. Recap only what the next action requires.

"The prepared decide_live already calls the model" does not explain why the application exists or what that call contains. Restore the concrete task before listing helpers. A link allows deeper review, but cannot carry all the context needed to follow the page.

## Show actual values and types

Introduce the data before its field names and operations. Identify a file path, file text, a list of lines, a dictionary, a parameter and a returned value as different things. Quote literal strings and make each argument's parameter clear when first introduced.

Use a prepared function beginning, a small unfinished template and a concrete hint for every blank. Explain the transformation on current values and who receives the result. Do not merely dictate `json.loads` and `dict`: show how a JSON string becomes a dictionary and how the caller then accesses the tool name.

Explain new language constructs briefly where they are used. A method description should cover the relevant argument or behavior, one simple example and its role in the current function. An optional note can hold broader detail; after it, remind the reader of the implementation in progress.

Distinguish returning from printing, writing a file, sending a request and executing a tool. These are different effects even when a demonstration performs them one after another.

## Name the exact next action

Identify the application, project folder, file, target function, Run action and output panel. For a download, verify the actual page and visible button rather than asking a beginner to guess which of several installation methods you meant.

After installation, check that the command is available before downloading a model. An editor already open during installation may retain its old environment. Verify the actual failure rather than declaring its cause from one error message.

Avoid extra accounts, an unfamiliar editor and infrastructure when a small local experiment is enough. Do not hide a required connection behind an optional "when you are ready" section if later lessons depend on it.

## Keep the experiment interpretable

Change one substantial factor at a time. Record the model, request and source when comparing behavior. A new session reduces carry-over from an earlier conversation, but does not make generated wording deterministic.

State success criteria before running. Source-grounded answers should be checked against the source; a Python function can be checked with known values. Parsing errors, unsupported generated claims and network failures require different investigations.

Separate a prepared fixture, an actual service request and local model inference. Reading a JSON file does not confirm API access. Loading instructions is different from the model claiming it followed them.

Preserve learner-written functions and intentional comments. Inspect saved work and run narrow relevant checks instead of requesting output you can access. Do not complete an exercise without authorization.

## Make diagrams explain a change

Use a readable compact width, usually around 480 pixels, with a static alternative. Label an illustration, conceptual route or recording honestly. Review labels as carefully as paragraphs.

An animation should show what moves or changes: data before and after processing, a growing matches list, a parsed dictionary or a tool result returning in the next model request. Highlighting an unchanged block can guide attention, but does not explain the process by itself. Give values time to be read and retain enough state to connect consecutive operations.

For an agent loop, show the return route and what the model receives on the next call. The static version should preserve the essential route rather than displaying only the final frame. Check the diagram against the real code: parsing a command does not execute it, and completing a write does not mean tests passed.

## Preserve the learning contract

Independent starters should prepare previous components, leave the current function unfinished and avoid requiring future work for the current check. Keep file names, data contracts and the launching method aligned between the lesson and TASK.md. Do not overwrite a learner's extracted project.

Close a substage by tracing the implemented path: where the rule originated, where the data entered, who sent the request and who received the result. Ready-made helper code can be explained in an optional note through its input, operations and output.

## A short map at the start of a lesson

A beginner does not keep the whole course in mind. Open each lesson with two or three lines of "Where we are": what we are building, which step this is and how it connects to the previous one, with a one-line diagram if it helps, such as `file -> [reading] -> search -> model`. This replaces retelling the introduction.

## Balance reading and doing

Count how much the reader reads before the first action and how much they do themselves. If several screens of text lead to filling two blanks in an almost finished function, the reader does not feel they did anything. Trim the explanation to what this step needs and move optional material (type hints, an alternative spelling, background) into a short note at the end.

Give the most detail where beginners get stuck most often: installation, choosing an interpreter, the first connection. There, name exact menu items, the expected screen and the error message the reader may see. Keep simple steps short.

## Guess, run, break

Before a run, ask a question the reader can answer: "Guess before running: how many lines will the function return?" After the run, bring them back to their guess. This holds attention better than any argument about usefulness.

After a working result, add a "Try to break it" section: remove one condition, pass an empty value, rename a file. Let the reader see the message that appears and what it means, then restore the code. Warnings about possible mistakes fit better here than in the middle of an explanation.
