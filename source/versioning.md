
## Task Management

TaskBeacon supports **task variant tracking** to promote transparency, reproducibility, and collaboration across the research community. Task variant tracking allows the community to build on shared paradigms while keeping modifications clear and organized. It encourages open science and makes experimental replication easier — without losing flexibility.

**Why it matters**: There are countless modifications of popular cognitive tasks in circulation — different stimuli, reward types, modalities, or participant populations. 
Without proper tracking:
- It becomes hard to understand what version was actually used.
- Reproducibility is compromised.
- Collaborative improvements or comparisons are inefficient.

By explicitly documenting task variants, TaskBeacon ensures that users can trace the origin of a task, understand what changed, and reuse versions that best match their research needs.

**How It Works**: Each task in TaskBeacon is hosted in its own GitHub repository. **Variants of a task are stored as Git branches**, with each variant accompanied by a `README.md` file at the root of that branch.

An Example Structure looks like this:
```
sst/
├── main/
│ └── README.md ← base version
├── audio_sst/
│ └── README.md ← describes the audio-based SST 

(not accepted as variant)
├── fast_response_version/
│ └── README.md ← minor timing changes 
```

### What Counts as a Variant?

Not all changes are meaningful enough to count as a separate variant. 

Here’s a general guideline:

✅ Counted as a variant:
- Changing the type of feedback or stimuli (e.g., replacing visual stop signals with audio in SST;Switching from monetary to social rewards in MID)
- Adding or modifying experimental conditions in a non-trivial way

❌ Not counted as a variant:
- Minor adjustments to trial timing
- Changing font sizes or button positions
- Cosmetic or layout-only changes

Variant contributions are reviewed and approved by TaskBeacon's administrative team to ensure they meet the standard for meaningful differentiation.


.. image:: _static/versioning.png
   :alt: Illustration of Task management
   :align: center
   :width: 85%

### Contribute a Variant

To contribute a new task variant:

1. **Fork** the GitHub repository of the base task.
2. **Create a new branch** for your variant (e.g., `social_reward_MID`).
3. **Modify the task code** as needed.
4. **Add a `README.md`** to the root of your branch. This file should:
   - Describe the purpose of the variant.
   - Explain how it differs from the `main` branch or original task.
   - Include your name and affiliation (optional but encouraged).
5. **Submit a pull request or contact the admin team** to get your branch reviewed and published on TaskBeacon.


### Contribute a New Task

If you want to contribute an entirely **new task** that doesn’t exist in TaskBeacon yet:

1. **Create a new public GitHub repository** under your own GitHub account or organization.
2. Structure the task according to the [TAPS format](https://taskbeacon.github.io/taps/).
3. Include a `README.md` with:
   - A brief overview of the task
   - Instructions for running it
   - Required dependencies or setup instructions
4. When ready, **submit the task** to TaskBeacon by opening an issue or contacting the admin team.
5. The TaskBeacon team will **review and fork** your repository under the official TaskBeacon GitHub organization for indexing.

This workflow ensures that tasks are standardized, documented, and easily discoverable through the TaskBeacon platform.


### Behind the Scenes: How Variants Get Indexed

TaskBeacon uses a script (`fetch_all_task_variants.py`) to automatically scan task repositories, detect branches, and build a browsable index for the website.

**Here's how it works**:

1. The script queries GitHub’s API to retrieve all public repositories under the TaskBeacon organization.
2. For each repository (excluding core tools like `psyflow` or documentation repos), it:
   - Lists all branches
   - Tries to download the `README.md` file from each branch
   - If found, saves it locally and registers the branch as a valid variant
3. For each task with one or more variants:
   - A task-specific index file is created listing all branches
   - This gets compiled into the global `Task Library` page on the TaskBeacon site

**Key Logic (Simplified)**

```python
# For each repo
branches = fetch_branches(repo)
for branch in branches:
    readme_url = f"https://raw.githubusercontent.com/TaskBeacon/{repo}/{branch}/README.md"
    if download(readme_url):
        # Register the branch as a variant
        add_to_index(branch)
```

This automated process ensures the Task Library always stays up to date with newly submitted variants.


### Browse Tasks and their Variants

You can explore all registered task variants in the [Task Library](https://taskbeacon.github.io/task-registry/). Each entry includes a short description and links to the associated branch on GitHub.




