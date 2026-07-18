import random


rsp = ['rock','scissor','paper']
user_choice = int(input("Press 0 for Rock,1 for scissor 2 for paper\t"))
if user_choice >2 or user_choice < 0 :
    print("You enter invalid Choice. you loss the game!")
else:
    print(f"you have Selected {rsp[user_choice]}")
    computer_choice = random.randint(0,2)
    print(f"Computer has selected {rsp[computer_choice]}")

    if user_choice == computer_choice :
        print("Game Draw")
    elif user_choice == 0 and computer_choice ==1 :
        print("Computer win")
    elif user_choice == 0 and computer_choice ==2 :
        print("You win")
    elif user_choice == 1 and computer_choice == 0:
        print("You win")
    elif user_choice == 1 and computer_choice == 2:
        print("Computer win")
    elif user_choice == 2 and computer_choice ==0 :
        print("Computer win")
    elif user_choice == 2 and computer_choice ==1 :
        print("You win")
    else:
        print("decision Pending")