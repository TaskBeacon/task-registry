
## Overview

This repository serves two main purposes:

1. **Task Indexing and Documentation**: It provides a centralized index of all tasks hosted under the TaskBeacon platform, rendered using [Sphinx](https://www.sphinx-doc.org/) with the [Furo](https://pradyunsg.me/furo/) theme for clean, readable documentation.

2. **Community Task Proposals**: It acts as the entry point for researchers to propose new tasks via GitHub Issues, following a structured template and review process.
> **Note**: If your task is a variant of an existing task, please submit it as a new branch in the original repository instead of creating a new task proposal. Variants can be added as branches like  `variant/sst-audio`, etc.


### Step-by-Step: Submitting a New Task to TaskBeacon

#### 1. Make Sure Your Task Follows the TAPS Format

Ensure your local task folder includes the standard TAPS structure:

```arduino
your-task/
├── assets/
├── config/
│   └── config.yaml
├── src/
│   ├── main.py
│   ├── run_trial.py
│   └── utils.py         # optional
├── analysis/
│   └── analysis.py      # optional
├── data/                # empty or example output
├── README.md            # generated via task2doc or manually written
```

> Note: psyflow command line tool psyflow-init (or the taps() function) helps researchers quickly generate a project skeleton with these components pre-wired.

#### 2. Push to Your Own GitHub Repo (if not already)
Create a public repository under your GitHub account (e.g., `stroop`), then push your files:

```bash
git init
git remote add origin https://github.com/yourname/stroop.git
git add .
git commit -m "Initial version of emotional stroop task"
git push -u origin main
```

### 3. Go to the Task Submissions Repository

Visit:

```text
https://github.com/taskbeacon/task-registry
```

#### 4. Open a New Issue Using the Template

- Click “New Issue”
- Select **New Task Proposal** (if configured)
- Fill in the form with:
  - Task name
  - Suggested repo name (e.g., `stroop`)
  - Short description of what the task measures
  - Link to your GitHub repo
  - Checkboxes for files included
  - Author and license info
  - Completion of the TAPS/psyflow checklist

New task proposal form template:

```markdown
---
name: 🧪 New Task Proposal
about: Propose a new cognitive task to be added to the TaskBeacon platform
title: "[Task Proposal] <Task Name>"
labels: new-task, review
---


**Task Metadata**

| Field                  | Value                                       |
|------------------------|---------------------------------------------|
| **Task Name**          | e.g., Stroop, Go/No-Go            |
| **Suggested Repo Name**| e.g., stroop                  |
| **Short Description**  | Briefly describe what this task measures    |
| **GitHub Repo URL**    | https://github.com/username/task-name       |
| **Author(s)**          |                                             |
| **License**            | e.g., MIT, CC-BY-4.0                        |
| **References**         |                                             |

---

**Paradigm Summary**

| Component              | Description                                 |
|------------------------|---------------------------------------------|
| Number of Blocks/Trials| e.g., 3 blocks × 60 trials                  |
| Stimulus Type          | e.g., words, images, video                  |
| Response Modality      | e.g., keyboard, mouse                       |
| Feedback Provided?     | Yes / No                                    |
| Adaptive Logic?        | Yes / No (describe briefly if Yes)          |

---

✅**Submission Checklist**
- [ ] The task is not variant of existing tasks (if it is a variant, please add it as a variant through PR)
- [ ] YAML configuration conforms to the TAPS structure
- [ ] Task logic uses psyflow components
- [ ] README includes configuration summary and methods
- [ ] All necessary files and folders are included
- [ ] The task is runable and tested locally
```


#### 5. Wait for Admin Review

A TaskBeacon admin will:

- Review your task structure and documentation
- Leave comments or suggestions
- Approve and create a new official repository under the TaskBeacon organization
-**Add you (the original author) as a collaborator** to the new repository, so you can continue maintaining and improving it


Once live, your task becomes part of the open library. You can continue submitting:
- Bug fixes or updates via pull requests
- Variants as new branches (e.g., `variant/sst-audio`)