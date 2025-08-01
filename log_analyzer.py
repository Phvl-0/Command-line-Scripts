#!/usr/bin/env python3

# ==============================================================================
# Log Analysis & Reporting Tool
# ------------------------------------------------------------------------------
# This Python script analyzes a specified log file to count and report on
# occurrences of specific keywords, such as "ERROR", "WARNING", and "INFO".
# It generates a summary report to a separate output file.
# ==============================================================================

import sys
import re

def analyze_log_file(log_file_path):
    """
    Analyzes a log file for specific keywords and returns a summary report.

    Args:
        log_file_path (str): The path to the log file to be analyzed.

    Returns:
        dict: A dictionary containing the counts of each keyword.
              Returns None if the file is not found.
    """
    try:
        # Initialize counts for different log levels
        error_count = 0
        warning_count = 0
        info_count = 0
        
        # Read the log file line by line
        with open(log_file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                
                # Check for keywords (case-insensitive)
                if re.search(r'\bERROR\b', line, re.IGNORECASE):
                    error_count += 1
                elif re.search(r'\bWARNING\b', line, re.IGNORECASE):
                    warning_count += 1
                elif re.search(r'\bINFO\b', line, re.IGNORECASE):
                    info_count += 1

        # Return the summary as a dictionary
        return {
            'ERROR': error_count,
            'WARNING': warning_count,
            'INFO': info_count,
            'total_lines': error_count + warning_count + info_count
        }

    except FileNotFoundError:
        print(f"Error: The file at path '{log_file_path}' was not found.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def generate_report(summary, output_file_path):
    """
    Generates a text report from the analysis summary.

    Args:
        summary (dict): The summary dictionary from the log analysis.
        output_file_path (str): The path to save the generated report.
    """
    with open(output_file_path, 'w') as file:
        file.write("=========================================\n")
        file.write("        Log Analysis Report\n")
        file.write("=========================================\n\n")
        
        if summary:
            for key, value in summary.items():
                file.write(f"{key}: {value}\n")
        else:
            file.write("No data to report.\n")
    
    print(f"Report generated successfully at: {output_file_path}")

def main():
    """
    Main function to run the script.
    Checks for command-line arguments and orchestrates the analysis and report generation.
    """
    if len(sys.argv) < 2:
        print("Usage: python3 log_analyzer.py <log_file_path> [output_file_path]")
        sys.exit(1)

    log_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "analysis_report.txt"

    print(f"Analyzing log file: {log_file}...")
    summary = analyze_log_file(log_file)
    
    if summary:
        print("Analysis complete. Generating report...")
        generate_report(summary, output_file)

if __name__ == "__main__":
    main()

