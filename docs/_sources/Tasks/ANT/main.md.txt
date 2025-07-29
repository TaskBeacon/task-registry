# Attention Network Test (ANT)

| Field                | Value                                      |
| -------------------- | ------------------------------------------ |
| Name                 | Attention Network Test (ANT)               |
| Version              | main (1.0)                                 |
| URL / Repository     | https://github.com/TaskBeacon/ANT          |
| Short Description    | A task measuring alerting, orienting, and executive control networks. |
| Created By           | Zhipeng Cao (zhipeng30@foxmail.com)        |
| Date Updated         | 2025/07/29                                 |
| PsyFlow Version      | 0.1.0                                      |
| PsychoPy Version     | 2025.1.1                                   |
| Modality             | Behavior/EEG                               |
| Language             | Chinese                                    |
| Voice Name           | zh-CN-YunyangNeural                        |

## 1. Task Overview

The Attention Network Test (ANT) is a classic experimental paradigm used to assess the efficiency of three distinct attentional networks: alerting, orienting, and executive control. Participants are presented with a central target stimulus (an arrow) flanked by other stimuli (arrows). They are instructed to respond to the direction of the central target while ignoring the flanking stimuli. The task measures how efficiently a participant can focus on a target and filter out distracting information, and how warning and spatial cues affect their performance.

## 2. Task Flow

### Block-Level Flow

| Step                       | Description                                                                 |
| -------------------------- | --------------------------------------------------------------------------- |
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
| ------------------- | --------------------------------------------------------------------------- |
| Fixation            | Show a central fixation cross `(+)`.                                        |
| Cue (Optional)      | A cue may appear to alert the participant (center cue), direct their attention (spatial cue), or both (double cue). |
| Stimulus            | Present the Flanker stimulus (e.g., `>>><>>`) at either the top or bottom of the screen. |
| Response            | Record the participant's key press (`left` or `right`).                     |
| Feedback            | Display feedback (`Correct`, `Incorrect`, or `Too Slow`).                   |
| ITI                 | A blank screen shown for a random duration before the next trial.           |

## 3. Configuration Summary

### a. Subject Info

| Field      | Meaning                    |
| ---------- | -------------------------- |
| subject_id | Unique participant ID (3 digits). |
| subname    | Participant's name (Pinyin). |
| age        | Participant's age.         |
| gender     | Participant's gender.      |

### b. Window Settings

Standard PsychoPy window settings for fullscreen display.

### c. Stimuli

| Name                     | Type    | Description                                   |
| ------------------------ | ------- | --------------------------------------------- |
| fixation                 | text    | Central cross `+`.                            |
| cue_up                   | text    | Cue `*` at the top of the screen.             |
| cue_down                 | text    | Cue `*` at the bottom of the screen.          |
| cue_center               | text    | Cue `*` at the center of the screen.          |
| congruent_up_left        | text    | `<<<<<` at the top of the screen.             |
| congruent_up_right       | text    | `>>>>>` at the top of the screen.             |
| incongruent_up_left      | text    | `>><>>` at the top of the screen.             |
| incongruent_up_right     | text    | `<<><<` at the top of the screen.             |
| congruent_down_left      | text    | `<<<<<` at the bottom of the screen.          |
| congruent_down_right     | text    | `>>>>>` at the bottom of the screen.          |
| incongruent_down_left    | text    | `>><>>` at the bottom of the screen.          |
| incongruent_down_right   | text    | `<<><<` at the bottom of the screen.          |
| correct_feedback         | textbox | "正确" (Correct) in green.                    |
| incorrect_feedback       | textbox | "错误" (Incorrect) in red.                    |
| no_response_feedback     | textbox | "太慢" (Too Slow) in orange.                  |
| instruction_text         | textbox | Instructions explaining the task.             |
| block_break              | text    | Inter-block message showing accuracy and RT.  |
| good_bye                 | text    | Final thank you message.                      |

### d. Timing

| Phase                  | Duration (s)      | Config Variable   |
| ---------------------- | ----------------- | ----------------- |
| cue                    | 0.1               | cue_duration      |
| fixation               | 0.5               | fixation_duration |
| stimulus               | 1.0 (max response time) | stim_duration     |
| feedback               | 0.5               | feedback_duration |
| iti                    | random 0.8–1.2    | iti_duration      |

### e. Triggers

| Event                           | Code  |
| ------------------------------- | ----- |
| exp_onset                       | 254   |
| exp_end                         | 255   |
| block_onset                     | 252   |
| block_end                       | 253   |
| fixation_onset                  | 1     |
| center_cue_onset                | 11    |
| double_cue_onset                | 12    |
| spatial_cue_up_onset            | 13    |
| spatial_cue_down_onset          | 14    |
| stim_1111                       | 21    |
| stim_1112                       | 22    |
| stim_1121                       | 23    |
| stim_1122                       | 24    |
| stim_1211                       | 25    |
| stim_1212                       | 26    |
| stim_1221                       | 27    |
| stim_1222                       | 28    |
| stim_2111                       | 31    |
| stim_2112                       | 32    |
| stim_2121                       | 33    |
| stim_2122                       | 34    |
| stim_2211                       | 35    |
| stim_2212                       | 36    |
| stim_2221                       | 37    |
| stim_2222                       | 38    |
| stim_3111                       | 41    |
| stim_3112                       | 42    |
| stim_3121                       | 43    |
| stim_3122                       | 44    |
| stim_3211                       | 45    |
| stim_3212                       | 46    |
| stim_3221                       | 47    |
| stim_3222                       | 48    |
| stim_4111                       | 51    |
| stim_4112                       | 52    |
| stim_4121                       | 53    |
| stim_4122                       | 54    |
| stim_4211                       | 55    |
| stim_4212                       | 56    |
| stim_4221                       | 57    |
| stim_4222                       | 58    |
| left_key_press                  | 201   |
| right_key_press                 | 202   |
| feedback_correct_response       | 221   |
| feedback_incorrect_response     | 222   |
| feedback_no_response            | 223   |
| feedback_onset                  | 230   |

## 4. Methods (for academic publication)

In this experiment, participants performed an Attention Network Test (ANT) to assess the efficiency of three attentional networks: alerting, orienting, and executive control. Each trial began with a central fixation cross, displayed for 500 ms. On some trials, a cue was presented for 100ms prior to the target. This cue could be a central cue (an asterisk at fixation), a double cue (asterisks at both possible target locations), a spatial cue (an asterisk at the location of the upcoming target), or no cue. Subsequently, a row of five arrows was presented at either the top or bottom of the screen for up to 1000 ms or until a response was made. Participants were instructed to respond to the direction of the central arrow while ignoring the flanking arrows by pressing the 'f' key for a left-pointing central arrow or the 'j' key for a right-pointing central arrow. Following their response, feedback was provided for 500 ms, indicating whether the response was correct, incorrect, or too slow.

The task included two types of stimuli: congruent trials, where all arrows pointed in the same direction (e.g., '>>>>>' or '<<<<<'), and incongruent trials, where the flanking arrows pointed in the opposite direction from the central target arrow (e.g., '>><>>' or '<<><<'). These conditions were presented in a randomized order within each block. The task was structured into 4 blocks of 96 trials each (total 384 trials), with equal numbers of each condition. After each block, participants received feedback on their accuracy and were given the opportunity to rest before continuing to the next block. The inter-trial interval varied randomly between 800 and 1200 ms to prevent anticipatory responses.

This design allows for the examination of the three attentional networks by calculating the following subtractions in reaction time: 

*   **Alerting Effect:** No Cue RT - Double Cue RT
*   **Orienting Effect:** Center Cue RT - Spatial Cue RT
*   **Executive Control Effect (Flanker Effect):** Incongruent RT - Congruent RT

## 5. References

1.  Fan, J., McCandliss, B. D., Sommer, T., Raz, a., & Posner, M. I. (2002). Testing the efficiency and independence of attentional networks. *Journal of Cognitive Neuroscience*, 14(3), 340-347.
2.  Eriksen, B. A., & Eriksen, C. W. (1974). Effects of noise letters upon the identification of a target letter in a nonsearch task. *Perception & Psychophysics*, 16(1), 143-149.
