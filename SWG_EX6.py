import random

lst = ["Snake", "Water", "Gun"]
user_wins = 0
system_wins = 0


def inp1():
    c = input("Enter S for Snake  | W for Water   |   G for Gun\n")
    if c == "S":
        return "Snake"
    elif c == "W":
        return "Water"
    elif c == "G":
        return "Gun"
    else:
        print("Wrong Input! Try Again.\n")
        inp1()


def win(u, s):
    if u == s:
        return "Tie"
    elif u == "Snake" and s == "Water":
        return "User Win"
    elif u == "Snake" and s == "Gun":
        return "System Win"
    elif u == "Water" and s == "Snake":
        return "System Win"
    elif u == "Water" and s == "Gun":
        return "User Win"
    elif u == "Gun" and s == "Snake":
        return "User Win"
    else:
        return "System Win"


def main():
    n = 1
    global user_wins
    global system_wins
    while n <= 10:
        print(f"Round {n}:\n")
        user_choice1 = inp1()
        system_choice = random.choice(lst)
        result = win(user_choice1, system_choice)
        if result == "User Win":
            user_wins += 1
            print(result + " this round\n")
        elif result == "System Win":
            system_wins += 1
            print(result + " this round\n")
        else:
            print(result + "\n")
        n += 1
    if user_wins > system_wins:
        print(f"Congratulation You Won!!! User Points {user_wins} System Points {system_wins}")
    elif system_wins > user_wins:
        print(f"Alas You Loose!!! User Points {user_wins} System Points {system_wins}")
    else:
        print("Tie")


main()
