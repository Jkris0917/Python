from todo_func import add_task,show_task,delete_task,mark_as_done

def main():
    tasks =[]
    completed = []
    print("== To Do List App ==")
    
    while True:
        
        print("\n[1] - Show\n[2] - Add\n[3] - Mark Done\n[4] - Delete\n[5] - Quit")
    
        choose = input("Choose: ")
        if not choose.isdigit():
            print("Must be a number!")
            continue
        choose = int(choose)
        
        if choose == 1:
            show_task(tasks)
            
        elif choose == 2:
            task = input("Enter task: ")
            if not task.strip():
                print("Blank not allowed!")
                return
            add_task(tasks,task)
            
        elif choose == 3:
            show_task(tasks)
            try:
                index = int(input("  Mark task #: "))
                mark_as_done(tasks, completed, index)
            except ValueError:
                print("  Enter a number.")
                
        elif choose == 4:
            show_task(tasks)
            try:
                n = input("Delete task #: ")
                n = int(n)
                delete_task(tasks,n)
            except ValueError:
                print('Enter a number')
                
        elif choose == 5:
            print("\nGoodbye!")
            print("\n-- Completed --")
            for i, task in enumerate(completed, start=1):
                print(f"  {i}. {task}")
            print("\n-- Pending --")
            for i, task in enumerate(tasks, start=1):
                print(f"  {i}. {task}")
            break
main()