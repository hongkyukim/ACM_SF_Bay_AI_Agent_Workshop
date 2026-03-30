"""Simple command-line To-Do list app written in Python."""

from __future__ import annotations


def show_menu() -> None:
    print("\nTo-Do Menu")
    print("1) View tasks")
    print("2) Add task")
    print("3) Mark task as done")
    print("4) Remove task")
    print("5) Quit")


def view_tasks(tasks: list[dict[str, object]]) -> None:
    if not tasks:
        print("No tasks yet. Add your first task!")
        return

    print("\nYour tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "✅" if task["done"] else "⬜"
        print(f"{i}. {status} {task['title']}")


def add_task(tasks: list[dict[str, object]]) -> None:
    title = input("Task title: ").strip()
    if not title:
        print("Task title cannot be empty.")
        return

    tasks.append({"title": title, "done": False})
    print("Task added.")


def mark_done(tasks: list[dict[str, object]]) -> None:
    if not tasks:
        print("No tasks to mark as done.")
        return

    view_tasks(tasks)
    try:
        task_number = int(input("Task number to mark done: "))
        if not 1 <= task_number <= len(tasks):
            raise ValueError
    except ValueError:
        print("Please enter a valid task number.")
        return

    tasks[task_number - 1]["done"] = True
    print("Task marked as done.")


def remove_task(tasks: list[dict[str, object]]) -> None:
    if not tasks:
        print("No tasks to remove.")
        return

    view_tasks(tasks)
    try:
        task_number = int(input("Task number to remove: "))
        if not 1 <= task_number <= len(tasks):
            raise ValueError
    except ValueError:
        print("Please enter a valid task number.")
        return

    removed = tasks.pop(task_number - 1)
    print(f"Removed: {removed['title']}")


def main() -> None:
    tasks: list[dict[str, object]] = []

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Please choose a valid menu option.")


if __name__ == "__main__":
    main()
