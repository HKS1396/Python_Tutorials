def getdate():
    import datetime
    return datetime.datetime.now()


def client_input():
    c = int(input("Enter 1 for Harry log\n2 for rohan log\n3 for hammad log\n"))
    if c == 1:
        c2 = int(input("Enter 1 to log food\n 2 to log exercise\n"))
        if c2 == 1:
            with open("Harry_food.txt", "a") as f:
                harry_food_input = input("Enter the diet to be logged\n")
                f.write("\n"+"[" + str(getdate()) + "] " + harry_food_input)
        else:
            with open("Harry_ex.txt", "a") as f:
                harry_ex_input = input("Enter the Exercise to be logged\n")
                f.write("\n"+"[" + str(getdate()) + "] " + harry_ex_input)
    elif c == 2:
        c2 = int(input("Enter 1 to log food\n 2 to log exercise\n"))
        if c2 == 1:
            with open("Rohan_food.txt", "a") as f:
                rohan_food_input = input("Enter the diet to be logged\n")
                f.write("\n"+"[" + str(getdate()) + "] " + rohan_food_input)
        else:
            with open("Rohan_ex.txt", "a") as f:
                rohan_ex_input = input("Enter the Exercise to be logged\n")
                f.write("\n"+"[" + str(getdate()) + "] " + rohan_ex_input)
    elif c == 3:
        c2 = int(input("Enter 1 to log food\n 2 to log diet\n"))
        if c2 == 1:
            with open("Hammad_food.txt", "a") as f:
                hammad_food_input = input("Enter the diet to be logged\n")
                f.write("\n"+"[" + str(getdate()) + "] " + hammad_food_input)
        else:
            with open("Hammad_ex.txt", "a") as f:
                hammad_ex_input = input("Enter the Exercise to be logged\n")
                f.write("\n"+"[" + str(getdate()) + "] " + hammad_ex_input)
    else:
        print("Incorrect input\n")
    print("Logged Successfully\n")


def client_output():
    c = int(input("Enter 1 for Harry log\n2 for rohan log\n3 for hammad logs\n"))
    if c == 1:
        c2 = int(input("Enter 1 to read food logs\n 2 to read exercise logs\n"))
        if c2 == 1:
            with open("Harry_food.txt", "r") as f:
                print(f.readlines())
        else:
            with open("Harry_ex.txt", "r") as f:
                print(f.readlines())
    elif c == 2:
        c2 = int(input("Enter 1 to read food logs\n 2 to read exercise logs\n"))
        if c2 == 1:
            with open("Rohan_food.txt", "r") as f:
                print(f.readlines())
        else:
            with open("Rohan_ex.txt", "r") as f:
                print(f.readlines())
    elif c == 3:
        c2 = int(input("Enter 1 to read food logs\n 2 to read exercise logs\n"))
        if c2 == 1:
            with open("Hammad_food.txt", "r") as f:
                print(f.readlines())
        else:
            with open("Hammad_ex.txt", "r") as f:
                print(f.readlines())
    else:
        print("Incorrect input\n")


c3 = int(input("Enter 1 to log data\n Enter 2 to read logs\n"))
if c3 == 1:
    client_input()
else:
    client_output()