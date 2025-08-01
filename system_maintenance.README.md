System Automation & Maintenance Script
This repository contains a simple yet effective Bash script designed to automate routine system maintenance tasks on a GNU/Linux system. This project showcases proficiency in Bash scripting for system administration, a key skill for DevOps and system-oriented roles.

Features
System Updates: Automatically updates the package list and installs new software versions.

System Cleanup: Removes outdated packages and clears the system cache to free up disk space.

Automated Backup: Creates a compressed .tar.gz backup of a specified directory, which can be configured by the user.

Usage
Clone the repository:

git clone https://github.com/Phvl-0/system-maintenance-script
cd system-maintenance-script

Make the script executable:

chmod +x system_maintenance.sh

Run the script with sudo:

sudo ./system_maintenance.sh

Note: The script requires sudo privileges to perform updates and cleanup tasks. You can edit the BACKUP_DIR and BACKUP_DEST variables within the script to customize the backup process.
