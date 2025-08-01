#!/bin/bash

# ==============================================================================
# System Automation & Maintenance Script
# ------------------------------------------------------------------------------
# This script automates common system maintenance tasks, including:
# 1. Updating package lists and installing available updates.
# 2. Cleaning up temporary files and cache.
# 3. Performing a simple backup of a specified directory.
# This script is intended to be run with sudo for full permissions.
# ==============================================================================

# --- Variables ---
# The directory you want to back up. Change this to a directory you'd like to back up.
BACKUP_DIR="/var/log"
# The destination for the backup. A folder will be created here with a timestamp.
BACKUP_DEST="/tmp"
# The name for the backup file.
BACKUP_FILE_NAME="system_backup_$(date +%Y-%m-%d_%H-%M-%S).tar.gz"

# --- Functions ---

# Function to check for root privileges
check_root() {
    if [ "$(id -u)" -ne 0 ]; then
        echo "This script requires root privileges. Please run with 'sudo'."
        exit 1
    fi
}

# Function to handle updates
run_updates() {
    echo "===================================="
    echo "Starting system updates..."
    echo "===================================="
    # Update package list
    sudo apt-get update -y
    # Upgrade all installed packages
    sudo apt-get upgrade -y
    echo "System updates finished."
    echo ""
}

# Function to clean up temporary files
clean_system() {
    echo "===================================="
    echo "Starting system cleanup..."
    echo "===================================="
    # Clean up old packages
    sudo apt-get autoremove -y
    sudo apt-get autoclean -y
    # Remove old log files
    sudo rm -rf /var/log/*.gz
    echo "System cleanup finished."
    echo ""
}

# Function to perform a backup
run_backup() {
    echo "===================================="
    echo "Starting backup of ${BACKUP_DIR}..."
    echo "===================================="
    # Check if the directory to back up exists.
    if [ ! -d "${BACKUP_DIR}" ]; then
        echo "Error: Backup directory ${BACKUP_DIR} not found. Skipping backup."
        echo ""
        return
    fi
    # Create the backup file
    sudo tar -czf "${BACKUP_DEST}/${BACKUP_FILE_NAME}" "${BACKUP_DIR}"
    echo "Backup created at: ${BACKUP_DEST}/${BACKUP_FILE_NAME}"
    echo "Backup finished."
    echo ""
}

# --- Main Script Execution ---

check_root
run_updates
clean_system
run_backup

echo "Script finished. All tasks completed!"

