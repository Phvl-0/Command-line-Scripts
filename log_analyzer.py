#!/usr/bin/env python3

# ==============================================================================
# Log Analysis & Reporting Tool (Enhanced)
# ------------------------------------------------------------------------------
# This Python script analyzes a specified log file to count and report on 
# occurrences of user-defined keywords (default: "ERROR", "WARNING", "INFO").
# It generates a summary report including total lines, keyword counts, and 
# percentage breakdowns. Keywords are configurable via command-line.
# ==============================================================================
# Example usage:
#   python3 log_analyzer.py <log_file_path> [output_file_path] [KEYWORD1 KEYWORD2 ...]
#   python3 log_analyzer.py mylog.txt report.txt ERROR WARNING DEBUG

import sys
import re
import time
from collections import Counter

def analyze_log_file(log_file_path, keywords):
    """
    Analyzes a log file for specified keywords and returns a summary report.

    Args:
        log_file_path (str): Path to the log file.
        keywords (list of str): List of keywords to count.

    Returns:
        dict: Counts of each keyword, total lines, and lines with at least one keyword.
    """
    keyword_counts = Counter()
    total_lines = 0
    lines_with_keyword = 0

    # Compile regex patterns for efficiency
    patterns = {kw: re.compile(rf"\b{re.escape(kw)}\b", re.IGNORECASE) for kw in keywords}

    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                total_lines += 1
                found_any = False
                for kw, pat in patterns.items():
                    matches = len(pat.findall(line))
                    if matches:
                        keyword_counts[kw] += matches
                        found_any = True
                if found_any:
                    lines_with_keyword += 1

        summary = {
            'total_lines': total_lines,
            'lines_with_keyword': lines_with_keyword,
        }
        summary.update(keyword_counts)
        return summary

    except FileNotFoundError:
        print(f"Error: File '{log_file_path}' not found.")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def generate_report(summary, keywords, output_file_path):
    """
    Generates a text report from the analysis summary.

    Args:
        summary (dict): The summary dictionary from log analysis.
        keywords (list of str): List of analyzed keywords.
        output_file_path (str): Path to save the generated report.
    """
    with open(output_file_path, 'w') as file:
        file.write("=========================================\n")
        file.write("        Log Analysis Report \n")
        file.write("=========================================\n\n")
        if summary:
            file.write(f"Total lines: {summary['total_lines']}\n")
            file.write(f"Lines with keyword(s): {summary['lines_with_keyword']} ({summary['lines_with_keyword'] / summary['total_lines']:.2%})\n\n")
            for kw in keywords:
                count = summary.get(kw, 0)
                percent = (count / summary['total_lines']) if summary['total_lines'] else 0
                file.write(f"{kw}: {count} ({percent:.2%} of all lines)\n")
        else:
            file.write("No data to report.\n")
    print(f"Report generated successfully at: {output_file_path}")

def main():
    """
    Main function to run the script.

    Usage:
        python3 log_analyzer.py <log_file_path> [output_file_path] [KEYWORD1 KEYWORD2 ...]
    """
    if len(sys.argv) < 2:
        print("Usage: python3 log_analyzer.py <log_file_path> [output_file_path] [KEYWORD1 KEYWORD2 ...]")
        sys.exit(1)

    log_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 and not sys.argv[2].upper().isalpha() else "analysis_report.txt"
    # Determine if keywords are specified (after output file)
    keyword_args = sys.argv[3:] if len(sys.argv) > 3 else []
    # Default keywords
    keywords = keyword_args if keyword_args else ["ERROR", "WARNING", "INFO"]

    print(f"Analyzing log file: {log_file} for keywords: {', '.join(keywords)}")
    time.sleep(1) 

    print("Counting keywords...")
    time.sleep(2) 

    summary = analyze_log_file(log_file, keywords)

    if summary:
        print("Analysis complete! Generating report...")
        time.sleep(3) 
        generate_report(summary, keywords, output_file)

if __name__ == "__main__":
    main()
