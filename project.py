import time

# Function to add task
def add_task(task_queue, name, pages):
    task = {"document_name": name, "pages": pages, "status": "Pending"}
    task_queue.append(task)
    print(f"\nTask added: {name} - {pages} pages - Status: Pending\n")

# Function to view pending tasks
def view_pending_tasks(task_queue):
    if not task_queue:
        print("\nNo pending tasks.\n")
    else:
        print("\nPending Tasks:")
        for i, task in enumerate(task_queue, 1):
            print(f"{i}. {task['document_name']} - {task['pages']} pages - Status: {task['status']}")
        print()

# Function to view completed tasks
def view_completed_tasks(completed_tasks):
    if not completed_tasks:
        print("\nNo completed tasks.\n")
    else:
        print("\nCompleted Tasks:")
        for i, task in enumerate(completed_tasks, 1):
            print(f"{i}. {task['document_name']} - {task['pages']} pages - Status: {task['status']}")
        print()

# Function to process tasks
def process_tasks(task_queue, completed_tasks):
    if not task_queue:
        print("\nNo tasks to process.\n")
        return
    print("\nProcessing tasks...\n")
    while task_queue:
        task = task_queue.pop(0)
        print(f"Printing: {task['document_name']} ({task['pages']} pages)")
        time.sleep(task['pages'] * 0.2)  # simulate printing delay
        task["status"] = "Completed"
        completed_tasks.append(task)
        print(f"Completed: {task['document_name']}\n")
    print("All tasks processed.\n")

# Function to search task by document name
def search_task(task_queue, completed_tasks, name):
    found = False
    print(f"\nSearching for task: {name}")
    for task in task_queue + completed_tasks:
        if task["document_name"].lower() == name.lower():
            print(f"Found: {task['document_name']} - {task['pages']} pages - Status: {task['status']}")
            found = True
            break
    if not found:
        print("Task not found.\n")

# Function to clear all completed tasks
def clear_completed_tasks(completed_tasks):
    if not completed_tasks:
        print("\nNo completed tasks to clear.\n")
    else:
        completed_tasks.clear()
        print("\nAll completed tasks cleared.\n")

# Function to view task count
def view_task_count(task_queue, completed_tasks):
    pending_count = len(task_queue)
    completed_count = len(completed_tasks)
    print(f"\nPending tasks: {pending_count}")
    print(f"Completed tasks: {completed_count}\n")

# Function to edit task
def edit_task(task_queue):
    if not task_queue:
        print("\nNo tasks available to edit.\n")
        return
    view_pending_tasks(task_queue)
    task_index = int(input("Enter the task number to edit: ")) - 1
    if 0 <= task_index < len(task_queue):
        new_pages = int(input("Enter the new number of pages: "))
        if new_pages < 1:
            print("Pages should be at least 1.\n")
        else:
            task_queue[task_index]["pages"] = new_pages
            print(f"Task updated: {task_queue[task_index]['document_name']} - {new_pages} pages\n")
    else:
        print("Invalid task number.\n")

# Function to show menu
def show_menu():
    print("==== Printing Task Scheduler ====")
    print("1. Add a Print Task")
    print("2. View Pending Tasks")
    print("3. Process All Tasks")
    print("4. View Completed Tasks")
    print("5. Search a Task")
    print("6. Clear Completed Tasks")
    print("7. View Task Count")
    print("8. Edit Task")
    print("9. Exit")

# Main program loop
def main():
    task_queue = []
    completed_tasks = []

    while True:
        show_menu()
        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            name = input("Enter document name: ")
            try:
                pages = int(input("Enter number of pages: "))
                if pages < 1:
                    print("Pages should be at least 1.\n")
                    continue
                add_task(task_queue, name, pages)
            except ValueError:
                print("Invalid input. Please enter a number for pages.\n")

        elif choice == "2":
            view_pending_tasks(task_queue)

        elif choice == "3":
            process_tasks(task_queue, completed_tasks)

        elif choice == "4":
            view_completed_tasks(completed_tasks)

        elif choice == "5":
            name = input("Enter document name to search: ")
            search_task(task_queue, completed_tasks, name)

        elif choice == "6":
            clear_completed_tasks(completed_tasks)

        elif choice == "7":
            view_task_count(task_queue, completed_tasks)

        elif choice == "8":
            edit_task(task_queue)

        elif choice == "9":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 9.\n")

# Run the program
if __name__ == "__main__":
    main()