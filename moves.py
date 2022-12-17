import enum

class MovesEnum(enum.Enum):
    """
    Enumeration of player actions
    """
    INCOME = enum.auto()
    FOREIGN_ADD = enum.auto()
    COUP = enum.auto()
    DUKE = enum.auto()
    ASSASSIN = enum.auto()
    CAPTAIN = enum.auto()
    AMBASSADOR = enum.auto()
