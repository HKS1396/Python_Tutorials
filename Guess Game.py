print("Welcome to the guess game - Find the hidden number")
count=1
while(True):
    if count>9:
        print("Game Over : You Lose")
        break
    else:
        n=int(input("Enter a number\n"))
        if n==18:
            print("Congractulation you won ","no of guess used ", count)
            break
        elif n<18:
            print("Enter a greater number! Try Again.15\n", "No of Guesses left", 9-count)
            count = count + 1
            continue
        else:
            print("Enter a lesser number! Try Again.\n", "No of Guesses left", 9 - count)
            count= count +1
            continue