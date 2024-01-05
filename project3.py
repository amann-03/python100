print("Welcome to Treasure Island.")
print("\nYour mission is to find the treasure.")

choice1 = input('You\'re at a crossroad, Where do you want to go? Type "left" or "right".\nleft').lower()

if choice1=="left":
    #Continue to Game
    choice2 = input("You've come to lake.There is an island in the middle of the lake. Type'wait' to wait for boat or 'swim' to swim across.\n").lower()
    if choice2=="wait":
        #Game will over
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors.1 red, 1 blue and 1 yellow. Which colour do you choose? \n").lower()
        if choice3=="red":
            print("It's a room full of fire. Game Over.\n")
        elif choice3=="yellow":
            print("You found the treasure. You win.\n")
        elif choice3=="blue":
            print("You entered a room of beasts. Game Over.\n")
        else:
            print("You chose a door that doesn't exist. Game Over.\n")           
    else:
        print("You got attacked by angry tout. Game Over.\n")
else:
    print("You fell into a hole. Game Over.\n")

