from datetime import datetime

tasks = []

while True:
    print("\n=== Daily Agent ===")
    print("1. Show Date")
    print("2. Add Task")
    print("3. View Tasks")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        print("Today's Date:", datetime.now().strftime("%Y-%m-%d"))

    elif choice == "2":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "3":
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option!")