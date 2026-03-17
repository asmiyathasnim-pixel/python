# Overview:
# Mini Project 1 – To-Do List (Console-Based)
# ● Create a simple To-Do List using a list
# ● Features: Add a task, View all tasks, Delete a task
# 📌 Tasks:
# ✅ Implement functions for add_task(), view_tasks(), and delete_task()
# ✅ Test your functions by adding/deleting tasks


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


tasks = []      
add_task(tasks, "Finish homework")
add_task(tasks, "Read a book") 
add_task(tasks, "Go for a walk")     
add_task(tasks, "Buy groceries")
add_task(tasks, "Call a friend")
add_task(tasks, "Clean the house")
view_tasks(tasks)
delete_task(tasks, 2)
view_tasks(tasks)
delete_task(tasks, 3)
view_tasks(tasks)
