# Why the reader needs this material

Use with [SKILL.md](../SKILL.md) when writing an introduction, a "who this is for" section, or explaining why the next step matters.

## Motivation comes from the role, not from usefulness in general

Formal usefulness persuades almost nobody. "Requirements like these can be verified, so they can be agreed with the developers" sounds reasonable, but no analyst learns a new tool for that. People invest effort in learning when it changes their position at work: it gives them strength others lack, removes a fear or gives them back control.

So for each role, ask: what in this person's work causes worry or a sense of dependence, and what gives them confidence and weight? Build the argument from that.

| Role | What matters | How the argument sounds |
|---|---|---|
| Analyst | Depth of competence, an edge over peers, a seat in the project from the start | Many analysts can specify an ordinary integration; few understand an LLM integration, and developers can work with them in the same language |
| Manager, process owner | Control, accountability for the result | An agent known only as "it handles everything" is a black box; trusting it means giving up control over work you are still accountable for |
| System administrator, DevOps | Responsibility for access to systems, the right to say no | Whoever knows that an agent's permissions live in harness code, not in the prompt, decides whether it may touch the servers |
| Support, QA | Getting out of "the bot got it wrong again and I can't do anything" | Showing exactly which step failed makes them indispensable to the rollout team |
| Domain expert | Recognition of their knowledge as the basis of the system | They know which source is current and what counts as a correct answer |

The table is a guide, not a template. Take the roles that are really among your readers and phrase the argument in their words.

## Back the argument with an event

An abstract "this reduces risk" does not work. Tie the argument to something the reader can picture. For a manager, a published case where a company had to answer for its chatbot's mistake. For an administrator, an instruction hidden in a log file that an agent executed as a command. For an analyst, a requirement like "the bot should answer correctly", which nobody can estimate or accept.

Retell a published case with a link and without adding details the source does not contain. Present a situation without a source as a supposition ("Suppose...").

## What to avoid

- A list of competencies copied from a job ad: "lays the groundwork for systems analysis, agent solution design and systems integration". Readers skip such lines.
- Fear of missing out and career promises: "without this you will be left behind", "master the profession of the future".
- Persuading in several paragraphs in a row. One strong argument per role beats five weak ones. A reader who is already convinced gets bored by more convincing.
- Motivation unconnected to the content. If you promise an analyst the ability to specify an LLM integration, the material has to deliver it: the lessons must show which data goes into the context and where it can get lost.

## Motivation inside a lesson

Within a lesson the argument is shorter: one situation where the current step is needed. Returning to the running example works well: "Recall the case from the introduction: the right paragraph never reached the model. The first thing to check is whether the program found it." The reader sees which question from the larger story today's function answers.

If a step is technical and dull in itself, show on concrete data which problem it prevents: "If the program reports a missing file and an empty file with the same message, the question goes to the wrong person."
