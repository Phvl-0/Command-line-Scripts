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
