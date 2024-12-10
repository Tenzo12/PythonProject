import random
import sys

total_attempts = 5
color_list = [
    "red", "green", "blue","yellow", "orange","black"
]

def start_game(total_attempts):
    computer_choice = str(random.choice(color_list))

    user_choice = str(input())

    if user_choice == computer_choice:
        print("Congrats! you won.")
        total_attempts -= 1
        print("Attempts left:"+str(total_attempts))
        print("Enter your choice")
        print("1> Start again")
        print("2> Exit")
        choice = int(input())
        if choice == 1 :
                start_game(5)
        elif choice == 2:
                sys.exit()


    elif total_attempts > 1:
            print("Incorrect color, try again")
            total_attempts -= 1
            print("Attempts left:" + str(total_attempts))
            start_game(total_attempts)

    else:
            print("You lose, no attempts left")
            print("Enter your choice")
            print("1> Start again")
            print("2> Exit")
            choice = int(input())
            if choice == 1:
                start_game(5)
            elif choice == 2:
                sys.exit()




start_game(5)