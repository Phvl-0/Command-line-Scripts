# scripts_projs

A collection of useful command-line scripts for everyday system tasks, automation, and log analysis. This repository is designed as a toolbox for quick solutions to common problems.

## Contents

- [log_analyzer.py](#log_analyzerpy) — Analyze log files for errors, warnings, and info.
- [cli_task_manager.py](#cli_task_managerpy) — Manage your tasks directly from the command line.
- [system_maintenance.sh](#system_maintenancesh) — Automate routine system maintenance operations.

---

## log_analyzer.py

A Python script to scan log files, count occurrences of important keywords (`ERROR`, `WARNING`, `INFO`), and generate a summary report.

**Usage:**
```sh
python3 log_analyzer.py <log_file_path> [output_file_path]
```
- `<log_file_path>`: Path to your log file (required).
- `[output_file_path]`: Optional path for the report (defaults to `analysis_report.txt`).

---

## cli_task_manager.py

A Python command-line tool to help you create, list, update, and remove personal tasks.

**Usage:**
```sh
python3 cli_task_manager.py [options]
```
Check the script’s help section or README for available commands.

---

## system_maintenance.sh

A shell script that automates common system cleanup and maintenance operations (e.g., updating packages, clearing caches, etc.).

**Usage:**
```sh
bash system_maintenance.sh
```
Run as root or with necessary permissions as required.

---

## Requirements

- Python 3.x (for Python scripts)
- Bash (for shell script)
- Appropriate permissions for system scripts

## Contribution

Feel free to fork, suggest improvements, or submit pull requests!

## License

This project is open source under the MIT License.

---

```
