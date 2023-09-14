# Create an empty list
tasks =[]
# Function to add task to list
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added")

# Function to view all the tasks in the list
def view_tasks():
    if not tasks:
        print("No tasks in the list")
    else:
        print("Tasks: ")
        for index, task in enumerate(tasks, start = 1):
            print(f"{index}. {task}")

# Function to remove task from list
def remove_task(task_index):
    if 1 <= task_index <= len(tasks):
        removed_task  = tasks.pop(task_index-1)
        print(f"Task '{removed_task}' removed.")
    else:
        print("Invalid task index.")

# Main Loop

while(True):
    print("\nOptions:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        task_index = int(input("Enter the task to remove: "))
        remove_task(task_index)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, Please try again")
