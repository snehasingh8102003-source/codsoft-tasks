task = []
while True:
    print("\n 1.add_task")
    print("2.view_task")
    print("3.remove_task")
    print("4.exit")
    a=input("enter choice (1-4): ")

    if a=="1":
        b=input("enter task: ")    
        # print("input_task")
        task.append(b)
        print("your task added")

    elif a=="2":
        if not list:
            print("no task avilable")
        else:
            print("your task")
        for i, list in enumerate(task,start=1):
            print(i,task)

    elif a=="3":
        if not list:
            print("no task to remove")
        else:
            try:
                a1=int(input("enter the task_no. which you want to remove"))
                if (1<=a1<=len(task)):
                    remove=task.pop(a1-1)
                    print("task removed")
                else:
                    print("invalid task")
            except:
                print("enter valid task")

    elif a=="4":
        print("Thank you for using list.")
        break

    else:
        print("invalid choice")
