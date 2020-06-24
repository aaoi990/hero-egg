
from bearlibterminal import terminal as blt
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class Gui:
    def __init__(self, game_w, game_h):
        self.menu_w = 20
        self.menu_h = 10
        self.menu_loc_w = game_w - self.menu_w
        self.menu_loc_h = game_h - self.menu_h

    def draw_game_menu(self):
        for x in range(self.menu_w):
            blt.put(x + self.menu_loc_w, 0, 0x2550)
            blt.put(x + self.menu_loc_w, self.menu_loc_h, 0x2550)

        blt.refresh()
