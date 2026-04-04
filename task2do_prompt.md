Your task is to process the following tasks strictly one by one, using a per-task loop.

Tasks:

Risk Perception Estimation
Game of Dice Task
Two-Armed Bandit
Probabilistic Reward Task
Probabilistic Stimulus Selection
Psychomotor Vigilance- Probabilistic Stimulus Selection
Fixed-ratio Satiation Schedule
Trier Social Stress Test (TSST)
Temporal Bisection Task
Tapping Synchronization Task
Hand Laterality Judgment
Anti-Reach Task (motor inhibition)
Language-based Visual World Paradigm
Raven’s Progressive Matrices
Matrix Reasoning
Mental Rotation Task
Serial Reaction Time Task
Paired-Associate Learning Task
Transitive Inference Task
Acquired Equivalence
Delayed Recall Task
Rey Auditory Verbal Learning Test (RAVLT)
California Verbal Learning Test (CVLT)
DRM False Memory Paradigm
Object-Location Memory Task
Visual Paired Comparison Task
Mnemonic Similarity Task (pattern separation)
Self-Ordered Pointing Task
Letter–Number Sequencing
Keep-Track Task


Execution rule:
Do not run task-build, task-plot, and task-py2js as three separate batch passes across all tasks. Instead, complete the full pipeline for one task before moving to the next.

Required per-task procedure:
1. Lock one task at a time.
2. Treat the local `Txxxxx-*` folder as the canonical source.
3. Treat the matching `Hxxxxx-*` folder as derived output.
3.5. For task IDs we have rule in determining the IDs and you need to check the existing task IDs in taskbeacon and avoid overlap.
4. Run `task-build` first on that task.
   - For already-built tasks, this is an audit / verification / repair pass, not a full rewrite.
   - Repair references or task structure only if needed.
5. Run `task-plot` second on the same task.
   - Refresh `task_flow.png`.
   - Refresh all plot-audit outputs.
   - Only do this after the build state is stable.
   - visually check if the task_flow.png is good (no overlap, no incorrect stimulus, no incorrect ratio/scale), otherwise iterate this for max 5 rounds  uisng `task-plot` skill
6. Run `task-py2js` last on the same task.
   - Sync the web task from the now-stable local canonical task.
7. Validate build / gates / QA / simulation / web-port checks for that single task.
8. Only when the current task is fully green across build, plot, and web-port checks:
   - mark it as done in the todo list
   - update the queue
   - move to the next task
9. If the task is already exists, then skip the task
10. after above steps done, push both python and js version task to taskbeacon

Critical constraints:
- Do not process multiple tasks in parallel.
- Do not do build for all tasks first, then plot for all tasks, then py2js for all tasks.
- Do not start the next task until the current task has passed the full pipeline.
- Work task by task until the last task, end to end.
- After each completed task, record its status in the todo list immediately.

In short:
Use this loop for each task:
`task-build -> task-plot -> task-py2js -> QA/validation -> mark done -> next task`

Follow this procedure exactly