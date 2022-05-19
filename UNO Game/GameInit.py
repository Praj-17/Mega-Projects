class GameInit():
    def __init__(self, no_of_players, cards_per_player, n_decks=1) -> None:
        self.no_of_players = no_of_players
        self.cards_per_player = cards_per_player
        self.n_decks = n_decks
    def validate_cards_per_player(self):
        if self.cards_per_player < 1:
            raise ValueError("Cards per player must be greater than 0")
        if self.cards_per_player > self.n_decks*56/self.no_of_players:
            raise ValueError("Cards per player must be less than the number of cards in the deck")
        else:
            return True
    def distribute_cards(self):
        if self.validate_cards_per_player() == True:
          pass
class Player():
    pass
   