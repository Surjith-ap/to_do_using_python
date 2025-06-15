import json

fileName = "to-do_List.json"

def loadTasks():
    try:
        with open(fileName, "r") as file:
            return json.load(file)
    except:
        return[]
def saveTasks(tasks):
    try:
        with open(fileName, "w") as file:
            return json.dump(tasks, file)
    except:
        print("Failed to Save")
    
def viewTasks(tasks):
    task_list = tasks["tasks"]
    if len(tasks["tasks"]) == 0:
        print("No Tasks")
    else :
        print("Your To-Do List")
        for idx, task in enumerate(task_list):
            status = "[completed]" if task["complete"] else "[pending]"
            print(f"{idx + 2}. {task['desc']} | {status}")
def createTasks(tasks):
    desc = input("Enter the task Desciption").strip()
    if desc:
        tasks["tasks"].append({"desciption": desc, "complete": False})
        saveTasks(tasks)
        print("Task Added")
    else:
        print("Desciption cannot be Empty.")
def completeTasks():
    pass

def main():
    tasks = loadTasks()

    while True:
        print("\nTo-Do List")
        print("1. View Tasks")
        print("2. Add Tasks")
        print("3. Complete Tasks")
        print("4. Exit")

        ch = input("Enter your Choice").strip()

        if ch == "1":
            viewTasks(tasks)
        elif ch == "2":
            createTasks()
        elif ch == "3":
            completeTasks()
        elif ch == "4":
            break
        else:
            print("Invalid Choice")

main()



