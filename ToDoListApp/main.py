from todo_func import add_task,show_task,delete_task

def main():
    tasks =[]
    print("== To Do List App ==")
    print("\n[1] - Show\n[2] - Add\n[3] - Delete\n[4] - Quit")
    
    choose = input("Choose a number: ")
    if not choose.isdigit():
        print("Must be a number!")
        return
    choose = int(choose)
    while True:
        if choose == 1:
            show_task(tasks)
        elif choose == 2:
            task = input("Enter task: ")
            if task.strip() == " ":
                print("Blank not allowed!")
                return
            add_task(tasks,task)
        elif choose == 3:
            show_task(tasks)
            try:
                index = int(input("Input number: "))
                delete_task(tasks,index)
            except ValueError:
                print('Enter a number')
        elif choose == 4:
            print("Goodbye")
            break
main()