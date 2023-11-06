# To-Do List Application
tasks = []
# Function to display the tasks in the to-do list
def display_tasks():
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        print("Tasks in the to-do list:")
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task}")

# Function to add a task to the to-do list
def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added to the to-do list.")

def edit_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task edit to the to-do list.")

# Function to mark a task as complete
def complete_task():
    display_tasks()
    task_index = int(input("Enter the task number to mark as complete: ")) - 1
    if 0 <= task_index < len(tasks):
        print(f"Task '{tasks[task_index]}' marked as complete.")
        tasks.pop(task_index)
    else:
        print("Invalid task number.")

# Function to delete a task from the to-do list
def delete_task():
    display_tasks()
    task_index = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_index < len(tasks):
        print(f"Task '{tasks[task_index]}' deleted.")
        tasks.pop(task_index)
    else:
        print("Invalid task number.")

# Main function to run the To-Do List application
def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. edit task")
        print("4. Mark Task as Complete")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            display_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            edit_task()
        elif choice == '4':
            complete_task()
        elif choice == '5':
            delete_task()
        elif choice == '6':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
