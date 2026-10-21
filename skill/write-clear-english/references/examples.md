# Revision techniques through examples

Use these as examples of a decision, not phrases to paste into every article.

## Restore the missing setting

Before: "In the current task, you can ask for Python notes. General rules control behavior."

After: "In a chat application you might type, 'Find notes about Python.' The application can also include a separate instruction asking the model to answer from the supplied notes. Our program will build both messages so we can inspect exactly what was sent."

The revision identifies where the person is working and how the instruction enters the request. It does not assume the reader already knows the surrounding application.

## Explain the operation that a vague location hides

Before: "The search ran, but the lines remained in Python."

After: "The search returned a list of matching lines, but the program has not included that list in a model request yet. We will record it with the command and send the updated history on the next call."

The meaningful distinction is whether the result was sent, not the place where a value supposedly remained.

## Preserve one action and its purpose

Before: "The model requests find_notes and a search for python."

After: "The model requests a search for python using the find_notes function."

Calling the tool and performing its search describe the same requested operation here. Do not turn the relationship into two independent tasks.

## Show why a rule matters

Before: "Check the status and age fields. Records meeting the conditions are selected."

After: "We are looking for requests that are still awaiting approval after more than two days. A-17 has status=new and elapsed_days=3, so it meets both conditions. A-18 is already approved and only one day old, so it is excluded."

The reader can now reconstruct the selection instead of guessing what the fields or conditions mean.

## Announce a changed example

Before: "Next the threshold is five days."

After: "For a second experiment, raise the age threshold from two days to five while keeping the same records. Neither current request will meet that stricter condition. Then return to the original two-day rule."

This is an intentional change with an observable consequence. It does not claim that the stricter threshold improves performance.

## Make a lesson's purpose visible

Before: "We will select a function by its name. This is dispatch."

After: "A model may return a tool name our application never provided. The dispatch_tool function will accept the two supported names and reject any other request before executing it. We will test that boundary with an invented name."

The definition follows the concrete reason for writing the function.

## Teach the value returned to the caller

Before: "Fill the first blank with json.loads(text) and the second with dict."

After: "The response text is a string containing JSON. json.loads(text) turns it into a Python value; check that this value is a dictionary, then return it. The caller can now read command['tool']. Returning the original string would leave that field access impossible."

The hints remain small, but the transformation and subsequent use are explicit.

## Ground professional relevance in a possible task

Before: "Using AI creates a need to understand how it works. This course unlocks new competencies."

After: "If a support assistant gives advice that contradicts a manual, someone needs to establish which fragment it received. The exercises give an analyst a way to inspect that transfer and prepare a case that can be checked again after a change."

This explains a condition under which the material is useful without inventing the reader's interests or promising a measured benefit.

## Distinguish a rule from a guarantee

Before: "The skill controls everything and prevents unsupported answers."

After: "The application loads the skill instructions into the model context. The instructions guide the response, but we still compare the answer with the supplied facts. A punctuation checker can flag characters; it cannot establish that the explanation is correct."

This keeps instructions, tool checks and observed output separate.
