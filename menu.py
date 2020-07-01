import numpy as np  # type: ignore
from tcod.console import Console

class Menu:
    def __init__(self, screen_height: int, map_height:int, menu_width: int):
        self.menu_height = screen_height - map_height
        self.menu_width = menu_width
        self.menu_location = map_height

    def render(self, console: Console) -> None:
        console.draw_frame(0, 40, self.menu_width,self.menu_height,"MENU", True)