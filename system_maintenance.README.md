
## README for `system_maintenance.sh`

# System Automation & Maintenance Script

Automates essential maintenance tasks for Debian/Ubuntu-based systems.

## Features
- Updates package lists and upgrades all packages (`apt-get update` & `apt-get upgrade`)
- Cleans up unused packages and log files
- Backs up a specified directory (`/var/log` by default) to `/tmp` with a timestamp

## Usage

```bash
chmod +x system_maintenance.sh
sudo ./system_maintenance.sh
```

## Customization

- To change the directory to back up, edit `BACKUP_DIR` in the script.
- To change the backup destination, edit `BACKUP_DEST`.

## Requirements

- Linux system with apt package manager
- Run as root (`sudo` required)

## Output

- Backup file created in `/tmp` named like `system_backup_YYYY-MM-DD_HH-MM-SS.tar.gz`

## Notes

- Old logs (`/var/log/*.gz`) are deleted as part of cleanup.
- Script must be run with sudo for all operations.

---
