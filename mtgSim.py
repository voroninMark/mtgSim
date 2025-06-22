from card import Card,CardInitialiser
from deck import Deck
from strategy import RubyStrategy
from player import Player
from game import *

#TODO
#fetch, cinderglade, thornspire,surveil
cardInitialisers = (
    CardInitialiser(["green","forest","basic","land"],10),
    CardInitialiser(["red","mountain","Basic","land"],9),
    CardInitialiser(["colorless","land"],1),
    CardInitialiser(["colorless","land","tapped"],1),
    CardInitialiser(["fetch","mountain","land"],1),
    CardInitialiser(["red","green","mountain","forest","cinderglade","land"],1),
    CardInitialiser(["red","green","mountain","forest","tapped","surveil","land"],1),
    CardInitialiser(["red","green","coloredFilter","land"],1),
    CardInitialiser(["red","green","tapped","bounce","land","deaddraw"],1),
    CardInitialiser(["green","tapped","land"],1),
    CardInitialiser(["red","green","colorlessFilter","land"],1),
    CardInitialiser(["green","tapped","land"],1),
    CardInitialiser(["colorless","land","tapped"],1),
    CardInitialiser(["colorless","land","tapped"],1),
    CardInitialiser(["colorless","land"],1),
    CardInitialiser(["red","green","land"],1),    
    CardInitialiser(["red","green","mountain","forest","land"],1),
    CardInitialiser(["colorless","land","deaddraw"],1),
    CardInitialiser(["colorless","land"],1),    
    CardInitialiser(["red","thornspire","land"],1),    
    CardInitialiser(["colorless","land"],1),    
    CardInitialiser(["colorless","land"],1),    
    CardInitialiser(["fetch","mountain","forest","land"],1),
    CardInitialiser(["green","land"],1), 
    CardInitialiser(["red","mdfc","land"],1),  
    CardInitialiser(["spell","4manaramp"],16),  
    CardInitialiser(["other"],41)
)

myDeck = Deck(cardInitialisers)
player = Player("player1",myDeck)
player.SetStrategy(RubyStrategy())
game = Game()
game.AddPlayer(player)
game.NewGame()
player.Hand.Cards.append(Card("commercial district",["red","green","mountain","forest","tapped","surveil","land"]))
#player.Deck.Cards.append(Card("test",["other"]))
game.PlayTurn()
game.NextTurn()
game.PlayTurn()
print("e")

