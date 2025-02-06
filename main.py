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
        print("Starting Game...")
        return play
    elif play.lower() == "no":
        print("Ok then... :-( ")
        return play
    else:
        print("Please enter Yes or No.")

def choice1():
    print("You look down at the flight of steps you just climbed. 13 333 steps, if the legends are true.")
    time.sleep(2)
    print("You're pretty sure they are...")
    time.sleep(2)
    print("Looking up ahead you can see 2 paths. One lead to a giant castle. The other to a small cabin.")
    while True:
        firstchoice = input("Do you head toward the castle or the cabin?: ").strip().lower()
        if firstchoice == "castle":
            print("You turn left and head towards the castle looming in the distance.")
            return firstchoice
        elif firstchoice == "cabin":
            print("You turn right and head towards the cabin.")
            return firstchoice
        else:
            print("Please choose 'castle' or 'cabin'")

def choicecastle():
    print("As you arrive near the castle, you see merchants, soldiers, and others like you "
          "arriving for the choosing.")
    time.sleep(1)
    print("The choosing is an important day. The day where you decide your element:"
          "Water, Fire, Earth, or Electricity")
    time.sleep(2)

    choicemerchant = input("Would you like to stop at a merchant's stall before "
          "commencing the choosing? (Yes / No): ").strip().lower()
    if choicemerchant == "yes":
        print("Hmmm... There are so many stalls to choose from.")
        time.sleep(2)
        choicestall = input("Do you stop at the armorer or the healer?: ").strip().lower()
        if choicestall == "armorer":
            print("You visit the armorer")
        elif choicestall == "healer":
            print("You visit the healer")
        else:
            print("Please choose 'armorer' or 'healer'")
        return choicemerchant

    elif choicemerchant == "no":
        print("You ignore the market and enter the castle")
        return choicemerchant
    else:
        print("Please choose 'yes' or 'no'")

def choicecabin():
    print("As you walk toward the cabin, you cross merchants, soldiers, and others like you "
          "arriving for the choosing.")
    time.sleep(1)
    print("The choosing is an important day. The day where you decide your element:"
          "Water, Fire, Earth, or Electricity")
    time.sleep(1)
    print("All of a sudden, you hear a noise in the bushes...")
    time.sleep(2)
    print("'YIELD!' yells a ragged looking bandit, jumping out of the bushes.")

    choicebandit = input("Do you fight the bandit or run away (fight / run)?: ").strip().lower()
    if choicebandit == "fight":
        print("You defeat the bandit. ")
    elif choicebandit == "run":
        print("You run back to the castle")
    else:
        print("Please choose 'fight' or 'run.")



# Main game loop
def main():

    global firstchoice
    global play

    run = True

    while run:
        play = intro()
        if play == "no":
            break

        firstchoice = choice1()
        if firstchoice == "castle":
            choicecastle()
        elif firstchoice == "cabin":
            choicecabin()

        # replay = input("Do you want to play again? (Yes / No): ").strip().lower()
        # if replay != "yes":
        #     print("Thanks for playing!")
        #     break

# Checks if in "main" Module
if __name__ == "__main__":
    main()