tasks=["python_practice", "free_code_camp", "skill_jars" ]
print("today your task is")
for index,  task in enumerate(tasks, start=1):
     print(f"{index}: {task}")
    
completed= input("Have you completed any task?   ")
if completed in tasks:
    print(f"{completed} is completed")
    remaining_tasks= [task for task in tasks if task != completed]
    print("uncompleted tasks are:")
    for index, task in enumerate(remaining_tasks, start=1):
     print(f"{index}: {task}")
else:
    print('task not found in the list')
    


    

    