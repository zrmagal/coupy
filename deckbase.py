from coupy import cardbase
from random import choice
from typing import Type, List
from abc import abstractmethod
class DeckBase:
    """
    Base class of deck (card set)
    """
    ###########################################################################
    def __init__(self, name: str) -> None:
        """
        Costruct of DeckBase (Card set)
        :name: Deck name
        :card_type: Type of deck's cards
        """
        self._name = name
        self._cards : List[cardbase.CardBase] = []
      
    ###########################################################################
    @property 
    @abstractmethod
    def _type(self) -> Type[cardbase.CardBase]:
        """
        Enumeration of deck's supported cards
        """
        raise NotImplementedError
        
    ###########################################################################
    def set_name(self, name: str) -> None:
        """
        Method to change the name of deck
        """
        self._name = name
    
    ###########################################################################
    def build(self, each_count: int = 0) -> None:
        """
        Method to reset the cards in the deck
        :each_count: number of cards of each type in the deck
        """        
        self._cards = [self._type(c, id) for c in self._type._enum  # type: ignore      
                                   for id in range(each_count)]
    
    ###########################################################################
    def add(self, new_card: Type[cardbase.CardBase]) -> None:
        """
        Insert a card into the deck
        :new_card: card added to the deck
        """
        assert isinstance(new_card, cardbase.CardBase) and  new_card.is_valid(), (
            f"Invalid card type {type(new_card)} for deck {self._name}"
        )
        
        self._cards.append(new_card)
    
    ###########################################################################
    def move(self, 
             dest,
             card: Type[cardbase.CardBase] = None) -> None:
        """
        Moves a card from this deck to another
        :dest: Destination deck
        :card: card to be moved. None selects a radom card.
        """
        assert self._cards,(
            f"Cannot move card from empty deck {self._name}"
        )
        
        if card is None:
            c : cardbase.CardBase = choice(self._cards)
            self._cards.remove(c)
            dest.add(c)
        else:
            assert (isinstance(card, cardbase.CardBase) and card.is_valid()), (
                f"Card {type(card)} is invalid for deck {self._name}"
            )
            
            it = [x for x in self if (x == card)]
            print(it[0])
            if it:
                self._cards.remove(it[0])
                dest.add(card)
    
    ###########################################################################
    def show(self) -> None:
        """
        Print the deck's cards
        """
        for c in self._cards:
            c.show()
