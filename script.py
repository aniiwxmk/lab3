import module

choice = int(input("Please, choose the task 1-2 (0-EXIT): "))
while choice:
    if choice==1:
        module.task1();
    elif choice==2:
        module.process_matrix();
    else:
        print("Wrong task number!")
    choice = int(input("Please, choose the task again (0-EXIT): "))
print("Good by!") 