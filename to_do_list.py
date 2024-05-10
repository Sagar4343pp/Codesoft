tasks = []

def add_task(task):
    tasks.append(task)
    print('Task added successfully............')

def update_task(index, new_task):
    if 0 <= index  < len(tasks):
        tasks[index] = new_task
        print('task update successfully....')
    else:
        print("invalid task index")

def display_task():
    if tasks:
        print("TO-DO List")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("Your TO-DO List is Empty")



def main():
    while True:
        print("1. Add Task")
        print("2. Update Task")
        print("3. Display Tasks")
        print("4. Exit")


        choice  = input("Enter your Choice: ")

        if choice == "1":
            task = input("enter your Task: ")
            add_task(task)
        elif choice == "2":
            index = int(input("Enter index of the task to update"))
            new_task = input("Enter the New Taask: ")
            update_task(index -1, new_task)
        elif choice == "3":
            display_task()
        elif choice == "4":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
