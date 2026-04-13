"""Simple Task Tracker

This script helps you create a checklist at the start of the day and, at the
end of the day, split tasks into `completed_tasks` and `incomplete_tasks`.

Usage (interactive):
  python task_tracker.py

The script will prompt for tasks and then ask which tasks were completed.
It can also save the results to `tasks.json`.
"""
import json
from typing import List, Tuple


def create_checklist() -> List[str]:
    """Interactively create a list of tasks."""
    tasks = []
    try:
        n = int(input("How many tasks for today? "))
    except ValueError:
        print("Please enter a valid integer."
              " Starting with 0 tasks.")
        n = 0

    for i in range(n):
        t = input(f"Task {i+1}: ").strip()
        if t:
            tasks.append(t)
        else:
            tasks.append(f"(empty task {i+1})")
    return tasks


def review_tasks(tasks: List[str]) -> Tuple[List[str], List[str]]:
    """Ask which tasks were completed and return two lists.

    Two interaction modes are supported:
      1) Enter indices of completed tasks separated by spaces (e.g. "1 3 4")
      2) For each task, answer Y/N when prompted
    """
    if not tasks:
        return [], []

    print("\nYou can enter completed task numbers separated by spaces (e.g. '1 3'),")
    print("or press Enter to answer Y/N for each task.")
    choice = input("Enter completed indices or press Enter to proceed: ").strip()

    completed = []
    incomplete = []

    if choice:
        # parse indices
        parts = choice.split()
        indices = set()
        for p in parts:
            try:
                idx = int(p) - 1
                if 0 <= idx < len(tasks):
                    indices.add(idx)
                else:
                    print(f"Ignoring out-of-range index: {p}")
            except ValueError:
                print(f"Ignoring invalid token: {p}")

        for i, t in enumerate(tasks):
            if i in indices:
                completed.append(t)
            else:
                incomplete.append(t)
    else:
        # Ask Y/N for each
        for i, t in enumerate(tasks, start=1):
            while True:
                ans = input(f"Did you complete task {i} - '{t}'? (y/n): ").strip().lower()
                if ans in ("y", "yes"):
                    completed.append(t)
                    break
                if ans in ("n", "no"):
                    incomplete.append(t)
                    break
                print("Please answer 'y' or 'n'.")

    return completed, incomplete


def save_tasks(filename: str, completed: List[str], incomplete: List[str]) -> None:
    payload = {
        "completed_tasks": completed,
        "incomplete_tasks": incomplete,
    }
    with open(filename, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, ensure_ascii=False)
    print(f"Saved results to {filename}")


def main() -> None:
    print("Task Tracker — create your checklist for the day")
    tasks = create_checklist()
    print("\nChecklist created.\n")
    completed, incomplete = review_tasks(tasks)

    print("\n--- Summary ---")
    print(f"Completed ({len(completed)}):")
    for t in completed:
        print(" - ", t)
    print(f"\nIncomplete ({len(incomplete)}):")
    for t in incomplete:
        print(" - ", t)

    save = input("\nSave results to tasks.json? (y/n): ").strip().lower()
    if save in ("y", "yes"):
        save_tasks("tasks.json", completed, incomplete)


if __name__ == "__main__":
    main()
