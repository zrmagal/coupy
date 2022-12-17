from typing import *
from coupy import deckbase
from coupy import card


class DeckCustom(deckbase.DeckBase):
    _type: Type[card.Card] = card.Card
    
    ###########################################################################
    def __init__(self, name: str) -> None:
        """
        Costructor of Deck object (card set)
        :name: A string tha names the deck
        """
        deckbase.DeckBase.__init__(self, name)
    
class DeckShared:
    """
    Class to represent shared decks. Card out of players' hands.
    """
    revealed = DeckCustom("revealed") # revealed cards
    stack = DeckCustom("stack") # unrevealed cards out of players' hands 
    
    ###########################################################################
    @classmethod
    def set_up(cls, each_count: int) -> None:
        """
        Method to initialized the shared decks with all the cards in the stack,
        assuming there is no card in players' hands.
        """
        cls.revealed.build()
        cls.stack.build(each_count)

class Deck(DeckCustom):
    ###########################################################################
    def __init__(self, name: str) -> None:
        """
        Costructor of Deck object (card set)
        :name: A string tha names the deck
        """
        DeckCustom.__init__(self, name)
    
    ###########################################################################
    def reveal(self, target_card: Type[card.Card]) -> None:
        """
        Method to revealled a card from deck object
        :target_card: Card to be revealled
        """
        self.move(DeckShared.revealed, target_card)
        
    ###########################################################################
    def draw(self) -> None:
        """
        Method to add into a deck a random card from common stack
        """
        DeckShared.stack.move(self, None)
    
    ###########################################################################
    def stack(self, target_card: Type[card.Card]) -> None:
        """
        Method to move a card from Deck to common stack
        """
        self.move(DeckShared.stack, target_card)

TDECK = TypeVar('TDECK', bound=Deck)