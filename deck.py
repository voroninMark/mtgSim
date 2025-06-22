from __future__ import annotations  
from card import Card,CardInitialiser
from game import PlayContext
import random

class CardCollection:
    def __init__(self):
        self.Cards = []
    def Tutor(self, tags,antitags=None,remove=False,name=None) -> Card:
        """
        Search for a card by name and/or tags.
        Returns the first matching card.
        If remove=True, also removes the card from the collection.
        """
        for card in self.Cards:
            name_match = (name is None or card.Name == name)
            tags_match = (tags is None or set(tags).issubset(card.Tags))
            antitags_match = (antitags is None or not(set(antitags).issubset(card.Tags)))
            if name_match and tags_match and antitags_match:
                if remove:
                    self.Cards.remove(card)
                return card
        return None  # Nothing found
    def TutorAll(self, tags,antitags=None,remove=False,name=None) -> CardCollection:
        """
        Search for a card by tags.
        Returns all matching card.
        If remove=True, also removes the cards from the collection.
        """
        result = CardCollection()
        for card in self.Cards:
            name_match = (name is None or card.Name == name)
            tags_match = (tags is None or set(tags).issubset(card.Tags))
            antitags_match = (antitags is None or not(set(antitags).issubset(card.Tags)))
            if name_match and tags_match and antitags_match:
                result.add_card(card)
                if remove:
                    self.Cards.remove(card)
        return result
    def TutorAny(self, tags, antitags=None,remove=False,name=None) -> Card:
        """
        Search for a card by tags.
        returns the first card matching at least on of the tags
        If remove=True, also removes the card from the collection.
        """
        for card in self.Cards:
            tags_match = any(tag in card.Tags for tag in tags)
            antitags_match = (antitags is None or not(set(antitags).issubset(card.Tags)))
            if tags_match and antitags_match:                
                if remove:
                    self.Cards.remove(card)
                return card
        return None
    def TakeCard(self, source : 'CardCollection' , card : Card):
        """
        Take a card from the source collection and add it to self.
        Returns True if successful, False otherwise.
        """
        if card in source.Cards:
            source.Cards.remove(card)
            self.Cards.append(card)
            return True
        else:
            return False
    def TakeCardsFromTop(self,number,source):
        numberToTake = number
        if(number >= len(source.Cards) or number == -1):
            numberToTake = len(source.Cards)
        for _ in range(numberToTake):
            card = source.Cards.pop(0)
            card.Restore()
            self.Cards.append(card)
    def Shuffle(self):
        random.shuffle(self.Cards)

    def UpdateTags(self,context : PlayContext):
        for card in self.Cards:
            card.UpdateTags(context)
    def add_card(self,card : Card):
        self.Cards.append(card)

class Board(CardCollection):
    def __init__(self):
        super().__init__()
    def Untap(self):
        for card in self.Cards:
            card.RemoveTag("tapped")

class Deck(CardCollection):
    def __init__(self, cardInitialisers):
        super().__init__() 
        self.Refill(cardInitialisers)
    
    def Refill(self, cardInitialisers):
        self.Cards = []
        for cardInitialiser in cardInitialisers:
            for _ in range(cardInitialiser.Number):
                self.Cards.append(Card("name",cardInitialiser.Tags))