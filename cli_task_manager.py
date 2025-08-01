#!/usr/bin/env python3

# ==============================================================================
# CLI Task Management Application
# ------------------------------------------------------------------------------
# A simple command-line application for managing tasks.
# Users can add new tasks, view all tasks, and mark tasks as complete.
# The tasks are saved to a file for persistence.
# ==============================================================================

import os
import json
from uuid import uuid4

# --- Constants ---
TASKS_FILE = os.getenv("TASKS_FILE", "tasks.json")

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

# --- Task Operations ---

def load_tasks():
    """Loads tasks from a JSON file."""
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, 'r') as file:
                return json.load(file)
        except Exception as e:
            print(f"Error loading tasks: {e}")
            return []
    return []

def save_tasks(tasks):
    """Saves tasks to a JSON file."""
    try:
        with open(TASKS_FILE, 'w') as file:
            json.dump(tasks, file, indent=4)
    except Exception as e:
        print(f"Error saving tasks: {e}")

def add_task(tasks):
    """Adds a new task."""
    clear_screen()
    task_description = input("Enter a new task: ").strip()
    if not task_description:
        print("Task cannot be empty.")
        input("Press Enter to continue...")
        return

    new_task = {
        "id": str(uuid4()),
        "description": task_description,
        "completed": False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task '{task_description}' added.")
    input("Press Enter to continue...")

def view_tasks(tasks):
    """Displays all tasks."""
    clear_screen()
    if not tasks:
        print("No tasks found.")
        input("Press Enter to continue...")
        return

    print("\n======================================")
    print("           Your Tasks")
    print("======================================")
    for i, task in enumerate(tasks, 1):
        status = "[DONE]" if task["completed"] else "[ ]"
        print(f"{status} {i}. {task['description']} (ID: {task['id']})")
    print("======================================")
    input("Press Enter to continue...")

def find_task_by_id(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None

def mark_complete(tasks):
    """Marks a task as complete."""
    clear_screen()
    view_tasks(tasks)
    task_id = input("Enter the ID of the task to mark as complete: ").strip()
    task = find_task_by_id(tasks, task_id)
    if task:
        if task["completed"]:
            print("Task is already completed.")
        else:
            task["completed"] = True
            save_tasks(tasks)
            print("Task marked as complete.")
    else:
        print("Task ID not found.")
    input("Press Enter to continue...")

def delete_task(tasks):
    """Deletes a task by ID."""
    clear_screen()
    view_tasks(tasks)
    task_id = input("Enter the ID of the task to delete: ").strip()
    task = find_task_by_id(tasks, task_id)
    if task:
        tasks.remove(task)
        save_tasks(tasks)
        print("Task deleted.")
    else:
        print("Task ID not found.")
    input("Press Enter to continue...")

def edit_task(tasks):
    """Edit a task's description."""
    clear_screen()
    view_tasks(tasks)
    task_id = input("Enter the ID of the task to edit: ").strip()
    task = find_task_by_id(tasks, task_id)
    if task:
        new_desc = input("Enter the new description: ").strip()
        if new_desc:
            task["description"] = new_desc
            save_tasks(tasks)
            print("Task updated.")
        else:
            print("Description cannot be empty.")
    else:
        print("Task ID not found.")
    input("Press Enter to continue...")

# --- Main Menu ---

def main_menu():
    """Displays the main menu and handles user input."""
    tasks = load_tasks()

    menu = (
        "\n--- CLI Task Manager ---\n"
        "1. Add a new task\n"
        "2. View all tasks\n"
        "3. Mark a task as complete\n"
        "4. Edit a task\n"
        "5. Delete a task\n"
        "6. Exit\n"
    )

    while True:
        clear_screen()
        print(menu)
        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_complete(tasks)
        elif choice == '4':
            edit_task(tasks)
        elif choice == '5':
            delete_task(tasks)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
            input("Press Enter to continue...")

# --- Main script execution ---
if __name__ == "__main__":
    main_menu()
