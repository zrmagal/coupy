import enum
from typing import *
from types import FunctionType
from coupy import player
from coupy import moves
from abc import abstractmethod



def _noop() -> None:
    pass

class Action:
    _players : List[player.Player]
    _cp : int
    
    """
    Class to represent players' actions
    """
    ###########################################################################
    def __init__(self, cost: int = 0, callback: Callable[[], None] = _noop) -> None:
        """
        Action constructor
        :cost: how many coins this action costs
        :callback: function to perform the action
        """
        self.cost = cost
        self.callback = callback

    ###########################################################################
    @classmethod
    def _options(cls: Type["Action"]) -> Dict[moves.MovesEnum, "Action"]: 
        """
        Function to get table with all actions information
        :return: dict that defines the cost and callback for each action
        """         
        return {
            moves.MovesEnum.INCOME:      cls(0, cls._income),
            moves.MovesEnum.FOREIGN_ADD: cls(0, cls._foreign_add),
            moves.MovesEnum.COUP:        cls(7, cls._coup),
            moves.MovesEnum.DUKE:        cls(0, cls._duke),
            moves.MovesEnum.ASSASSIN:    cls(3, cls._assassin),
            moves.MovesEnum.CAPTAIN:     cls(0, cls._captain),
            moves.MovesEnum.AMBASSADOR:  cls(0, cls._ambassador)}
 
    ###########################################################################   
    @classmethod
    def _income(cls) -> None:
        cls._players[cls._cp].add_coins(2) # type: ignore
        
    ###########################################################################
    @classmethod
    def _foreign_add(cls) -> None:
        pass

    ###########################################################################
    @classmethod
    def _coup(cls) -> None:
        pass
    
    ###########################################################################
    @classmethod
    def _duke(cls) -> None:
        pass

    ###########################################################################
    @classmethod
    def _assassin(cls) -> None:
        pass
    
    ###########################################################################
    @classmethod
    def _captain(cls) -> None:
        pass

    ###########################################################################
    @classmethod
    def _ambassador(cls) -> None:
        pass
    
    ###########################################################################
    @classmethod
    def _dummy(cls) -> None:
        pass

    ###########################################################################
    @classmethod
    def options(cls) -> Dict[moves.MovesEnum, "Action"]:          
        opt = cls._options()
        return {x:y for x,y in opt.items() if y.cost <= cls._players[cls._cp].coins}
