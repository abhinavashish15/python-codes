def task():
    tasks=[]
    print("----WELCOME TO THE TASK MANAGEMENT APP----")

    total_task=int(input("Enter how many task you want to add = "))
    for i in range(1, total_task+1):
        task_name=input(f"Enter task {i} = ")
        tasks.append(task_name)

    print(f"Today's tasks are\n{tasks}")

    while True:
        operation=int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop/"))
        if operation==1:
            add = input("Enter task you want to add = ")
            tasks.append(add)
            print(f"Task {add} has been successfully added")

        elif operation==2:
            updated_val=input("Enter the task name you want to update =")
            up=input("Enter new task =")
            index = tasks.index(updated_val)
            tasks[index]=up
            print(f"Updated task {up}")

        elif operation==3:
            delelte_value=input("Enter task you want to delete = ")
            if delelte_value in tasks:
                index = tasks.index(delelte_value)
                del tasks[index]
                print(f"Task {delelte_value} has been deleted.")
    
        elif operation==4:
            print(f"Total tasks = {tasks}")

        elif operation==5:
            print("Closing the application..")
            break
        else:
            print("The entered number is invalid..")


if __name__=="__main__":
    task()