def show_task(tasks):
    """Display All the Task"""
    if not tasks:
        print('No task yet')
        return
    for i,task in enumerate(tasks,start=1):
        print(f'{i}: {task}')

def add_task(tasks, task):
    """Add Task"""
    if task == 'exit':
        return
    tasks.append(task)
    print(f"Added: {task}")
    
def delete_task(tasks,index):
    """Delete Tast"""
    if 1 <= index <= len(tasks):
        removed = tasks.remove(index-1)
        print(f"Deleted: '{removed}'")
    else:
        print('Invalid task number')