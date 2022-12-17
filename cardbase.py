from enum import Enum
from typing import Type, Any, NamedTuple
from abc import abstractmethod
class CardBase(NamedTuple):
    card: Enum
    unique: Any
        
    ###########################################################################
    @property
    @abstractmethod
    def _enum(self) -> Type[Enum]:
        """
        Enumeration type of deck's cards
        """
        raise NotImplementedError
    
    
    ###########################################################################
    def is_valid(self) -> bool:
        """
        Method to check if a given card is part of deck
        """
        return self.card in self._enum 
    
    ###########################################################################
    def show(self) -> None:
        """
        Method to print  the card name and index
        """
        print(f"{self.card} {self.unique}")

