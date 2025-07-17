import os.path
import time 

t = time

file_exists = os.path.isfile("savefile.txt")

#loads the file
def load():
    if file_exists:
        file = open("savefile.txt","r")
        area = file.read()
        file.close()
    else:
        area = "0"
    
    areachooser(area)

#saves the file
def save(s):
    file = open("savefile.txt","w")
    file.write(s)
    file.close()

def areachooser(area):
    area_map = {
        "0": start,
        "54": Beginningarea,
        "64": SixtyFourthArea,
        "74": SeventyFourthArea,
        "84": EightyFourthArea

    }

    func = area_map.get(area, lambda: print("Invalid or unknown area."))
    func()


# Dialog before game starts.
def start():
    s = "0"
    save(s)

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
    print("Do you wish to play? (Y/N)")

    choice = input(">")
    if (choice == "Y"):
        Beginningarea()
    elif (choice == "N"):
        print("Too bad. I'll see you again soon.")
    else:
        print("Invalid input")
        t.sleep(1)
        start()

def Beginningarea():
    s = "54"
    save(s)
    print("You are standing in a field of grass")
    choice = input("> ").lower()
    if choice == "n" or choice == "north":
        Beginningarea()
    else:
        print("Invalid input")
        t.sleep(1)
        Beginningarea()

def SixtyFourthArea():
    s = "64"
    save(s)
    print("you are in a field of grass, in the distance is a village.")
    choice = input("> ")
    if choice == "n" or "north":
        SixtyFourthArea()
    else:
        print("Invalid input")
        t.sleep(1)
        SixtyFourthArea()

def SeventyFourthArea():
    s = "74"
    save(s)
    print("you are outside a village in a massive grassy plain.")
    choice = input("> ")
    if (choice == "n" or "north"):
        SeventyFourthArea()
    else:
        print("Invalid input")
        t.sleep(1)
        SeventyFourthArea()

def EightyFourthArea():
    s = "84"
    save(s)
    print("")
    choice = input("> ")
    if (choice == "n" or "north"):
        pass
    else:
        print("Invalid input")
        t.sleep(1)
        EightyFourthArea()

load()

