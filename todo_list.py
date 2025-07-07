from todo_list_manager import ToDoListManager

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            print(task)

def main():
    manager = ToDoListManager()

    while True:
        print("\n--- To-Do List Manager ---")
        print("1. Add Task")
        print("2. List All Tasks")
        print("3. List Completed Tasks")
        print("4. List Pending Tasks")
        print("5. Mark Task as Completed")
        print("6. Clear All Tasks")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Title: ")
            description = input("Description: ")
            due_date = input("Due Date: ")
            priority = input("Priority (Low/Medium/High): ")
            manager.add_task(title, description, due_date, priority)
            print("Task added.")

        elif choice == '2':
            print("\nAll Tasks:")
            display_tasks(manager.list_tasks())

        elif choice == '3':
            print("\nCompleted Tasks:")
            display_tasks(manager.list_completed_tasks())

        elif choice == '4':
            print("\nPending Tasks:")
            display_tasks(manager.list_pending_tasks())

        elif choice == '5':
            title = input("Enter the task title to mark as completed: ")
            if manager.mark_completed(title):
                print("Task marked as completed.")
            else:
                print("Task not found.")

        elif choice == '6':
            manager.clear_tasks()
            print("All tasks cleared.")

        elif choice == '7':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
