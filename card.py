from behavior import UPDATE_TAG_BEHAVIORS, PLAY_BEHAVIORS
from strategy import *

class CardInitialiser:
    def __init__(self,tags,number):
        self.Tags = set(tags)
        self.Number = number
class Card:
    def __init__(self, name, tags):
        self.Name = name
        self.OriginalTags = set(tags)
        self.Tags = set(tags)
    def RemoveTag(self,tag):
        self.Tags.discard(tag)
    def AddTag(self,tag):
        self.Tags.add(tag)
    def Restore(self):
        self.Tags = set(self.OriginalTags)
    def has_all_tags(self, tags : list[str]) -> bool:
        return set(tags).issubset(self.Tags)
    def has_any_tag(self, tags : list[str]) -> bool:
        return any(tag in self.Tags for tag in tags)
    def has_tag(self,tag):
        return set([tag]).issubset(self.Tags)
    def get_all_matching_tags(self, tags : list[str]):
        """
        returns a list of tag that are in the both present in the list and in the card
        """
        return list(set(tags) & self.Tags)

    def Play(self, context: PlayContext):
        for tag in self.Tags:
            behavior = PLAY_BEHAVIORS.get(tag)
            if behavior:
                behavior(self, context)

    def UpdateTags(self, context: PlayContext):
        for tag in self.Tags:
            behavior = UPDATE_TAG_BEHAVIORS.get(tag)
            if behavior:
                behavior(self, context)