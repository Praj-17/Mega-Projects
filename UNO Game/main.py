
from deck_builder import Deck
from GameInit import GameInit, Player, player_names
  




    
    
    
if __name__ == "__main__":
 
  n_players = int(input("How many players? "))
  cards_per_player = int(input("How many cards per player? "))
  Game = GameInit(n_players, cards_per_player)
  if Game.validate_cards_per_player():
      print("Valid number of cards per player")
      playerwise_cards, remaining_deck = Game.distribute_cards()
      print("________Playerwise Cards_______")
      print(playerwise_cards)
      print("________Remaining Deck_______")
      print(len(remaining_deck))
      
      
  
      
  
  
   
    

        
        
        