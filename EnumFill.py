import enum
from enum import Enum

@enum.unique
class EnumFill(Enum):
    """
    Describes whether the property is applied to the entire element,
    only to part of it, or not applied at all

    NO_APPLY - property does not occur in the element
    APPLY_TO_ALL_ELEMENTS -  property is applied to the entire element
    APPLY_TO_SOME_ELEMENTS -  property is applied to a part of the element (unknown which one)
    """
    NO_APPLY = 0
    APPLY_TO_ALL_ELEMENTS = 1
    APPLY_TO_SOME_ELEMENTS = 2
