from __future__ import annotations
import copy
from typing import Tuple, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from game_map import GameMap

T = TypeVar("T"m bound="Entity")


class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """

    def __init__(self, x: int, y: int, max_hp: int, char: str, color: Tuple[int, int, int]):
        self.x = x
        self.y = y
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.char = char
        self.color = color

    def move(self, dx: int, dy: int) -> None:
        # Move the entity by a given amount
        self.x += dx
        self.y += dy
