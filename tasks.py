# Simple CLI Task Manager

tasks = {
    "Complete homework": "High",
    "Clean room": "Medium"
}

def display_menu():
    print("\n===== Personal Task Manager =====")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Save tasks to file")
    print("5. Load tasks from file")
    print("6. Exit")

def add_task():
    task = input("Enter task name: ").strip()
    priority = input("Enter priority (Low, Medium, High): ").strip().capitalize()

    if task == "" or priority == "":
        print("❌ Task or priority cannot be empty.")
        return

    tasks[task] = priority
    print(f"✅ Task '{task}' added with priority '{priority}'.")

def view_tasks():
    if not tasks:
        print("📭 No tasks found.")
    else:
        print("\n📋 Current Tasks:")
        for index, (task, priority) in enumerate(tasks.items(), start=1):
            print(f"{index}. {task} - {priority}")

def remove_task():
    task = input("Enter the task name to remove: ").strip()
    if task in tasks:
        del tasks[task]
        print(f"🗑️ Task '{task}' removed.")
    else:
        print("❌ Task not found.")

def save_tasks():
    try:
        with open("tasks.txt", "w") as file:
            for task, priority in tasks.items():
                file.write(f"{task}:{priority}\n")
        print("💾 Tasks saved to 'tasks.txt'.")
    except Exception as e:
        print(f"⚠️ Failed to save tasks: {e}")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks.clear()
            for line in file:
                if ":" in line:
                    task, priority = line.strip().split(":", 1)
                    tasks[task] = priority
        print("📂 Tasks loaded from 'tasks.txt'.")
    except FileNotFoundError:
        print("⚠️ File 'tasks.txt' not found. No tasks loaded.")
    except Exception as e:
        print(f"⚠️ Error loading tasks: {e}")

def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1–6): "))
        except ValueError:
            print("❌ Invalid input. Please enter a number between 1 and 6.")
            continue

        if choice == 1:
            add_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            remove_task()
        elif choice == 4:
            save_tasks()
        elif choice == 5:
            load_tasks()
        elif choice == 6:
            print("👋 Exiting Task Manager. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

# Start the program
main()
