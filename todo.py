TASKS_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from file."""
    try:
        with open(TASKS_FILE, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
        return tasks
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Save tasks to file."""
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def view_tasks(tasks):
    """Display current tasks."""
    if not tasks:
        print("🟦 No tasks yet. Add some!")
    else:
        print("📋 Your To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def add_task(tasks):
    """Add tasks with custom date and time."""
    print("➤ Enter tasks (Separate multiple tasks with a comma):")
    input_text = input("> ").strip()
    new_tasks_raw = [task.strip() for task in input_text.split(",") if task.strip()]

    if new_tasks_raw:
        timestamped_tasks = []
        for task in new_tasks_raw:
            print(f"🕒 Enter date and time for '{task}' (e.g., 06-08-2025 15:30):")
            user_datetime = input("Date & Time > ").strip()
            timestamped_tasks.append(f"{task} (scheduled for {user_datetime})")

        tasks.extend(timestamped_tasks)
        message = "task" if len(new_tasks_raw) == 1 else "tasks"
        print(f"✅ Added {len(new_tasks_raw)} {message}.")
    else:
        print("⚠️ No valid tasks entered.")



def remove_task(tasks):
    """Remove one or multiple tasks by their number."""
    view_tasks(tasks)
    print("➤ Enter task number(s) to remove (Separate with commas):")
    input_text = input("< ").strip()
    try:
        indices = [int(i.strip()) for i in input_text.split(",")]
        removed = []
        for index in sorted(indices, reverse=True):
            if 1 <= index <= len(tasks):
                removed_task = tasks.pop(index - 1)
                removed.append(removed_task)
            else:
                print(f"⚠️ Task {index} does not exist.")
        if removed:
            print("🗑️ Removed:")
            for task in removed:
                print(f"- {task}")
        else:
            print("⚠️ No valid task numbers entered.")
    except ValueError:
        print("⚠️ Please enter valid number(s).")



def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View Tasks | 2. Add Task | 3. Remove Task | 4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("📦 Tasks saved!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
