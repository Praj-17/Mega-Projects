from deck_builder import GetCard, Deck

def player_names(no_of_palyers):
        player_name_list = []
        for i in range(no_of_palyers):
            player_name = input("Enter player name: ")
            player_name_list.append(player_name)
        player_name_list = player_name_list
        return player_name_list

class GameInit():
    def get_player_names(self):
        self.player_names = player_names(self.no_of_players)
        return self.player_names
    def __init__(self, no_of_players, cards_per_player, n_decks=1) -> None:
        self.no_of_players = no_of_players
        self.cards_per_player = cards_per_player
        self.n_decks = n_decks
        self.get_player_names()
    def validate_cards_per_player(self):
        if type(self.cards_per_player) == int:
            if self.cards_per_player < 1:
                raise ValueError("Cards per player must be greater than 0")
            if self.cards_per_player > self.n_decks*56/self.no_of_players:
                raise ValueError("Cards per player must be less than the number of cards in the deck")
            else:
                return True
        else:
            raise TypeError("Cards per player must be an integer")
    
    def get_player_names(self):
        self.player_names = player_names(self.no_of_players)
        return self.player_names

    def distribute_cards(self , deck=Deck().Get_Deck()):
        print("Distributing  Cards now, please wait...")
        if self.validate_cards_per_player() == True:
            player_cards = {}
            for i in range(self.no_of_players):
                player_cards[f'{self.player_names[i]}'] = []
                for j in range(self.cards_per_player):
                    card, deck = GetCard(deck)
                    Deck = deck
                    player_cards[f'{self.player_names[i]}'].append(card)
                self.player_cards = player_cards
                self.remaining_deck = deck

            print("Cards Distributed Successfully")
            return self.player_cards, self.remaining_deck
        
        
            

    
class Player():
    def __init__(self, name, cards_in_hand) -> None:
        self.name = name
        self.cards_in_hand = cards_in_hand

    
   