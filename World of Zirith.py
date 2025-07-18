import os.path
import time as t
import os

os.system('cls')  # Clears the terminal

file_exists = os.path.isfile("savefile.txt")

Note = "Note: Good job you weren't stupid!"

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
        "1": FirstArea,
        "2": SecondArea,
        "3": ThirdArea,
        "4": FourthArea,
        "5": FifthArea,
        "6": SixtenthArea,
        "7": SeventhArea,
        "8": EighthArea,
        "9": NinthArea,
        "10": TenthArea,
        "11": EleventhArea,
        "12": TwelfthArea,
        "13": ThirteenthArea,
        "14": FourteenthArea,
        "15": FifteenthArea,
        "16": SixtenthArea,
        "17": SeventeenthArea,
        "18": EighteenthArea,
        "19": NineteenthArea,
        "20": TwentythArea,
        "45": FourtyFifthArea,
        "54": FiftyFourthArea,
        "55": Beginningarea,
        "65": SixtyFourthArea,
        "75": SeventyFourthArea,
        "75-1": PlainsVillage,
        "85": EightyFifthArea

    }

    func = area_map.get(area, lambda: print("Invalid or unknown area."))
    func()

inventory = ["shovel"]  # Global inventory list


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

def FirstArea():
    s = "1"
    save(s)
    os.system('cls')
    print("")
    choice = input("> ")
    if choice == "n":
        print("")
    else:
        print("Invalid input. Try again.")
        t.sleep(1)
        FirstArea()

def SecondArea():
    s = "2"
    save(s)
    os.system('cls')
    print("")
    choice = input("> ")
    if choice == "n":
        print("")
    else:
        print("Invalid input. Try again.")
        t.sleep(1)
        SecondArea()

def ThirdArea():
    s = "3"
    save(s)
    os.system('cls')
    print("")
    choice = input("> ")
    if choice == "n":
        print("")
    else:
        print("Invalid input. Try again.")
        t.sleep(1)
        ThirdArea()

def FourthArea():
    s = "4"
    save(s)
    os.system('cls')
    print("")
    choice = input("> ")
    if choice == "n":
        print("")
    else:
        print("Invalid input. Try again.")
        t.sleep(1)
        FourthArea()

def FifthArea():
    s = "5"
    save(s)
    os.system('cls')
    print("")
    choice = input("> ")
    if choice == "n":
        print("")
    else:
        print("Invalid input. Try again.")
        t.sleep(1)
        FifthArea()

def SixthArea():
    s = "6"
    save(s)
    os.system('cls')
    print("")
    choice = input("> ")
    if choice == "n":
        print("")
    else:
        print("Invalid input. Try again.")
        t.sleep(1)
        SixtenthArea()

def SeventhArea():
    s = "7"
    save(s)
    os.system('cls')
    print("")
    choice = input("> ")
    if choice == "n":
        print("")
    else:
        print("Invalid input. Try again.")
        t.sleep(1)
        SeventhArea()

def EighthArea():
    s = "8"
    save(s)
    os.system('cls')
    print("")
    choice = input("> ")
    if choice == "n":
        print("")
    else:
        print("")

def NinthArea():
    s = "9"
    save(s)
    os.system('cls')
    print("You walk around the open mountain top.\n" \
    "You feel your as high as dragons like your flying.")
    choice = input("> ").lower()
    if choice == "n" or choice == "north":
        pass #Area 12
    elif choice == "e" or choice == "east":
        EighthArea()
    else:
        print("Invalid input. Try again.")
        t.sleep(1)
        NinthArea()

def TenthArea():
    s = "10"
    save(s)
    os.system('cls')
    print("You made it to the top with your Pickaxe.")
    choice = input("> ").lower()
    if choice == "n" or choice == "north":
        pass #Area 11
    elif choice == "e" or choice == "east":
        NinthArea()
    else:
        print("Invalid input. Try again.")
        t.sleep(1)
        TenthArea()

def EleventhArea():
    s = "11"
    save(s)
    os.system('cls')
    print("There is a small mound of dirt like something is\n" \
    "buried in the ground. The ground looks very rocky and hard\n" \
    "to dig through with hands. You might want a shovel. do you have\n" \
    "one (Y/N)")
    choice = input("> ")
    if choice == "Y":
        if "shovel" not in inventory:
            print("No you don't go find one.")
        else:
            print("Great!!! Would you like to use the shovel? (Y/N)")
            choice = input("> ")
            if choice == "Y":
                print("You dig up a very old, and dirty chest.\n" \
                "a closer look shows that the chest is made of gold.")
            elif choice == "N":
                print("See you again soon.")

def TwelfthArea():
    s = "12"
    save(s)
    os.system('cls')
    print("")
    choice = input("> ")
    if choice == "n":
        print("")
    else:
        print("Invalid input. Try again.")
        t.sleep(1)
        TwelfthArea()

def ThirteenthArea():
    s = "13"
    save(s)
    os.system('cls')
    print("")
    choice = input("> ")
    if choice == "n":
        print("")
    else:
        print("Invalid input. Try again.")
        t.sleep(1)
        ThirteenthArea()

def FourteenthArea():
    s = "14"
    save(s)
    os.system('cls')
    print("")
    choice = input("> ")
    if choice == "n":
        print("")
    else:
        print("Invalid input. Try again.")
        t.sleep(1)
        FourteenthArea()

def FifteenthArea():
    s = "15"
    save(s)
    os.system('cls')
    print("")
    choice = input("> ")
    if choice == "n":
        print("")
    else:
        print("Invalid input. Try again.")
        t.sleep(1)
        FifteenthArea()

def SixtenthArea():
    s = "16"
    save(s)
    os.system('cls')
    print("")
    choice = input("> ")
    if choice == "n":
        print("")
    else:
        print("Invalid input. Try again.")
        t.sleep(1)
        SixtenthArea()

def SeventeenthArea():
    s = "17"
    save(s)
    os.system('cls')
    print("")
    choice = input("> ")
    if choice == "n":
        print("")
    else:
        print("Invalid input. Try again.")
        t.sleep(1)
        SeventhArea()

def EighteenthArea():
    s = "18"
    save(s)
    os.system('cls')
    print("")
    choice = input("> ")
    if choice == "n":
        print("")
    else:
        print("Invalid input. Try again.")
        t.sleep(1)
        EighteenthArea()

def NineteenthArea():
    s = "19"
    save(s)
    os.system('cls')
    print("")
    choice = input("> ")
    if choice == "n":
        print("")
    else:
        print("Invalid input. Try again.")
        t.sleep(1)
        NineteenthArea()

def TwentythArea():
    s = "20"
    save(s)
    os.system('cls')
    print("")
    choice = input("> ")
    if choice == "n":
        print("")
    else:
        print("Invalid input. Try again.")
        t.sleep(1)
        TwentythArea()

def TwentyFirstArea():
    s = "21"
    save(s)
    os.system('cls')
    print("")
    choice = input("> ")
    if choice == "n":
        print("")
    else:
        print("Invalid input. Try again.")
        t.sleep(1)
        TwentyFirstArea()

def TwentySecondArea():
    s = "22"
    save(s)
    os.system('cls')
    print("")
    choice = input("> ")
    if choice == "n":
        print("")
    else:
        print("Invalid input. Try again.")
        t.sleep(1)
        TwentySecondArea()

def FourtyFifthArea():
    s = "45"
    save(s)
    os.system('cls')
    print("You are facing towards an entrance to a cave")
    choice = input("> ").lower()
    if choice == "n" or choice == "north":
        Beginningarea()
    elif choice == "e" or choice == "east":
        pass #Area 46
    elif choice == "w" or choice == "west":
        pass #Area 44
    else:
        print("Invalid input. Try again.")
        t.sleep(1)
        FourtyFifthArea()

def FiftyFourthArea():
    s = "54"
    save(s)
    os.system('cls')
    if "Pickaxe" not in inventory:
        print("You Can not climb a cliff without tools.\n" \
        "Do you still want to try? (Y/N)")
        choice = input("> ")
        if choice == "Y":
            print("You tried to climb the cliff with nothing\n" \
            "but your hands. You slipped, and fell. The second\n" \
            "you hit the ground you went splat. Luckily no one\n" \
            "was around to see you being supid. I warned you not\n" \
            "to climb without tools.")
            if choice == "restart":
                Beginningarea()
        elif choice == "N":
            print("Good choice. As a reward for not being stupid!\n" \
            "I'll give you a Note.")
            add_to_inventory("rock")
            FourtyFifthArea()
    else:
        print("Invalid input. Try again.")
        t.sleep(1)
        FiftyFourthArea()

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
        FiftySixArea()
    elif choice == "s" or choice == "south":
        FourtyFifthArea()
    elif choice == "w" or choice == "west":
        FiftyFourthArea()
    else:
        print("Invalid input. Try again.")
        t.sleep(1)
        Beginningarea()

def FiftySixArea():
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
        FiftySixArea()
    else:
        print("Invalid input")
        t.sleep(1)
        FiftySixArea()

                

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
        pass #add inventory list here.
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
        EightyFifthArea()
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

def EightyFifthArea():
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
        EightyFifthArea()

def add_to_inventory(item):
    inventory.append(item)

def list_inventory():
    for i in inventory:
        print(i)
    SixtenthArea()
    
load()

