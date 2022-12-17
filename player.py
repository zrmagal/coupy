from typing import Type, List
from enum import Enum

from coupy import deck
from coupy import msgdevice
from coupy import card
from coupy import moves

class Player(deck.Deck):
    """
    Class of player instance.
    """
    ###########################################################################
    def __init__(self, name: str, io: msgdevice.MsgDev) -> None:
        """
        Constructor of player object
        :name: string that denotes player's name
        :io: IO instance to communicate with player
        """
        self._coins: int = 0
        self._io : msgdevice.MsgDev = io
        self.name : str = name
        deck.Deck.__init__(self, name+"deck")
        
    ###########################################################################
    @property
    def coins(self) -> int:
        return self._coins

    ###########################################################################            
    def collect(self, coins: int) -> int:
        """
        Method to remove coins from player
        :coins: The number of coins to be removed.
        :return: The number of coins removed
        """
        if coins > self._coins:
            coins = self._coins
            self._coins = 0
        else:
            self._coins -= coins
        
        return coins

    ###########################################################################
    def add_coins(self, coins: int) -> None:
        """
        Method to give coins to player
        :coins: the number of coins given to player
        """
        if (coins > 0):
            self._coins += coins

    ###########################################################################
    def sel_target(self, targets: List["Player"]) -> str:
        """
        Function to ask the player for selection of target opponent
        :targets: List of opponent players
        """
        if not targets:
            return ""
        
        repply = ""
        req = f"{self.name} sel target:\n"
        for t in targets:
            req += t.name
            req += "\n"
               
        while all(t.name != repply for t in targets):        
            repply = self._io.ask(req)
            
        return repply

    ###########################################################################
    def sel_card(self) -> card.cardbase.CardBase:
        """
        Function to ask the player for selection of target card
        with the cards in its hand.
        :return: Returns the selected card.
        """
        if len(self._cards) == 0:
            return card.Card(card.CardEnum.INVALID,-1)
        
        req = f"{self.name} sel card:\n"
        for i,c in enumerate(self._cards):
            req += f"{i}-{c.card.name}" 
            req += f" {c.unique} \n"
        
        ret = ""
        while ret not in [str(i) for i in range(len(self._cards))]:
            ret = self._io.ask(req)
            
        return self._cards[int(ret)]
    
    ###########################################################################
    def sel_action(self, actions: List[moves.MovesEnum]) -> moves.MovesEnum:
        """
        Method to ask player for selection of its next action
        :return: it returns the selected action
        """
        
        req = f"{self.name} sel action\n"
        for v in actions:
            req += f"{v.name} \n"
        
        key : List[moves.MovesEnum] = []
        while not key:
            rep = self._io.ask(req)
            key = [k for k in actions if k.name == rep]
        
        return key[0]
    
        
        
        
        
        
        
    