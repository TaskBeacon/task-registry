# Stroop Task

| Field                | Value                                      |
|----------------------|--------------------------------------------|
| Name                 | Stroop Task                                |
| Version              | main (1.0)                                 |
| URL / Repository     | https://github.com/TaskBeacon/T000014-stroop       |
| Short Description    | A task measuring response inhibition and selective attention. |
| Created By           | Zhipeng Cao (zhipeng30@foxmail.com)        |
| Date Updated         | 2025/07/24                                 |
| PsyFlow Version      | 0.1.0                                      |
| PsychoPy Version     | 2025.1.1                                   |
| Modality             | Behavior/EEG                               |
| Language | Chinese |
| Voice Name | zh-CN-YunyangNeural |


## 1. Task Overview

The Stroop Task is a classic experimental paradigm used to assess selective attention and response inhibition. Participants are presented with a word (a color name) printed in a specific ink color. They are instructed to name the ink color of the word, ignoring the word itself. The task measures how efficiently a participant can focus on a target attribute (the ink color) and filter out distracting information (the word's meaning).

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
| Stimulus            | Present the Stroop stimulus (e.g., the word "Red" in green ink).            |
| Response            | Record the participant's key press (`f` for red, `j` for green).            |
| Feedback            | Display feedback (`Correct`, `Incorrect`, or `No Response`).                |
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
| congruent_red            | text      | The word "Á∫? (Red) in red ink.                       |
| congruent_green          | text      | The word "Áª? (Green) in green ink.                   |
| incongruent_red          | text      | The word "Áª? (Green) in red ink.                     |
| incongruent_green        | text      | The word "Á∫? (Red) in green ink.                     |
| correct_feedback         | textbox   | "Ê≠£Á°Æ" (Correct) in white.                            |
| incorrect_feedback       | textbox   | "ÈîôËØØ" (Incorrect) in white.                          |
| no_response_feedback     | textbox   | "Êú™ÂèçÂ∫? (No Response) in white.                      |
| instruction_text         | textbox   | Instructions explaining the task.                     |
| block_break              | text      | Inter-block message showing accuracy.                 |
| good_bye                 | text      | Final thank you message.                              |

### d. Timing

| Phase                 | Duration (s)        | Config Variable      |
|------------------------|--------------------|--------------------|
| fixation              | 0.5                | fixation_duration  |
| stimulus              | 2.0 (max response time) | stim_duration      |
| feedback              | 0.5                | feedback_duration  |
| iti                   | random 0.8‚Ä?.2     | iti_duration       |

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
| red_key_press            | 30    |
| green_key_press          | 31    |
| feedback_correct_response | 51    |
| feedback_incorrect_response | 52    |
| feedback_no_response     | 53    |
| feedback_onset           | 60    |

## 4. Methods (for academic publication)

In this experiment, participants performed a Stroop task to assess selective attention and response inhibition. Each trial began with a central fixation cross, displayed for 500 ms. Subsequently, a word was presented in the center of the screen for up to 2000 ms or until a response was made. Participants were instructed to respond to the ink color of the word while ignoring the word's meaning by pressing the 'f' key for red ink or the 'j' key for green ink. Following their response, feedback was provided for 500 ms, indicating whether the response was correct, incorrect, or if no response was made.

The task included two types of stimuli: congruent trials, where the word and ink color matched (e.g., the word "Red" in red ink), and incongruent trials, where the word and ink color were mismatched (e.g., the word "Red" in green ink). These conditions were presented in a randomized order within each block.

The task was structured into 3 blocks of 60 trials each (total 180 trials), with equal numbers of each condition (congruent-red, congruent-green, incongruent-red, incongruent-green) in each block. After each block, participants received feedback on their accuracy and were given the opportunity to rest before continuing to the next block. The inter-trial interval varied randomly between 800 and 1200 ms to prevent anticipatory responses.

This design allows for the examination of cognitive control processes, specifically the ability to selectively attend to relevant information while suppressing interference from irrelevant information. The difference in performance (reaction time and accuracy) between congruent and incongruent trials provides a measure of the "Stroop effect," which reflects the cost of inhibiting conflicting information.

## 5. References

1. Stroop, J. R. (1935). Studies of interference in serial verbal reactions. *Journal of Experimental Psychology*, 18(6), 643-662.

2. MacLeod, C. M. (1991). Half a century of research on the Stroop effect: An integrative review. *Psychological Bulletin*, 109(2), 163-203.

