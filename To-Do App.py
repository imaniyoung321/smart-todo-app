tasks = []

while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append({"task": task, "done": False}) # store task and it's status
        print(f"Task '{task}' added!")
    elif choice == "2":
        print("\nYour tasks:")
        if not tasks:
            print("No tasks yet.")
        else:
            for i, t in enumerate(tasks, start=1):
                status = "*" if t["done"] else "X"
                print(f"{i}. {t['task']} [{status}]")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")