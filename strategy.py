
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from card import Card
from game import PlayContext
class Strategy:
    def LandForTurn(self, context: PlayContext):
        return context.player.Hand.Tutor(["land"])

    def MulliganCheck(self, context: PlayContext) -> bool:
        cards = context.player.Hand.TutorAll(["land"]).Cards
        return len(cards) >= 3
    def Surveil(self,context : PlayContext):
        if(set(["other"]).issubset(context.player.Deck.Cards[0].Tags) or set(["deaddraw"]).issubset(context.player.Deck.Cards[0].Tags)):
            context.player.Graveyard.TakeCardsFromTop(1,context.player.Deck)
    def FetchLand(self, context : PlayContext, card : Card):
        if(card.has_tag("fetch_land")):
            basicLandTags = card.get_all_matching_tags(["forest","mountain","island","plains","swamp"])
            fetchedCard = context.player.Deck.TutorAny(basicLandTags,["fetch_land"])
            context.player.Graveyard.TakeCard(context.player.Board,card)
            context.player.PlayCard(context,context.player.Deck,fetchedCard)

class RubyStrategy(Strategy):
    def LandForTurn(self, context: PlayContext):
        game = context.game
        hand = context.player.Hand
        board = context.player.Board
        if(game.TurnCount == 1):
            card = hand.Tutor(["land","surveil"],["deaddraw"])
            if card:
                return card
            card = hand.Tutor(["land","tapped","red"],["deaddraw"])
            if card:
                return card
            card = hand.Tutor(["land","tapped","green"],["deaddraw"])
            if card:
                return card
            card = hand.Tutor(["land","red","green"],["deaddraw"])
            if card:
                return card
            card = hand.Tutor(["land","green"],["deaddraw"])
            if card:
                return card
            card = hand.Tutor(["land","red"],["deaddraw"])
            if card:
                return card
            card = hand.Tutor(["land"],["deaddraw"])
            if card:
                return card
            card = hand.Tutor(["land"])
            if card:
                return card
        else:
           return super().LandForTurn(context)
            

    def MulliganCheck(self, context: PlayContext) -> bool:
        return super().MulliganCheck(context)