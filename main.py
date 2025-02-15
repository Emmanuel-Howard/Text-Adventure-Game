# A text adventure game using conditional statements
# Adding storyline + potential to add stats
# Will also add pygame for sound effects
# Need to continue working healer/armorer

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
    print("You look down at the flight of steps you just climbed. 13 333 steps, ")
    print("if the legends are true.")
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
    print("As you arrive near the castle, you see merchants, soldiers, and ")
    print("others like you arriving for the choosing.")
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

    banditalive = True

    print("As you walk toward the cabin, you cross merchants, soldiers ")
    print("and others like you arriving for the choosing.")
    time.sleep(2)
    print("The choosing is an important day. The day where you decide your element: ")
    print("Water, Fire, Earth, or Electricity")
    time.sleep(3)
    print("All of a sudden, you hear a noise in the bushes...")
    time.sleep(3)
    print("'YIELD!' yells a ragged looking bandit, jumping out of the bushes.")
    time.sleep(1)

    choicebandit = input("Do you fight the bandit or run away (fight / run)?: ").strip().lower()
    if choicebandit == "fight":
        choiceweapon = input("Do you use your sword or your bow?: ").strip().lower()
        if choiceweapon == "sword":
            print("You draw your sword and circle the bandit.")
            time.sleep(2)
            print("HE LUNGES")
            time.sleep(1)
            choiceattack = input("Do you parry or attack?: ").strip().lower()
            if choiceattack == "parry":
                print("You parry and lunge back at the bandit, striking him dead center.")
                time.sleep(2)
                print("You vanquish the bandit and finally make it to the cabin entrance.")
            elif choiceattack == "attack":
                print("You sidestep and lunge back at the bandit, striking him dead center.")
                time.sleep(2)
                print("You vanquish the bandit and finally make it to the cabin entrance.")
            else:
               print("Please enter 'parry' or 'attack'")

        elif choiceweapon == "bow":
            print("You sling your bow off your shoulder and nock an arrow.")
            time.sleep(2)
            print("Right before you shoot, the bandit throws his spear right at you.")
            time.sleep(1)
            choiceattack = input("Do you dodge or shoot?: ").strip().lower()
            if choiceattack == "dodge":
                print("You dodge his spear and shoot. The spear barely misses.")
                time.sleep(2)
                print("Your arrow hits him in the shoulder. He yells and runs away...")
                time.sleep(2)
                print("You vanquish the bandit and finally make it to the cabin entrance.")

            elif choiceattack == "shoot":
                print("You shoot your arrow and his spear luckily misses you by an inch.")
                time.sleep(2)
                print("Your arrow hits him in the chest. He falls without a sound...")
                banditalive == False
                time.sleep(2)
                print("You vanquish the bandit and finally make it to the cabin entrance.")
            else:
                print("Please enter 'dodge' or 'shoot'")
        else:
            print("Please enter 'sword' or 'bow'")
    elif choicebandit == "run":
        print("You run back to the castle")
    else:
        print("Please choose 'fight' or 'run.")

def castle():
    print("Arrives at castle")

def cabin():
    print("Arrives at cabin")

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