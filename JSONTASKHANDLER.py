project = "focus.txt"
task_id = 1

def delete_function(task_number):
    with open(project) as file:
        lines = file.readlines()
    if 0 < task_number <= len(lines):
        del lines[task_number - 1]
        with open(project, "w") as file:
            for line in lines:
                file.write(line)
        print(f"Task {task_number} deleted successfully!")
        with open(project, "r") as file:
            print(file.read())
    else:
        print("No task with that ID")

def mark_done(task_number):
    with open(project) as file:
        lines = file.readlines()
    
    if 0 < task_number <= len(lines):
        line = lines[task_number - 1]
        if "X" not in line:
            lines[task_number - 1] = line.rstrip('\n') + " X\n"
        else:
            lines[task_number - 1] = line.replace(" X", "").rstrip('\n') + "\\n"
        
        with open(project, "w") as file:
            for line in lines:
                file.write(line)
        print(f"Task {task_number} updated!")
        with open(project, "r") as file:
            print(file.read())
    else:
        print("No task with that ID")

def add_task():
    global task_id
    while True:
        user_input = input("Add task (if not, type done): ")
        if user_input.lower() == "done":
            return
        with open(project, "a") as file:
            file.write(f"{task_id}. {user_input}\n")
        print(f"Task {task_id} added successfully!")
        task_id += 1
        with open(project, "r") as file:
            print(file.read())

with open(project, "w") as file:
    pass


while True:
    user_input = input("Add task (if not, type done): ")
    if user_input.lower() == "done":
        break
    with open(project, "a") as file:
        file.write(f"{task_id}. {user_input}\n")
    task_id += 1

print("All done. Your tasks today are:")
with open(project, "r") as file:
    print(file.read())


with open(project, "r") as file:
    lines = file.readlines()

while True and lines:
    user_input2 = input("What's your next move? [D] to delete, [M] to mark as done, [A] to add more tasks, [Q] to quit: ")
    
    if user_input2.upper() == "Q":
        print("Goodbye!")
        break
    elif user_input2.upper() == "A":
        add_task()
    else:
        try:
            user_input3 = int(input("Select a task by its number: "))
            if user_input2.upper() == "D":
                delete_function(user_input3)
            elif user_input2.upper() == "M":
                mark_done(user_input3)
        except ValueError:
            print("Please enter a valid number")

