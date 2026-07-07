print("Welcome to The Game to Find the Treasure!!!")
direction=input("You are at a crossroad Where you want to go Type left or Right\t").lower()

if direction == 'right':
    print("Congratulations! You have passed level 1.")
    choice = input("You have reached to lake. Do you like to wait for boat or will go by swim.Please type swim or wait\t").lower()
    if choice == 'wait':
        print("Congratulations! You have passed level 2.")
        door=input("Please select any one door . Type red, blue or yellow\t").lower()
        if door == 'yellow':
            print("Congratulations!!! You found the treasure.")
        elif door == 'red' or door == "blue" :
            print("Wrong Door ! Game Over!")
        else :
            print("Please type either red , yellow, or blue")

    elif choice =='swim':
        print("Hunted !Game Over!")
    else :
        print("Please type either swim or weight")

elif direction == 'left':
    print("wrong turn .Game Over!")
else:
    print("Please type either left or right")