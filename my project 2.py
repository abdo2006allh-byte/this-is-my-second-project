tasks = []

def add_task(task: str) -> None:
    """Add a new task"""
    tasks.append(task)
    print(f"✅ Task added: {task}")

def show_tasks() -> None:
    """Show all tasks"""
    if not tasks:
        print("📭 No tasks exist now.")
    else:
        print("\n📋 Main Task List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def delete_task(index: int) -> bool:
    """Delete a task by its number, returns True if it is deleted"""
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"🗑️ The task has been deleted: {removed}")
        return True
    else:
        print("❌ This number is not valid")
        return False
    
def main():
    while True:
        print("\n______ Main Menu ______")
        print("1. Add task")
        print("2. Show tasks")
        print("3. Delete task")
        print("4. Count number of tasks")
        print("5. Exit")

        choice = input("Choose a number: ")

        if choice == "1":
            task = input("Write a task: ")
            add_task(task)

        elif choice == "2":
            show_tasks()

        elif choice == "3":
            show_tasks()
            if tasks:
                try:
                    num = int(input("Write the number of the task to delete: ")) - 1
                    delete_task(num)
                except ValueError:
                    print("❌ You must enter a valid number.")

        elif choice == "4":
            count = len(tasks)
            print(f"📊 Number of tasks: {count}")

        elif choice == "5":
            print("👋 Thank you, goodbye!")
            break

        else:
            print("❌ Invalid choice, try again.")

# Run the program
main()
