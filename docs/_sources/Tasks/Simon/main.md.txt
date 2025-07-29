# Simon Task

| Field                | Value                                      |
|----------------------|--------------------------------------------|
| Name                 | Simon Task                                 |
| Version              | main (1.0)                                 |
| URL / Repository     | https://github.com/TaskBeacon/SimonTask    |
| Short Description    | A task measuring response conflict and cognitive control. |
| Created By           | Zhipeng Cao (zhipeng30@foxmail.com)        |
| Date Updated         | 2025/07/25                                 |
| PsyFlow Version      | 0.1.0                                      |
| PsychoPy Version     | 2025.1.1                                   |
| Modality             | Behavior/EEG                               |
| Language | Chinese |
| Voice Name | zh-CN-YunyangNeural |


## 1. Task Overview

The Simon Task is a classic experimental paradigm used to assess response conflict and cognitive control. Participants are presented with a stimulus (e.g., a colored circle) that appears on either the left or right side of the screen. They are instructed to respond based on a non-spatial attribute of the stimulus (e.g., its color), while ignoring its spatial location. The task measures the interference that occurs when the irrelevant spatial location of the stimulus conflicts with the required response location.

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
| Stimulus            | Present a colored circle on the left or right side of the screen.           |
| Response            | Record the participant's key press (`f` for red, `j` for blue).             |
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
| red_left                 | circle    | A red circle presented on the left.                   |
| red_right                | circle    | A red circle presented on the right.                  |
| blue_left                | circle    | A blue circle presented on the left.                  |
| blue_right               | circle    | A blue circle presented on the right.                 |
| correct_feedback         | textbox   | "正确" (Correct) in white.                            |
| incorrect_feedback       | textbox   | "错误" (Incorrect) in white.                            |
| no_response_feedback     | textbox   | "未反应" (No response) in white.                          |
| instruction_text         | textbox   | Instructions explaining the task.                     |
| block_break              | text      | Inter-block message showing accuracy and RT.          |
| good_bye                 | text      | Final thank you message.                              |

### d. Timing

| Phase                 | Duration (s)        | Config Variable      |
|------------------------|--------------------|--------------------|
| fixation              | 0.5                | fixation_duration  |
| stimulus              | 1.0 (max response time) | stim_duration      |
| feedback              | 0.5                | feedback_duration  |
| iti                   | random 0.8–1.2     | iti_duration |

### e. Triggers

| Event                    | Code  |
|--------------------------|-------|
| exp_onset                | 98    |
| exp_end                  | 99    |
| block_onset              | 100   |
| block_end                | 101   |
| fixation_onset           | 1     |
| stim_onset               | 10    |
| left_key_press           | 30    |
| right_key_press          | 31    |
| feedback_correct_response | 51    |
| feedback_incorrect_response | 52    |
| feedback_no_response     | 53    |
| feedback_onset           | 60    |

## 4. Methods (for academic publication)

In this experiment, participants performed a Simon task to assess response conflict and cognitive control. Each trial began with a central fixation cross, displayed for 500 ms. Subsequently, a colored circle (red or blue) was presented on either the left or right side of the screen for up to 1000 ms or until a response was made. Participants were instructed to respond based on the color of the circle, ignoring its spatial location. Specifically, they pressed the 'f' key for a red circle and the 'j' key for a blue circle. Following their response, feedback was provided for 500 ms, indicating whether the response was correct, incorrect, or too slow.

The task included two types of trials: congruent trials, where the stimulus color and its spatial location mapped to the same response side (e.g., a red circle on the left, requiring a left-hand response), and incongruent trials, where the stimulus color and its spatial location mapped to different response sides (e.g., a red circle on the right, requiring a left-hand response). These conditions were presented in a randomized order within each block.

The task was structured into 3 blocks of 60 trials each (total 180 trials), with equal numbers of each condition (red-left, red-right, blue-left, blue-right) in each block. After each block, participants received feedback on their accuracy and were given the opportunity to rest before continuing to the next block. The inter-trial interval varied randomly between 800 and 1200 ms to prevent anticipatory responses.

This design allows for the examination of cognitive control processes, specifically the ability to resolve conflict between relevant (color) and irrelevant (location) stimulus features. The difference in performance (reaction time and accuracy) between congruent and incongruent trials provides a measure of the "Simon effect," which reflects the cost of inhibiting conflicting spatial information.

## 5. References

1. Simon, J. R., & Rudell, A. P. (1967). Auditory S-R compatibility: The effect of an irrelevant spatial dimension on reaction time. *Journal of Applied Psychology*, 51(3), 300-304.

2. Lu, C. H., & Proctor, R. W. (1995). The Simon effect and the processing of stimulus and response features. *Journal of Experimental Psychology: Human Perception and Performance*, 21(2), 457-470.

3. Hommel, B. (1993). The relationship between stimulus-response compatibility and the Simon effect. *Psychological Research*, 55(2), 158-162.

