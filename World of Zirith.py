import os.path
import time as t
import os

os.system('cls')  # Clears the terminal

file_exists = os.path.isfile("savefile.txt")


# Ask for save name at the start
def get_save_name():
    print("Enter your save name (or slot number):")
    save_name = input("> ").strip()
    if not save_name:
        save_name = "default"
    return f"savefile_{save_name}.txt"

SAVE_FILE = get_save_name()

def load():
    if os.path.isfile(SAVE_FILE):
        with open(SAVE_FILE, "r") as file:
            area = file.read()
    else:
        area = "0"
    areachooser(area)

def save(s):
    with open(SAVE_FILE, "w") as file:
        file.write(s)

def areachooser(area):
    area_map = {
        "0": start,
        "55": Beginningarea,
        "65": SixtyFourthArea,
        "75": SeventyFourthArea,
        "75-1": PlainsVillage,
        "85": EightyFourthArea

    }

    func = area_map.get(area, lambda: print("Invalid or unknown area."))
    func()

inventory = []  # Global inventory list


# Dialog before game starts.
def start():
    s = "0"
    save(s)
    os.system('cls')
    print("Welcome traveler.")
    print("I see you have found your way into")
    print("the world I call home.")
    print("While your here I suppose I should introduce")
    print("myself.")
    print("I am GOD. Everything you experience was made")
    print("by me. Every word you see, and")
    print("every word you write go together to make a naritive")
    print("for you the, traveler of my world.")
    print("pls enjoy my world, and all it has to offer.")
    print("Shall we play a game? (Y/N)")

    choice = input("> ")
    if (choice == "Y"):
        Beginningarea()
    elif (choice == "N"):
        print("Too bad. I'll see you again soon.")
    else:
        print("Invalid input. Try again.")
        t.sleep(1)
        os.system('cls')
        start()


def Beginningarea():
    s = "55"
    save(s)
    os.system('cls')
    print("You are standing in a field of grass.\n" \
    "to move around type 'n' 's' 'e' or 'w'.")
    choice = input("> ").lower()
    if choice == "n" or choice == "north":
        SixtyFourthArea()
    elif choice == "e" or choice == "east":
        FiftySix()

    else:
        print("Invalid input. Try again.")
        t.sleep(1)
        Beginningarea()

def FiftySix():
    s = "56"
    os.system('cls')
    print("You are standing infront of a forest. The forest is filled\n" \
          "with creature that will tear you apart if you encounter one.")
    choice = input("> ")
    if choice == "n" or choice == "north":
        print("You have entered the forest, You hear the creatures getting closer\n" \
              "and closer to you. you still have time to leave. Do you want to leave (Y/N)")
        choice = input("> ")
        if choice == "N":
            print("A giant scorpion about 25ft long and 10ft wide grabs your leg,\n" \
                  "lifts you into the air and tears you in two with it's pincers.\n" \
                  "you died type 'start' to try again.")
            choice = input("> ")
            if choice == "start":
                start()
    elif choice == "Y":
        FiftySix()
    else:
        print("Invalid input")
        t.sleep(1)
        FiftySix()

                

def SixtyFourthArea():
    s = "65"
    save(s)
    os.system('cls')
    print("you are in a field of grass, in the distance is a village.\n" \
          "on the ground is a rock. would you like to pick it up? (Y/N)")
    choice = input("> ")
    if (choice == "n" or choice == "north"):
        SeventyFourthArea()
    elif (choice == "Y"):
        add_to_inventory("rock")
        print("You picked up the rock.")
        t.sleep(1)
        SixtyFourthArea()
    elif (choice == "list"):
        list_inventory()
        choice = input("> ")
        
    else:
        print("Invalid input try again.")
        t.sleep(1)
        SixtyFourthArea()

def SeventyFourthArea():
    s = "75"
    save(s)
    os.system('cls')
    print("you are outside the village in a massive grassy plain.\n" \
    "would you like to enter the villae? (Y/N)")
    choice = input("> ")
    if (choice == "Y"):
        PlainsVillage()
    if (choice == "n" or "north"):
        EightyFourthArea()
    else:
        print("Invalid input try again.")
        t.sleep(1)
        SeventyFourthArea()

def PlainsVillage():
    s = "75-1"
    save(s)
    os.system('cls')
    print("You entered the village. Around you are people walking about,\n" \
    "and houses surrounding you. Would you like to talk to someone? (Y/N)")
    choice = input("> ")
    if (choice == "Y"):
        pass
    else:
        print("Invalid input try again.")
        t.sleep(1)
        PlainsVillage()

def EightyFourthArea():
    s = "85"
    save(s)
    os.system('cls')
    print("")
    choice = input("> ")
    if (choice == "n" or "north"):
        print("There is a river infront of you. The river is full of piranhas.")
        t.sleep(1)
    else:
        print("Invalid input try again.")
        t.sleep(1)
        EightyFourthArea()

def add_to_inventory(item):
    inventory.append(item)

def list_inventory():
    print(inventory)

load()

