from typing import *

from coupy import player
from coupy import deck
from coupy import msgdevice
from coupy import action


###########################################################################
def _noop() -> None:
    """
    Dummy function recorded as default action callback.
    """
    pass

class Game(action.Action):
    """
    Base class of game instance
    """
    _players: List[player.Player] # List of players
    _io: List[msgdevice.MsgDev] # List of devices used to communicate with each player
    _cp: int = 0 #Index of current player instance within players list.
    
    ###########################################################################
    def __init__(self, cost : int = 0, callback : Callable[[], None] = _noop) -> None:
        action.Action.__init__(self, cost, callback)

    ###########################################################################
    @classmethod
    def __set_players(cls, count : int):
        cls._io = [msgdevice.MsgDev() for i in range(count)]
        cls._players = [player.Player(f"player{i}", cls._io[i]) for i in range(count)]
        deck.DeckShared.set_up(3 if count < 5 else 4)
        
    ###########################################################################
    @classmethod
    def __deal(cls):
        for i,p in enumerate(cls._players):
            p.draw()
            p.draw()
            p.add_coins(2)

    ###########################################################################
    @classmethod
    def run(cls, count : int):
        cls.__set_players(count)
        cls.__deal()
        
        for cls._cp,p in enumerate(cls._players):
            opt = cls.options()
            valid = [x for x,y in opt.items()]
            act = cls._players[cls._cp].sel_action(valid)
            opt[act].callback()

