
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
