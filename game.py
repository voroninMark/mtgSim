
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from player import Player
import random
from dataclasses import dataclass

@dataclass
class PlayContext:
    player: 'Player'
    game: 'Game'

class Game:
    def __init__(self):
        self.Players = []
        self.ActivePlayerIndex = 0
        self.TurnCount = 1
    @property
    def active_player(self) -> Player:
        return self.Players[self.ActivePlayerIndex]
    def NewGame(self):
        for player in self.Players:
            context = PlayContext(player=player,game=self)
            player.NewGame(context)
        random.shuffle(self.Players)
        self.ActivePlayerIndex = 0
    def NextTurn(self):
        if self.Players:
            player = self.active_player
            context = PlayContext(player=player,game=self)
            player.Draw(context,1)
            player.Board.Untap()
            self.ActivePlayerIndex = (self.ActivePlayerIndex + 1) % len(self.Players)
            if self.ActivePlayerIndex == 0:
                self.TurnCount += 1
    def PlayTurn(self):
        context = PlayContext(player=self.active_player,game=self)
        self.active_player.UpdateTags(context)
        self.active_player.PlayTurn(context)
        
    def AddPlayer(self, player : Player):
        self.Players.append(player)