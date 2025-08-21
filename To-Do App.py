tasks = []

while True:
    task = input("Enter a task (or type 'quit' to stop):")
    if task.lower() == "quit":
        break
    tasks.append(task)
    print(f"Task '{task}' added!")

print("\nYour tasks:")
for t in tasks:
    print("-", t)