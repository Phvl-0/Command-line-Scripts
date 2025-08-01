Log Analysis & Reporting Tool
This repository contains a simple Python script that serves as a command-line tool for analyzing log files. The script demonstrates proficiency in Python scripting, file handling, and regular expressions—all essential skills for tasks involving data processing and system monitoring.

Features
Error & Warning Detection: Counts occurrences of "ERROR", "WARNING", and "INFO" in a given log file.

Report Generation: Generates a clean, human-readable report summarizing the analysis.

Command-Line Interface: Designed to be run directly from the terminal with easy-to-use arguments.

Usage
Clone the repository:

git clone https://github.com/Phvl-0/log-analysis-tool
cd log-analysis-tool

Run the script:

python3 log_analyzer.py <log_file_path> [output_file_path]

<log_file_path>: The path to the log file you want to analyze (required).

[output_file_path]: An optional path to save the generated report. If not provided, it defaults to analysis_report.txt.

Example
To analyze a log file named server.log and save the report as report.txt, you would run:

python3 log_analyzer.py server.log report.txt

This will create report.txt with a summary of the errors, warnings, and info messages found in server.log.
