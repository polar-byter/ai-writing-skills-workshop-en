# Facts to preserve

The reader is an analyst who reviews approval requests and is seeing this explanation for the first time.
requests.csv contains request IDs, status and age in days.
status is the approval state; elapsed_days is the number of days since submission.
Select requests that are not approved and are older than two days.
A-17 has status=new and elapsed_days=3; A-18 has status=approved and elapsed_days=1.
A-17 qualifies. A-18 fails both conditions.
new means a new request awaiting approval; approved means approval is complete.
A five-day threshold is permitted only as an explicitly announced second experiment. Neither current row qualifies then.
No efficiency or KPI improvement has been measured.
No application name, button or automatic table-opening mechanism is specified. Do not invent one.
We are editing an explanation, not writing a request-filtering application.
