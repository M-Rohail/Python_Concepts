import random

# Computer choice


def computer_choice():
    random_number = random.randint(1, 3)
    options = {1: "Rock", 2: "Paper", 3: "Sciessor"}
    user1 = options[random_number]
    return user1

# User Input


def User_input():
    choice = int(
        input("Press 1 for Rock.\nPress 2 for Paper.\nPress 3 for Sciessor:\n"))
    option = {1: "Rock", 2: "Paper", 3: "Sciessor"}
    user2 = option[choice]
    return user2


i = True
while i:

    user = User_input()
    comp = computer_choice()

    print("You Selected:", user)
    print("Computer Selected:", comp)

    if comp == user:
        print("Draw!")

    if user == "Rock" and comp == "Sciessor":
        print("You Won!")
    elif user == "Rock" and comp == "Paper":
        print("Computer Won!")
    elif user == "Paper" and comp == "Rock":
        print("You Won!")
    elif user == "Sciessor" and comp == "Rock":
        print("Computer Won!")
    elif user == "Sciessor" and comp == "Paper":
        print("You Won!")
    elif user == "Paper" and comp == "Sciessor":
        print("Computer Won!")
    i = int(input("Want to play Again? :"))
    if i == 0:
        i = False
        print("Bye")
