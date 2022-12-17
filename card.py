from enum import Enum, auto
from coupy import cardbase
from typing import Type

class CardEnum(Enum):
    """ 
    Enumeration of card types 
    """
    AMBASSADOR = auto()
    ASSASSIN = auto()
    CAPTAIN = auto()
    CONTESSA = auto()
    DUKE = auto()
    INVALID = auto()

class Card(cardbase.CardBase):
    """
    Class of game specific cards
    """
    _enum : Type[Enum] = CardEnum
 