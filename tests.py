from __future__ import annotations  
from card import Card,CardInitialiser
from deck import Deck,CardCollection,Board
from strategy import RubyStrategy
from player import Player
from game import *

cardInitialisers = (
    CardInitialiser(["green","forest","basic","land"],10),
    CardInitialiser(["red","mountain","Basic","land"],9),
    CardInitialiser(["colorless","land"],1),
    CardInitialiser(["colorless","land","tapped"],1),
    CardInitialiser(["fetch_land","mountain","land"],1),
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
    CardInitialiser(["fetch_land","mountain","forest","land"],1),
    CardInitialiser(["green","land"],1), 
    CardInitialiser(["red","mdfc","land"],1),  
    CardInitialiser(["spell","4manaramp"],16),  
    CardInitialiser(["other"],41)
)



def TestFetchLand() -> bool:
    cardInitialisersFetch = (
        CardInitialiser(["red","green","mountain","forest","tapped","surveil","land"],1),
        CardInitialiser(["other"],1),
    )

    myDeck = Deck(cardInitialisersFetch)
    player = Player("player1",myDeck)
    player.SetStrategy(RubyStrategy())
    game = Game()
    game.AddPlayer(player)
    game.NewGame()
    game.active_player.Deck.TakeCardsFromTop(-1,game.active_player.Hand)
    game.active_player.Hand.add_card(Card("fetch_gruul",["fetch_land","mountain","forest","land"]))
    game.PlayTurn()
    landCardTutored = game.active_player.Board.TutorAny(["mountain","forest","land"],["fetch_land"])
    if(landCardTutored):
        print("land tutored : "+str(landCardTutored.Tags))
        return True
    print("land not found")
    return False

TestFetchLand()