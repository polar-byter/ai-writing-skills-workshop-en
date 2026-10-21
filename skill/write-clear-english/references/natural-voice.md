# A human voice without machine-writing tells

Use with [SKILL.md](../SKILL.md) before handing over any text. Readers rarely say why a text feels machine-written, but they notice quickly and read the rest with suspicion. Below are the patterns that give it away and how to remove them. Each one also appears in human writing; what raises suspicion is a cluster of them.

## How to check

Read the text straight through as the reader would and mark where you stumbled or where a sentence is "correct, but nobody talks like that". Then go through the list below. The script `node scripts/check_style.js text.md` finds some of these patterns automatically, but the editor decides: a flagged phrase is fine when the meaning needs it.

When you fix a pattern, do not swap one stock phrase for another. Go back to the thought: what did the author mean at this point? Say that directly, in words from the reader's situation.

## Looking at people from outside

A model often describes people as an observer who is not one of them.

Weak: "The file looks the way documents edited by humans usually look."

Better: "There are stray spaces before the second point and a blank line after it - files often end up like that after a few rounds of edits."

The same goes for "users typically...", "people tend to...", "many individuals struggle with...", when the author is writing to a person about a concrete situation. Describe the situation, not people in general.

## Treating the program as a person

Weak: "The function returns an empty list. That is an honest answer: the file was read and has no notes."

Better: "The function returns `[]`: the file was read and has no notes."

Programs are not honest, polite, confident or confused, and a model does not "want" or "try". If a figure of speech really helps explain a mechanism, use it once and say what it stands for.

## A disclaimer closing every paragraph

The most recognizable pattern. A paragraph explains something, and its last sentence hedges: "This does not prove...", "This is not a guarantee that...", "The example is illustrative, not a recording of a real run", "Results may vary."

A caveat belongs where a reader could really draw the wrong conclusion, and once, not after every diagram and every exercise. If a limitation applies to the whole piece, state it in one place. If it is obvious, drop it.

Weak (under each of nine diagrams): "These are illustrative values and steps, not a recorded model run."

Better: say once, in the introduction, that the diagrams show the order of steps and that the reader will get the real model output in their own run.

## "Not X, but Y" in a row

The construction works when the reader genuinely confuses X and Y. Three of them in a paragraph sound like an advertisement or a sermon.

Weak: "The manager sees not a black box but a set of control points. This isn't magic - it's engineering. What matters is not the answer but the path to it."

Better: "The manager knows where the agent's control points are: what data it gets, what it may do, where it must stop and ask a person."

Related forms: "isn't just X, it's Y", "it's not about X, it's about Y", "more than just a...".

## Triplets and even lists

Models reach for three parallel items: "faster, safer and more transparent", "configure, check and stop at any moment". A triplet sounds complete, so it gets inserted by habit even when the meaning needs one item or five.

Weak: "Such a system can be configured, verified and stopped at any time."

Better: "When something goes wrong, you know where to step in."

Keep a list when every item adds something the reader can picture on its own.

## Aphorisms and slogan conclusions

Weak: "So most questions about an agent are really questions about its harness." "That is the deeper competence." "A convincing paragraph is only part of the job."

Better: say what follows for the reader: "So when an agent gets something wrong, the cause is usually in the harness."

Signals: "this is exactly", "at the end of the day", "that's the whole point", "here's the thing", a five-to-seven-word sentence at the end of a paragraph that could go on a poster.

## A rhetorical question answered at once

Weak: "Why learn this hands-on rather than from articles? Because many things only become clear through practice."

Better: "Much of this only becomes clear in practice."

A question to the reader works when they should actually stop and think: "Guess before running: how many lines will the function return?" A question the author answers in the next breath only slows the reader down.

## Generic openings and summarizing endings

Weak openings: "In today's fast-paced world...", "AI is rapidly transforming...", "Let's dive in", "In this article, we will explore...".

Better: start with an event or with data, or go straight to the case.

Weak endings: "In conclusion...", "To sum up...", "This is the difference we started with."

Better: return to the opening example concretely: "Back to the example from the start: an empty list means the document itself needs content."

## Vocabulary models overuse

"Delve", "leverage", "seamless", "robust", "crucial", "pivotal", "navigate the complexities", "unlock the potential", "a testament to", "tapestry", "landscape", "realm", "embark", "foster", "elevate", "game-changer", "it's worth noting", "it's important to note", "moreover" and "furthermore" at the start of every other sentence. If a sentence starts with "It's worth noting that", just state the point; if there is no point, delete the sentence.

## Even rhythm

Paragraphs of the same length, four or five sentences each, every sentence starting with "This", "Here", "Now" or "So". Human text is uneven: one thought takes a sentence, another a paragraph; some sentences open with an example, others with an action. Do not level the paragraphs, and do not start several sentences in a row with the same word.

Do not swing into choppiness either: "The model returns a name. The function checks the name. Then it calls the function." sounds just as artificial. Join the parts of one thought, as described in [reader-first.md](reader-first.md).

## Internal notes leaking to the reader

A model sometimes leaves in reader-facing text what was an instruction to itself or to the editor: "Do not claim a model comparison from file validation alone", "Do not describe a suggested command as executed." The reader does not understand such lines, and they reveal where the text came from. Internal rules stay in working notes.

The same goes for one action described twice in a row in different words ("Open demo.py and choose Run... Open demo.py and run it"): a trace of stitched fragments.

## Instructions by prohibition

Weak: "You do not need to add this to notes.py. You do not need to type these assignments. Do not create a second function with the same name."

Better: say what to do, once, and where a mistake is actually likely. Each unnecessary prohibition suggests the author does not trust the reader and pulls attention from the task.

The same applies to warnings about mistakes a beginner has not made yet. Show such a mistake when it can actually happen, or in a "try to break it" section.

## An invented author persona

Do not write "as a programmer, I..." or "once I..." on the author's behalf, and do not rework stories found online into their personal experience. If the author wants lively examples and the material contains none of their own experience, use a situation without a narrator ("Imagine a team that...") or a published case with a link. A concrete situation persuades without a storyteller.
