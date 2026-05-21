import json
from datetime import datetime

FILENAME = 'ToDoListApp/todolist.json'
LOGS = 'ToDoListApp/logs.txt'

class Task:
    
    def __init__(self, title):
        self.title = title
        self.completed = False
        
    def mark_done(self):
        self.completed = True
        print(f" ✓ '{self.title}' mark as done")
        
    def __str__(self):
        status = "✓" if self.completed else "○"
        return f"{[status]} {self.title}"
    
    def to_dict(self):
        return{
            "title": self.title,
            "completed": self.completed
        }
    
class ToDoList:
    
    def __init__(self):
        self.tasks = []
        
    def add(self,title):
        task = Task(title)
        self.tasks.append(task)
        print(f" Added {title}")
        
    def show(self):
        if not self.tasks:
            print(" No task yet.")
            return
        for i, task in enumerate(self.tasks,start=1):
            print(f"{i}. {task}")
    
    def mark_as_done(self,index):
        if 1 <= index <= len(self.tasks):
            self.tasks[index-1].mark_done()
        else:
            print(" Invalid number")
    
    def delete(self,index):
        if 1 <= index <= len(self.tasks):
            removed = self.tasks.pop(index-1)
            print(f"Deleted: {removed.title}")
        else:
            print(" Invalid number.")
            
    def pending(self):
        return [t for t in self.tasks if not t.completed]

    def completed(self):
        return [t for t in self.tasks if t.completed]
    
    def save(self):
        data = [task.to_dict() for task in self.tasks]
        with open(FILENAME, 'w') as f:
            json.dump(data, f, indent=2)
        print(' Saved.')
    
    def load(self):
        try:
            with open(FILENAME,'r') as f:
                data = json.load(f)
            self.tasks = []
            for item in data:
                task = Task(item["title"])
                task.completed= item["completed"]
                self.tasks.append(task)
        except FileNotFoundError:
            self.tasks = []
            
    
    def save_logs(self,action):
        timestamp = datetime.now().strftime("%Y=%m-%d %H:%M:%S")
        with open(LOGS,'a') as f:
            f.write(f"[{timestamp}] - {action}\n")