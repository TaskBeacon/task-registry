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
| **License**            | MIT                        |
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
