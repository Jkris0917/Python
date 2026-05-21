from todo_func import ToDoList

todo = ToDoList()
todo.load()
print("\n=== To do List App ===")

while True:
    print("[1] - Show [2] - Add [3] - Done [4] - Delete [5] - Summary [6] - Exit ")
    choose = input('Choose: ')
    if not choose.isdigit():
        print("Must be a number")
        continue
    choose = int(choose)
    
    if choose == 1:
        todo.show()
    elif choose == 2:
        title = input("  Task: ").strip()
        if not title:
            print("  Title cannot be blank.")
            continue
        todo.add(title)
        todo.save()
        todo.save_logs(f"Added: {title}")
    elif choose == 3:
        todo.show()
        index = input("  Mark done #: ")
        if not index.isdigit():
            print("  Must be a number.")
            continue
        todo.mark_as_done(int(index))
        todo.save()
        todo.save_logs(f"Marked done: task #{index}")
        todo.mark_as_done(index)
    elif choose == 4:
        todo.show()
        index = input(" Index: ")
        if not index.isdigit():
            print("Must be a number")
            continue
        todo.delete(int(index))
        todo.save()
        todo.save_logs(f"Deleted: Task #{index}")
    elif choose == 5:
        print(f"  Pending: {len(todo.pending())} | Done: {len(todo.completed())}")
    elif choose == 6:
        print(" Good Bye! ")
        break
