from deck import *
from strategy import *

class Player:
    def __init__(self, name, deck : Deck,strategy : Strategy = None):
        self.Name = name
        self.OriginalDeck = deck
        self.SetStrategy(strategy)
        self.Deck = self.OriginalDeck
        self.MulliganCount = 0
        self.Hand = CardCollection()
        self.Board = Board()
        self.Graveyard = CardCollection()

    def SetStrategy(self, strategy : Strategy):
        if strategy is None:
            self.Strategy = Strategy()
        else:
            self.Strategy = strategy
    def NewGame(self, context : PlayContext):
        self.Deck = self.OriginalDeck
        self.Hand = CardCollection()
        self.Board = Board()
        self.Graveyard = CardCollection()
        self.Mulligan(context,0)
        self.MulliganCount = 0
        while not(self.Strategy.MulliganCheck(context)) and self.MulliganCount < 7:
            self.Mulligan(context,self.MulliganCount)

    def Draw(self, context : PlayContext, number):
        if self.Deck.Cards:
            self.Hand.TakeCardsFromTop(number,self.Deck)
    def Mulligan(self, context : PlayContext, number):
        self.Deck.TakeCardsFromTop(-1,self.Hand)
        self.Deck.Shuffle()
        self.Draw(context,7-number)
        self.MulliganCount = self.MulliganCount+1
    
    def PlayTurn(self,context : PlayContext):
        self.LandForTurn(context)

    def PlayCard(self,context : PlayContext, source : CardCollection,card : Card):
        self.Board.TakeCard(source,card)
        card.Play(context)
        
    def LandForTurn(self,context : PlayContext):
        self.PlayCard(context,context.player.Hand,self.Strategy.LandForTurn(context))
    
    def UpdateTags(self, context : PlayContext):
        self.Hand.UpdateTags(context)
        self.Board.UpdateTags(context)