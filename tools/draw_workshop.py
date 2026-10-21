"""Render illustrative skill-loading and editing experiments at 480 px."""
from pathlib import Path
from drawing import render

ROOT = Path(__file__).resolve().parents[1]


def step(action, before, after, explanation, packet='data'):
    return dict(action=action, source='Before this operation', before=before,
                destination='After this operation', after=after, explanation=explanation, packet=packet)


STORIES = [
    ('skill-workflow', 'How a skill reaches the answer', [
        step('Discover the relevant skill', 'Current task: edit the supplied draft.', 'Available name and description:\nwrite-clear-english', 'Discovery metadata identifies a capability; its body is not loaded merely by being listed.', 'description'),
        step('Load the instruction and reference', 'skill: write-clear-english', 'SKILL.md body\n+ the relevant reference', 'Inspect actual loading in the activity trace.', 'instructions'),
        step('Edit and check the result', 'Current draft, facts and instructions', 'An edited explanation\n+ a separate check report', 'Illustrative output: no live improvement is claimed by this diagram.', 'answer'),
    ]),
    ('experiment-cycle', 'One changed factor per experiment', [
        step('Keep the comparison conditions', 'The same draft, records and model', 'A saved baseline answer', 'Save actual output rather than an improved version of it.', 'baseline'),
        step('Add one instruction', 'Previous skill version', 'Previous rules + one new criterion', 'Changing several factors would obscure what caused a difference.', 'one rule'),
        step('Run again in a fresh session', 'Same editing prompt; updated skill', 'New actual answer and loading trace', 'Compare defined criteria, not exact wording.', 'compare'),
    ]),
    ('step-00', 'Prepare a visible starting point', [
        step('Open the extracted project', 'writing-00-setup', 'source.md, facts.md, requests.csv', 'These files make the task and evidence inspectable.', 'files'),
        step('Choose an available model', 'Record the exact model name.', 'A short request asking for READY', 'No skill is installed in this first stage.', 'request'),
        step('Record the actual reply', 'The model response', 'results/observations.md', 'This checks connection, not skill discovery or writing quality.', 'record'),
    ]),
    ('step-01', 'Save an unassisted baseline', [
        step('Supply the draft and facts', 'A-17: new, 3 days\nA-18: approved, 1 day', 'An editing request with those same facts', 'The original condition is unapproved and older than two days.', 'prompt'),
        step('Receive an ordinary edit', 'No project skill yet.', 'Save the actual baseline answer.', 'The output may already meet some criteria.', 'baseline'),
        step('Check against the source facts', 'The answer and facts.md', 'Both conditions?\nAnnounced five-day experiment?\nAny invented benefit?', 'Record observations without rewriting the saved baseline.', 'review'),
    ]),
    ('step-02', 'Create and observe the first skill', [
        step('Complete the skill metadata', 'name: write-clear-english\ndescription: empty', 'A specific description and one rule', 'Keep folder name, frontmatter and exact SKILL.md filename aligned.', 'save'),
        step('Request the named skill', 'Same source and facts in a new session', 'Inspect the skill loading action.', 'A model saying it used the skill is not evidence of loading.', 'load'),
        step('Compare with the baseline', 'Actual new answer', 'Were unsupported measured claims avoided?', 'Loading and editorial effect are separate observations.', 'compare'),
    ]),
    ('step-03', 'Explain fields through actual records', [
        step('Add a reader-and-data rule', 'Fields: status and elapsed_days', 'Require meaning and both conditions.', 'Describe the desired understanding, not a fixed favorite sentence.', 'rule'),
        step('Use the same two records', 'A-17: new, 3\nA-18: approved, 1', 'A-17 qualifies; A-18 does not.', 'The explanation should connect each outcome to the values.', 'values'),
        step('Announce the changed threshold', 'Original threshold: two days', 'Second experiment: five days\nNeither record qualifies.', 'A changed example needs a reason and a clear transition.', 'transition'),
    ]),
    ('step-04', 'Load a reference when it is relevant', [
        step('Write a reference example', 'The same two-day and five-day cases', 'references/reader-first.md', 'The example illustrates a technique, not mandatory record IDs for every task.', 'reference'),
        step('Add a loading condition', 'A resource exists beside SKILL.md.', 'SKILL.md links it and says when to read it.', 'File proximity does not load the content automatically.', 'routing'),
        step('Inspect two loading events', 'A fresh session and the same prompt', 'Skill body loaded\nReference read separately', 'Reorganization alone does not prove a better answer.', 'trace'),
    ]),
    ('step-05', 'Separate character checks from meaning', [
        step('Give the checker actual text', 'A saved answer or pasted paragraph', 'A character report with line positions', 'The checker identifies unusual punctuation and separators.', 'text'),
        step('Interpret the report narrowly', 'No unusual characters found.', 'This says nothing about selection logic.', 'A false claim can contain only ordinary keyboard characters.', 'report'),
        step('Review facts separately', 'The answer and original records', 'Correct fields, conditions and transitions?', 'Mechanical checks support but do not replace editorial review.', 'review'),
    ]),
    ('step-06', 'Try a different task and project', [
        step('Change the explanation deliberately', 'New task: answer from a policy fragment.', 'Current facts replace the approval-table facts.', 'The new answer should not mention A-17.', 'new input'),
        step('Check the transferred principle', 'A skill provides instructions.', 'It does not grant file access\nor guarantee model compliance.', 'Preserve the distinction between a rule and an observed result.', 'principle'),
        step('Open a separate local project', 'Copy the project with its local skill.', 'Observe loading in a fresh session there.', 'Record portability and remaining uncertainty, without a global installation.', 'load'),
    ]),
]


def main():
    for name, title, scenes in STORIES:
        render(dict(path='assets/' + name + '.gif', title=title, scenes=scenes), ROOT, ROOT / '.checks/flow-review')


if __name__ == '__main__':
    main()
