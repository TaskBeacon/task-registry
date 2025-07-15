# TAPS

The Task and Paradigm Structure (TAPS) provides a standardized folder layout for organizing cognitive tasks in a modular and reproducible way. This structure promotes clarity, cross-task consistency, and ease of reuse—whether in individual research projects or shared task libraries.

A sample directory tree might look like this:
```
Task/
├── assets/             # Multimedia stimuli (images, sounds, videos, etc.)
│ ├── instruction.mp3
│ ├── stim1.bmp
│ ├── stim2.bmp
│ └── stim3.bmp
├── config/
│ └── config.yaml       # YAML-based configuration files for task logic and settings
├── data/               # Collected participant data and logs
│ ├── sub-001_task_sst_20250603_143742.json
│ ├── sub-001_task_sst_20250603_143742.log
│ └── sub-001_task_sst_20250603_143742.csv
├── src/                # Source code implementing task flow and logic
│ ├── __init__.py
│ ├── run_trial.py
│ └── controller.py
├── analysis/            # Optional scripts for analyzing collected data
│ └── analysis.py
├── main.py              # Entry point for running the task   
└── README.md            # Documentation
```

Each task organized under TAPS typically contains the following components:

`assets/`
Contains all multimedia stimuli used in the task, such as images (.bmp), audio files (.mp3), or videos (.mp4). These files are referenced by the configuration and code but stored independently for clarity.

`config/`
Includes YAML configuration files (e.g., config.yaml) that define task parameters, stimuli mappings, timing settings, and localization content. This enables flexible task customization without modifying the source code.

`data/`
Stores participant outputs including raw logs, structured .csv data, and optionally serialized formats like .json. Each session is typically timestamped for easy tracking and reproducibility.

`src/`
Contains the core Python scripts implementing the task logic and runtime flow (e.g., run_trial.py, controller.py). This code defines how trials are executed, how input is handled, and how responses are recorded.

`analysis/`
(Optional) Includes scripts to analyze the collected data. Useful for quick validation, pilot analysis, or standardized data summaries.

`main.py`
A runnable Python entry point that initializes the task using the configuration and source logic. This is typically the file users execute to start the experiment.

`README.md`
Provides human-readable documentation describing the task’s purpose, structure, configuration, and usage.



This structure cleanly separates task components—stimuli, configuration, logic, data, and metadata—enabling better task reuse, localization, and version control. 