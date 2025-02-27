import guessing_game as gg
import calculator as calc
import to_do as td

def main():
    #gg.game()
    
    #calc.div(1, 0)

    tasks = []

    while True:
        print("\n--- To-Do List App ---")
        print("1. List tasks")
        print("2. Add task")
        print("3. Toggle task completion")
        print("4. Remove task")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            if not tasks:
                print("No tasks in your to-do list.")
            else:
                print("\nYour Tasks:")
                for idx, task in enumerate(tasks, start=1):
                    status = "Completed" if task.state.get_value() else "Pending"
                    print(f"{idx}. {task.description} - {status}")
        elif choice == "2":
            description = input("Enter task description: ").strip()
            if description:
                task = td.Task(description)
                tasks.append(task)
                print("Task added.")
            else:
                print("Task description cannot be empty.")
        elif choice == "3":
            if not tasks:
                print("No tasks to toggle.")
                continue
            try:
                index = int(input("Enter the task number to toggle: ").strip())
                if 1 <= index <= len(tasks):
                    tasks[index - 1].state.toggle_value()
                    print("Task state toggled.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == "4":
            if not tasks:
                print("No tasks to remove.")
                continue
            try:
                index = int(input("Enter the task number to remove: ").strip())
                if 1 <= index <= len(tasks):
                    removed = tasks.pop(index - 1)
                    print(f"Removed task: {removed.description}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()