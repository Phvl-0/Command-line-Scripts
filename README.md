# scripts_projs

A collection of useful command-line scripts for everyday system tasks, automation, and log analysis. This repository is designed as a toolbox for quick solutions to common problems.

## Contents

- [log_analyzer.py](#log_analyzerpy) — Analyze log files for errors, warnings, and info.
- [cli_task_manager.py](#cli_task_managerpy) — Manage your tasks directly from the command line.
- [system_maintenance.sh](#system_maintenancesh) — Automate routine system maintenance operations.

---

# Log Analysis & Reporting Tool

This repository contains a simple Python script for analyzing log files via the command line. It’s useful for quickly finding and summarizing occurrences of key log messages (like `ERROR`, `WARNING`, `INFO`)—making it a practical tool for system monitoring, debugging, and more.

## Features

- **Keyword Detection:** Counts how many times `ERROR`, `WARNING`, and `INFO` (or your chosen keywords) appear in the log file.
- **Report Generation:** Creates a clean, human-readable summary of the analysis.
- **Command-Line Interface:** Run directly from the terminal with easy-to-use arguments.
- **Custom Keywords:** Optionally specify your own keywords to search for.

## Usage

**1. Clone the repository:**
```sh
git clone https://github.com/Phvl-0/scripts_projs
cd scripts_projs
```

**2. Run the script:**
```sh
python3 log_analyzer.py <log_file_path> [output_file_path] [KEYWORD1 KEYWORD2 ...]
```
- `<log_file_path>`: Path to the log file you want to analyze (**required**)
- `[output_file_path]`: Optional path to save the generated report (defaults to `analysis_report.txt`)
- `[KEYWORD1 KEYWORD2 ...]`: Optional list of keywords to search for (defaults to `ERROR`, `WARNING`, `INFO`)

**Example:**
```sh
python3 log_analyzer.py server.log report.txt ERROR WARNING
```
This will analyze `server.log` for `ERROR` and `WARNING` messages and save the summary to `report.txt`.

## Sample Output

```
Log Analysis Report
Total lines: 100
Lines with keyword(s): 40 (40.00%)
ERROR: 15 (15.00% of all lines)
WARNING: 25 (25.00% of all lines)
INFO: 10 (10.00% of all lines)
```

## Requirements

- Python 3.x

## Why Use This Tool?

- Quickly summarize large log files.
- Instantly spot errors and warnings.
- Useful for system admins, developers, security teams, and support.

---

*Feel free to fork or contribute! If you find it useful, star the repo or share feedback.*



---

# CLI Task Manager

A simple and interactive command-line application for managing your tasks easily and efficiently. With this tool, you can add, view, edit, delete, and mark tasks as complete—all from your terminal. All tasks are saved to a file for persistence across sessions.

## Features

- **Add Tasks**: Quickly create new tasks with a description.
- **View Tasks**: List all tasks, showing their completion status and unique IDs.
- **Edit Tasks**: Update a task’s description using its ID.
- **Delete Tasks**: Remove tasks by ID.
- **Mark Complete**: Mark any task as completed by its ID.
- **Persistent Storage**: Tasks are saved in a local JSON file (`tasks.json` by default).
- **Clear Screen**: Keeps the interface clean after each action.

## Requirements

- Python 3.x

No external packages are required; only the Python standard library is used.

## Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Phvl-0/scripts_projs.git
   cd scripts_projs
   ```

2. **Run the script:**
   ```bash
   python3 cli_task_manager.py
   ```
   Or make it executable:
   ```bash
   chmod +x cli_task_manager.py
   ./cli_task_manager.py
   ```

3. **Interact with the menu:**
   - When launched, you’ll see a menu with numbered options:
     ```
     --- CLI Task Manager ---
     1. Add a new task
     2. View all tasks
     3. Mark a task as complete
     4. Edit a task
     5. Delete a task
     6. Exit
     ```
   - Enter the number for your desired action and follow the prompts.

## Configuration

By default, tasks are stored in `tasks.json` in the current directory. You can override this by setting the `TASKS_FILE` environment variable:

```bash
export TASKS_FILE="/path/to/your_tasks.json"
python3 cli_task_manager.py
```

## File Format

Tasks are stored as a list of JSON objects, each with:
- `id`: Unique task identifier
- `description`: The task text
- `completed`: Boolean (true if the task is done)

## Example

```
$ python3 cli_task_manager.py

--- CLI Task Manager ---
1. Add a new task
2. View all tasks
...
Enter your choice (1-6): 1
Enter a new task: Finish writing the report
Task 'Finish writing the report' added.
```

## License

This script is provided as-is for personal use and learning. Check the repository for any specific licensing.

## Author

- GitHub: [Phvl-0](https://github.com/Phvl-0)

---

Let me know if you want further customization, screenshots, or details!

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
