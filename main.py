# A text adventure game using conditional statements
# Adding storyline + potential to add stats
# Will also add pygame for sound effects

# Importing necessary modules
import time

# Function defining intro to game
def intro():
    print("Welcome to Storm's Adventure!")
    play = str(input("Would you like to play (Yes / No)?: "))
    if play.lower() == "yes":
        run = True
        print("Starting Game...")
    elif play.lower() == "no":
        print("Ok then... :-( ")
    else:
        print("Please enter Yes or No.")

def choice1():
    print("You look down at the flight of steps you just climbed. 13 333 steps, if the legends are true.")
    time.sleep(2)
    print("You're pretty sure they are...")
    time.sleep(2)
    print("Looking up ahead you can see 2 paths. One lead to a giant castle. The other to a small cabin.")
    while True:
        firstchoice = input("Do you head toward the castle or the hut?: ").lower()
        if firstchoice == "castle":
            print("You turn left and head towards the castle looming in the distance.")
            break
        elif firstchoice == "hut":
            print("You turn right and head towards the hut.")
            break
        else:
            print("Please choose 'castle' or 'cabin'")

def choicecastle():
    print("You see the castle")

def choicecabin():
    print("You see the cabin")


# Main game loop
def main():

    global firstchoice

    run = True

    while run:
        intro()
        choice1()
        if firstchoice == "castle":
            choicecastle()
        elif firstchoice == "cabin":
            choicecabin()

# Checks if in "main" Module
if __name__ == "__main__":
    main()