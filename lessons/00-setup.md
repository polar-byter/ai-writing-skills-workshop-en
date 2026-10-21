# Prepare the workspace

We will turn editorial observations into a reusable writing skill. First establish a place to keep the source, facts and results, and confirm that the application can answer a small request. Keeping this setup separate means a later failure to load a skill will not be confused with a missing model connection.

## Open this experiment

Download [writing-00-setup](../downloads/writing-00-setup.zip), extract it into its own folder and open that folder in OpenCode. Use a plain text editor for the lesson files. Earlier parts are prepared; the current change is yours to make. Keep previous outputs in their original folders so comparisons remain possible.

## Perform the experiment

Open the [OpenCode download page](https://opencode.ai/download). Under **OpenCode Desktop**, choose **Windows (x64)** if that matches your computer; use the appropriate platform download otherwise. Download and open the installer, complete installation and start OpenCode Desktop. These steps concern the desktop application, not the terminal installer commands displayed elsewhere on the same page.

Extract this lesson's archive. Open its `writing-00-setup` folder as the project in OpenCode. Use a plain text editor to inspect `source.md`, `facts.md`, `requests.csv` and `results/observations.md`. On Windows, turn on **View -> Show -> File name extensions** in File Explorer so a file called `SKILL.md.txt` will not be mistaken for Markdown.

In the application's model selector, choose an available model. The [official model catalog](https://opencode.ai/v2/docs/console/models/) lists temporary free models, including Big Pickle as checked on 2026-10-22. Choose an explicitly free option if offered to your account and record its exact name. Availability can change; the catalog, rather than a promise in this lesson, determines the current conditions. A model connection you already have is also suitable. Do not buy a subscription merely to reproduce a small writing experiment if a suitable available option works.

Create a new session and send the contents of `PROMPT.md`. A short answer establishes that requests reach a model. In `results/observations.md`, record the date, application version, model and actual reply. No skill is installed in this starter. The next lesson will use the supplied draft and facts.

<img src="../assets/step-00.gif" width="480" alt="Experiment 0: Prepare the workspace">

[Static alternative](../assets/step-00.png). These are illustrative values and steps, not a recorded model run.

## What to record

You can identify the opened folder, find each input file and receive a model reply. This confirms the application connection, not skill discovery or writing quality. If the model is unavailable, resolve that connection before editing skill files.

Use `results/observations.md` to separate the changed instruction, observed loading and actual output. Do not claim a model comparison from file validation alone.

[All lessons](../README.md#lessons).
