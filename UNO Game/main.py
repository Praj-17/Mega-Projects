from GameInit import GameInit, Player
import os
  
def generate_player_objects(Game, playerwise_cards):
  players = []
  for i in Game.get_player_names():
    players.append(Player(i, playerwise_cards[i]))
  print("Player objects created successfully")
  return players
  

    
    
if __name__ == "__main__":
  n_players = int(input("How many players? "))
  cards_per_player = int(input("How many cards per player? "))
  Game = GameInit(n_players, cards_per_player)
  if Game.validate_cards_per_player():
      print("Valid number of cards per player")
      playerwise_cards, remaining_deck = Game.distribute_cards()
      players = generate_player_objects(Game, playerwise_cards)
      
      
      

 
      
      
  
      
  
  
   
    

        
        
        