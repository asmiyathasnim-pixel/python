# Overview:
# Mini Project 2 – Interactive To-Do App (With File Storage)
# ● Implement To-Do List with UI (CLI-based)
# ● Save tasks using file storage
# 📌 Final project submission and interview

import pickle
def save_tasks(task_list):
    with open("todo_tasks.pkl", "wb") as file:
        pickle.dump(task_list, file)
def load_tasks():
    try:
        with open("todo_tasks.pkl", "rb") as file:
            tasks = pickle.load(file)
            return tasks
    except FileNotFoundError:
        return []
def add_task(task_list, task):
    task_list.append(task)
    print(f'Task "{task}" added.')
def view_tasks(task_list):
    if not task_list:
        print("No tasks in the list.")
    else:
        print("To-Do List:")
        for idx, task in enumerate(task_list, start=1):
            print(f"{idx}. {task}")
def delete_task(task_list, task_number):
    if 0 < task_number <= len(task_list):
        removed_task = task_list.pop(task_number - 1)
        print(f'Task "{removed_task}" deleted.')
    else:
        print("Invalid task number.")
tasks = load_tasks()
while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    choice = input("Choose an option (1-4): ")
    if choice == '1':
        task = input("Enter the task to add: ")
        add_task(tasks, task)
        save_tasks(tasks)
    elif choice == '2':
        view_tasks(tasks)
    elif choice == '3':
        task_number = int(input("Enter the task number to delete: "))
        delete_task(tasks, task_number)
        save_tasks(tasks)
    elif choice == '4':
        print("Exiting To-Do List App. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")