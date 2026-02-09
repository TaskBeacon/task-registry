# Flanker Task

| Field                | Value                                      |
|----------------------|--------------------------------------------|
| Name                 | Eriksen Flanker Task                       |
| Version              | main (1.0)                                 |
| URL / Repository     | https://github.com/TaskBeacon/T000004-flanker      |
| Short Description    | A task measuring response inhibition and selective attention. |
| Created By           | Zhipeng Cao (zhipeng30@foxmail.com)        |
| Date Updated         | 2025/07/24                                 |
| PsyFlow Version      | 0.1.0                                      |
| PsychoPy Version     | 2025.1.1                                   |
| Modality             | Behavior/EEG                               |
| Language | Chinese |
| Voice Name | zh-CN-YunyangNeural |


## 1. Task Overview

The Eriksen Flanker Task is a classic experimental paradigm used to assess selective attention and response inhibition. Participants are presented with a central target stimulus (an arrow) flanked by other stimuli (arrows). They are instructed to respond to the direction of the central target while ignoring the flanking stimuli. The task measures how efficiently a participant can focus on a target and filter out distracting information.

## 2. Task Flow

### Block-Level Flow

| Step                       | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| Load Config                | Load task configuration from `config.yaml`.                                 |
| Collect Subject Info       | Display a form to collect participant demographics.                         |
| Setup Triggers             | Initialize the trigger sender for EEG/fMRI synchronization.                 |
| Initialize Window/Input    | Create the PsychoPy window and keyboard handler.                            |
| Load Stimuli               | Load all visual stimuli defined in the config using `StimBank`.             |
| Show Instructions          | Present task instructions to the participant.                               |
| Loop Over Blocks           | For each block: run trials, then compute and show block-level feedback.     |
| Show Goodbye               | Display a final thank you message.                                          |
| Save Data                  | Save all recorded trial data to a CSV file.                                 |
| Close                      | Close the trigger port and quit PsychoPy.                                   |

### Trial-Level Flow

| Step                | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| Fixation            | Show a central fixation cross `(+)`.                                        |
| Stimulus            | Present the Flanker stimulus (e.g., `>>><>>`).                              |
| Response            | Record the participant's key press (`left` or `right`).                     |
| Feedback            | Display feedback (`Correct`, `Incorrect`, or `Too Slow`).                   |
| ITI                 | A blank screen shown for a random duration before the next trial.           |

## 3. Configuration Summary

### a. Subject Info

| Field       | Meaning                    |
|-------------|----------------------------|
| subject_id  | Unique participant ID (3 digits). |
| subname     | Participant's name (Pinyin). |
| age         | Participant's age.         |
| gender      | Participant's gender.      |

### b. Window Settings

Standard PsychoPy window settings for fullscreen display.

### c. Stimuli

| Name                     | Type      | Description                                           |
|--------------------------|-----------|-------------------------------------------------------|
| fixation                 | text      | Central cross `+`.                                    |
| congruent_left           | text      | `<<<<<`                                               |
| congruent_right          | text      | `>>>>>`                                               |
| incongruent_left         | text      | `>><>>`                                               |
| incongruent_right        | text      | `<<><<`                                               |
| correct_feedback         | textbox   | "正确" (Correct) in green.                            |
| incorrect_feedback       | textbox   | "错误" (Incorrect) in red.                            |
| no_response_feedback     | textbox   | "太慢" (Too Slow) in orange.                          |
| instruction_text         | textbox   | Instructions explaining the task.                     |
| block_break              | text      | Inter-block message showing accuracy and RT.          |
| good_bye                 | text      | Final thank you message.                              |

### d. Timing

| Phase                 | Duration (s)        | Config Variable      |
|------------------------|--------------------|--------------------|
| fixation              | 0.5                | fixation_duration  |
| stimulus              | 1.0 (max response time) | stim_duration      |
| feedback              | 0.5                | feedback_duration  |
| iti                   | random 0.8�?.2     | iti_duration |

### e. Triggers

| Event                    | Code  |
|--------------------------|-------|
| exp_onset                | 98    |
| exp_end                  | 99    |
| block_onset              | 100   |
| block_end                | 101   |
| fixation_onset           | 1     |
| congruent_stim_onset     | 10    |
| incongruent_stim_onset   | 20    |
| left_key_press           | 30    |
| right_key_press          | 31    |
| feedback_correct_response | 51    |
| feedback_incorrect_response | 52    |
| feedback_no_response     | 53    |
| feedback_onset           | 60    |

## 4. Methods (for academic publication)

In this experiment, participants performed an Eriksen Flanker task to assess selective attention and response inhibition. Each trial began with a central fixation cross, displayed for 500 ms. Subsequently, a row of five arrows was presented in the center of the screen for up to 1000 ms or until a response was made. Participants were instructed to respond to the direction of the central arrow while ignoring the flanking arrows by pressing the 'f' key for a left-pointing central arrow or the 'j' key for a right-pointing central arrow. Following their response, feedback was provided for 500 ms, indicating whether the response was correct, incorrect, or too slow.

The task included two types of stimuli: congruent trials, where all arrows pointed in the same direction (e.g., '>>>>>' or '<<<<<'), and incongruent trials, where the flanking arrows pointed in the opposite direction from the central target arrow (e.g., '>><>>' or '<<><<'). These conditions were presented in a randomized order within each block.

The task was structured into 3 blocks of 60 trials each (total 180 trials), with equal numbers of each condition (congruent-left, congruent-right, incongruent-left, incongruent-right) in each block. After each block, participants received feedback on their accuracy and were given the opportunity to rest before continuing to the next block. The inter-trial interval varied randomly between 800 and 1200 ms to prevent anticipatory responses.

This design allows for the examination of cognitive control processes, specifically the ability to selectively attend to relevant information while suppressing interference from irrelevant information. The difference in performance (reaction time and accuracy) between congruent and incongruent trials provides a measure of the "flanker effect," which reflects the cost of inhibiting conflicting information.

## 5. References

1. Eriksen, B. A., & Eriksen, C. W. (1974). Effects of noise letters upon the identification of a target letter in a nonsearch task. *Perception & Psychophysics*, 16(1), 143-149.

2. Ridderinkhof, K. R., van der Molen, M. W., Band, G. P., & Bashore, T. R. (1997). Sources of interference from irrelevant information: A developmental study. *Journal of Experimental Child Psychology*, 65(3), 315-341.

3. Fan, J., McCandliss, B. D., Sommer, T., Raz, A., & Posner, M. I. (2002). Testing the efficiency and independence of attentional networks. *Journal of Cognitive Neuroscience*, 14(3), 340-347.

