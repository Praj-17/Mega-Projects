import itertools
import random


class card:
    def __init__(self, front_color, back_color, front_type, back_type):
        self.front_color = front_color
        self.back_color = back_color
        self.front_type = front_type
        self.back_type = back_type



def Building_Fresh_deck():
    
  
  
    fronts_general = ["1","2","3","4","5","6","7","8","9","REVERSE", "SKIPONE", "1+", "FLIP"]
    fronts_black = ["WILD", "2+",]
    backs_general =  ["1","2","3","4","5","6","7","8","9","REVERSE", "SKIPALL",  "3+", "FLIP"]
    backs_black = ["WILD", "STACKUP",]
    front_colors= ["Red", "Green", "Yellow", "Blue"]
    back_colors = ["Pink", "Purple", "Orange", "Aqua"]
    front_sides = []
    back_sides = []


    # Build the front and back sides of the cards
    for r in itertools.product(fronts_general,front_colors ):
        front_sides.append(f"{r[0]}_{r[1]}")
    for r in itertools.product(fronts_black,["Black"]):
        front_sides.append(f"{r[0]}_{r[1]}")
        front_sides.append(f"{r[0]}_{r[1]}")
        
    for r in itertools.product(backs_general,back_colors ):
        back_sides.append(f"{r[0]}_{r[1]}")
    for r in itertools.product(backs_black,["Black"]):
        back_sides.append(f"{r[0]}_{r[1]}")
        back_sides.append(f"{r[0]}_{r[1]}")

    #Now we will remove power cards from the deck so as no card gets a power on either side.
    front_sides_numbers  = front_sides[:36]
    front_sides_power    = front_sides[36:]
    back_sides_numbers   = back_sides[:36]
    back_sides_power     = back_sides[36:]


    # As of now front and back sides have been built
    # Now, we need to integrate them into the cards


    random.shuffle(front_sides_numbers)
    random.shuffle(front_sides_power)
    random.shuffle(back_sides_numbers)
    random.shuffle(back_sides_power)



    front_sides_numbers_1 = front_sides_numbers[0:20]
    front_sides_numbers_2 = front_sides_numbers[20:]

    back_sides_numbers_1 = back_sides_numbers[0:20]
    back_sides_numbers_2 = back_sides_numbers[20:]






    deck_1 = list(zip(front_sides_numbers_1, back_sides_power))
    deck_2 = list(zip(front_sides_power, back_sides_numbers_1))
    deck_3 = list(zip(front_sides_numbers_2, back_sides_numbers_2))

    #appending all three sub-decks together
    deck = deck_1 + deck_2 + deck_3
    # for i in range(n-1):
    #     deck += deck
    return deck
    
def Build_Deck(n=1, same_deck=True):
    """
    This function is basically a wrapper for the Building_Fresh_deck function. It has 2 paremeters: that help it to build a deck of n number of decks. and a boolean that tells it to build the same deck or not.
    n : number of decks to build, Must be integer
    same_deck : boolean, if True, it will build the same deck, if False, it will build a different decks.
    """
    if same_deck == True:
        Deck = Building_Fresh_deck()
        for _ in range(n-1):
            Deck += Deck
        return Deck
    else:
        if n==1:
            return Building_Fresh_deck()
        else:
            Decks = []
            for _ in range(n):
                Decks.append(Building_Fresh_deck())
            return Decks
    
    
    
if __name__ == "__main__":
    print(len(Build_Deck(2, False)))
    

        
        
        