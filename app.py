tasks = []

def show_tasks():
    print("Your current tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!")

def main():
    while True:
        print("\n1. Show tasks\n2. Add task\n3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
