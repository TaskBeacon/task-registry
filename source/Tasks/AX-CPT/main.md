# AX-CPT Task

| Field | Value |
|---|---|
| Name | AX-CPT Task |
| Version | main (1.0) |
| URL / Repository | https://github.com/TaskBeacon/T000001-ax-cpt |
| Short Description | A task measuring cognitive control, context processing, and goal maintenance. |
| Created By | Zhipeng Cao (zhipeng30@foxmail.com) |
| Date Updated | 2025/07/25 |
| PsyFlow Version |0.1.0|
| PsychoPy Version |2025.1.1              |
| Modality     |Behavior/EEG                  |
| Language | Chinese |
| Voice Name | zh-CN-YunyangNeural |

## 1. Task Overview
This task is an AX-Continuous Performance Test (AX-CPT) designed to assess cognitive control and context processing. Participants are presented with a series of letter pairs (cue followed by probe). They must make a specific target response only when the cue is an 'A' and the probe is an 'X' (AX trials). For all other combinations (AY, BX, BY), a different response (or no response) is required.

## 2. Task Flow
### Block-Level Flow
| Step | Description |
|---|---|
| 1. Instruction | Instructions are displayed at the beginning of the experiment. |
| 2. Trial Execution | Each block runs for a set number of trials, as defined in `config.yaml`. |
| 3. Block Break | After each block, a break screen is shown with the accuracy for the current block. |
| 4. Goodbye | After all blocks are complete, a "goodbye" message is displayed. |

### Trial-Level Flow
| Step | Description |
|---|---|
| 1. Fixation | A central fixation cross `(+)` is displayed. |
| 2. Cue Presentation | The cue letter (A or B) is presented. |
| 3. Inter-Stimulus Interval (ISI) Fixation | A central fixation cross `(+)` is displayed for a short duration. |
| 4. Probe Presentation & Response | The probe letter (X or Y) is presented, and the participant responds. |
| 4. Feedback | Feedback (`Correct`, `Incorrect`, or `Too Slow`) is displayed. |
| 5. Inter-Trial Interval (ITI) | A blank screen is shown before the next trial. |

## 3. Configuration Summary
### a. Subject Info
| Field | Meaning |
|---|---|
| subject_id | Subject Identifier |
| subname | Subject Name |
| age | Age |
| gender | Gender |

### b. Window Settings
| Parameter | Value |
|---|---|
| size | [1920, 1080] |
| units | deg |
| screen | 1 |
| bg_color | gray |
| fullscreen | True |
| monitor_width_cm | 60 |
| monitor_distance_cm | 72 |

### c. Stimuli
| Name | Type | Description |
|---|---|---|
| fixation | text | Central cross `+`. |
| cue_A | text | The cue letter 'A'. |
| cue_B | text | The cue letter 'B'. |
| probe_X | text | The probe letter 'X'. |
| probe_Y | text | The probe letter 'Y'. |
| correct_feedback | text | "正确" (Correct) in white. |
| incorrect_feedback | text | "错误" (Incorrect) in white. |
| no_response_feedback | text | "未反�? (No response) in white. |
| instruction_text | textbox | Instructions explaining the task. |
| instruction_text_voice | voice | Voice instructions for the task. |
| block_break | text | Feedback shown between blocks. |
| good_bye | text | Final message at the end of the task. |

### d. Timing
| Phase | Duration (s) | Config Variable |
|---|---|---|
| fixation | 0.5 | fixation_duration |
| cue | 0.5 | cue_duration |
| isi | 0.5 | isi_duration |
| probe | 1.0 (max response time) | probe_duration |
| feedback | 0.5 | feedback_duration |
| iti | random 0.8�?.2 | iti_duration |

### e. Triggers
| Event | Code |
|---|---|
| exp_onset | 98 |
| exp_end | 99 |
| block_onset | 100 |
| block_end | 101 |
| cue_onset | 10 |
| probe_onset | 20 |
| AX_trial_onset | 30 |
| AY_trial_onset | 31 |
| BX_trial_onset | 32 |
| BY_trial_onset | 33 |
| key_press | 40 |
| no_response | 41 |
| feedback_correct_response | 51 |
| feedback_incorrect_response | 52 |
| feedback_no_response | 53 |
| feedback_onset | 60 |

## 4. Methods
Participants perform an AX-CPT task, a continuous performance paradigm used to measure cognitive control and context processing. Each trial consists of a cue letter (A or B) followed by a probe letter (X or Y). Participants are instructed to press the 'f' key if the cue is 'A' and the probe is 'X' (AX trials). For all other cue-probe combinations (AY, BX, BY), they are instructed to press the 'j' key.

The task begins with a fixation cross, displayed for 500ms. The cue letter is then presented for 500ms, followed by a brief inter-stimulus interval (ISI) fixation of 500ms, and then the probe letter for up to 1000ms or until a response is made. Feedback (correct, incorrect, or no response) is provided for 500ms, followed by a randomized inter-trial interval between 800ms and 1200ms.

The task is structured into 4 blocks of 40 trials each (total 160 trials). Trial types (AX, AY, BX, BY) are presented in a randomized order within each block, with a higher proportion of AX trials to establish a strong context. This design allows for the examination of proactive and reactive cognitive control strategies.