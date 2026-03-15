# Create an empty list to store the tasks and their status
todo_list = []
#Function to Add a New Task
def add_task():
    task = input("Enter a task:")
    todo_list.append({"Task":task,"Status": "pending"})
    print("New Task Added Successfully!\n")
#Function to View All Task
def view_task():
    print("your Todo List:")
    if len(todo_list) == 0:
        print("No pending tasks!")
    else:
        for index, task in enumerate(todo_list, 1):
            print(f"{index}:{task['Task']} - {task['Status']}")
    print("\n")
#Function to Remove a Task
def remove_task():
    if len(todo_list) == 0:
        print("List Empty!")
    else:
        try:   
            search_index = int(input("Enter the task number that you want to remove:")) - 1
            if 0 <= search_index < len(todo_list):
             removed_task = todo_list.pop(search_index)
             print(f"Task Removed: {removed_task['Task']}")
            else: 
             print("Invalid task Number.")
        except ValueError:
            print("Please Enter a valid Task Number.")
         

#Function to Mark a Task completed
def mark_task():
    if len(todo_list) == 0:
        print("List Empty!")
    else:
        try:   
            search_index = int(input("Enter the task number that you want to mark as complete:")) - 1
            if 0 <= search_index < len(todo_list):
             todo_list[search_index]['Status'] = 'done'
             print(f"Task {todo_list[search_index]['Task']}has been marked as Done.")
            else: 
             print("Invalid task Number.")
        except ValueError:
            print("Please Enter a valid Task Number.")
    
#Function to Display a menu
def menu():
    while (True):
        print("** Mian Menu**")
        print("1. Add a New Tasks")
        print("2. View All Tasks")
        print("3. Remove a Tasks")
        print("4. Mark a task as completed")
        print("5. Exit")

        choice = input("Enter your choice:")
        if choice =="1":
            add_task()
        elif choice =="2":
            view_task()
        elif choice =="3":
            remove_task()
        elif choice =="4":
            mark_task()
        elif choice =="5":
            print("Exiting this application....")
            exit()
        else:
            print("Invalid choice! Try again!!!")

menu()