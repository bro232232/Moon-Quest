def start_game():
    print("Welcome to Moon Quest!")
    print("You are an explorer in the country of Moon, a land shaped like a crescent moon.")
    print("Your mission is to find the hidden treasure of Lunar Bay.")
    print("")

    choice = input("You begin your journey in Crescent City. Where would you like to go?\n1. Selene Springs\n2. Crater Ridge\n3. Starlight Shores\nEnter 1, 2, or 3: ")

    if choice == '1':
        selene_springs()
    elif choice == '2':
        crater_ridge()
    elif choice == '3':
        starlight_shores()
    else:
        print("Invalid choice. Please try again.")
        start_game()

def selene_springs():
    print("\nYou arrive at Selene Springs, known for its healing waters.")
    choice = input("What would you like to do?\nA. Drink from the springs\nB. Explore the surrounding forest\nEnter A or B: ")

    if choice.lower() == 'a':
        print("You drink from the springs and gain health.")
        lunar_bay()
    elif choice.lower() == 'b':
        print("You explore the forest and find a map.")
        lunar_bay()
    else:
        print("Invalid choice. Please try again.")
        selene_springs()

def crater_ridge():
    print("\nYou arrive at Crater Ridge, a treacherous path filled with obstacles.")
    choice = input("What would you like to do?\nA. Climb the ridge\nB. Go around the ridge\nEnter A or B: ")

    if choice.lower() == 'a':
        print("You climb the ridge, risking injury but finding a shortcut.")
        lunar_bay()
    elif choice.lower() == 'b':
        print("You go around the ridge, taking a safer but longer route.")
        lunar_bay()
    else:
        print("Invalid choice. Please try again.")
        crater_ridge()

def starlight_shores():
    print("\nYou arrive at Starlight Shores, a serene beach with hidden secrets.")
    choice = input("What would you like to do?\nA. Search the beach\nB. Talk to a local fisherman\nEnter A or B: ")

    if choice.lower() == 'a':
        print("You search the beach and find a clue.")
        lunar_bay()
    elif choice.lower() == 'b':
        print("You talk to a local fisherman and gain valuable information.")
        lunar_bay()
    else:
        print("Invalid choice. Please try again.")
        starlight_shores()

def lunar_bay():
    print("\nYou finally reach Lunar Bay. To find the treasure, you must solve a riddle.")
    answer = input("I shine bright in the night, but disappear at dawn. What am I? ")

    if answer.lower() == 'the moon' or answer.lower() == 'moon':
        print("Congratulations! You found the hidden treasure of Lunar Bay and became a hero of Moon!")
    else:
        print("Incorrect. The treasure remains hidden. Better luck next time!")

start_game()
