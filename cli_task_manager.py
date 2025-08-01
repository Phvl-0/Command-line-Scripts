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

# --- Constants ---
TASKS_FILE = "tasks.json"

# --- Functions ---

def load_tasks():
    """Loads tasks from a JSON file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Saves tasks to a JSON file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    """Adds a new task."""
    task_description = input("Enter a new task: ")
    if task_description:
        new_task = {
            "id": len(tasks) + 1,
            "description": task_description,
            "completed": False
        }
        tasks.append(new_task)
        save_tasks(tasks)
        print(f"Task '{task_description}' added.")
    else:
        print("Task cannot be empty.")

def view_tasks(tasks):
    """Displays all tasks."""
    if not tasks:
        print("No tasks found.")
        return
    
    print("\n======================================")
    print("           Your Tasks")
    print("======================================")
    for task in tasks:
        status = "[DONE]" if task["completed"] else "[ ]"
        print(f"{status} {task['id']}. {task['description']}")
    print("======================================")
    
def mark_complete(tasks):
    """Marks a task as complete."""
    view_tasks(tasks)
    try:
        task_id = int(input("Enter the ID of the task to mark as complete: "))
        found = False
        for task in tasks:
            if task["id"] == task_id:
                task["completed"] = True
                found = True
                break
        
        if found:
            save_tasks(tasks)
            print(f"Task {task_id} marked as complete.")
        else:
            print(f"Task with ID {task_id} not found.")

    except ValueError:
        print("Invalid input. Please enter a number.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main_menu():
    """Displays the main menu and handles user input."""
    tasks = load_tasks()
    
    while True:
        print("\n--- CLI Task Manager ---")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Mark a task as complete")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_complete(tasks)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# --- Main script execution ---
if __name__ == "__main__":
    main_menu()

