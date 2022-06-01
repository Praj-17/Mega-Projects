import itertools
import random
from card import Card

    

class Deck:
    def __init__(self,n=1,same_Deck= True) -> None:
        self.n = n
        self.same_Deck = same_Deck
        
    def Building_Fresh_deck(self):
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
        
    def Build_Deck(self):
        """
        This function is basically a wrapper for the Building_Fresh_deck function. It has 2 paremeters: that help it to build a deck of n number of decks. and a boolean that tells it to build the same deck or not.
        n : number of decks to build, Must be integer
        same_deck : boolean, if True, it will build the same deck, if False, it will build a different decks.
        """
        if self.same_Deck == True:
            Deck = self.Building_Fresh_deck()
            if self.n > 1:
                for _ in range(self.n-1):
                    Deck += Deck
            cards = []
            for sides in (Deck):
                card = Card(sides[0],sides[1]) 
                card.fit()
                cards.append(card)
            return cards
            
        else:
            if self.n==1:
                return self.Building_Fresh_deck()
            else:
                Decks = []
                for _ in range(self.n):
                    Decks.append(self.Building_Fresh_deck())
                cards = []
                for sides in (self.Build_Deck()):
                    card = Card('card')
                    card.fit()
                    card.front, card.back = sides[0], sides[1]
                    cards.append(card)
                return cards
                
    def Get_Deck(self):
        """
        This function is a wrapper for the Build_Deck function. It has 2 paremeters: that help it to build a deck of n number of decks. and a boolean that tells it to build the same deck or not.
        n : number of decks to build, Must be integer
        same_deck : boolean, if True, it will build the same deck, if False, it will build a different decks.
        """
        cards = []
        deck = self.Build_Deck()
        for card in deck:
                card.fit()
                cards.append(card)
        self.deck = cards
        return self.deck
   
deck_object = Deck()
deck = deck_object.Get_Deck()
def GetCard(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card, deck

        

