import logging
import random
from collections import namedtuple
from bearlibterminal import terminal
from thematics import Thematics
from gui import Gui
from map import Map

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class Game:
    def __init__(self):
        self.blt = terminal
        self.game_w = 120
        self.game_h = 40
        self.themes = Thematics(self.blt)
        self.gui = Gui(self.game_w, self.game_h)
        self.map = Map()

    def __del__(self):
        self.blt.close()

    def start(self):
        self.blt.open()
        self.blt.set(
            "window: size=120x40, cellsize=auto, title='Hero Egg: The Beginning'; font: default")
        self.blt.color("white")

        logger.info("Terminal started")
        if(self.themes.intro_loop()):
            self.game_loop()
        else:
            self.blt.close()

    def game_loop(self):
        self.blt.clear()
        self.gui.draw_game_menu()
        self.map.draw_map()
        logger.info("Game loop init")
        while True:
            key = self.blt.read()
            self.blt.put(1, 10, 'x')
            if key in (self.blt.TK_CLOSE, self.blt.TK_ESCAPE):
                logger.info('Quitting')
                break

            logger.info("Key press: " + str(key))
            self.blt.refresh()
