import logging
from collections import namedtuple

from bearlibterminal import terminal
from thematics import Thematics
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class Game:
    def __init__(self):
        self.blt = terminal
        self.themes = Thematics(self.blt)

    def __del__(self):
        self.blt.close()

    def start(self):
        self.blt.open()
        self.blt.set(
            "window: size=120x40, cellsize=auto, title='Hero Egg: The Beginning'; font: default")
        self.blt.color("white")

        logger.info("Terminal started")
        self.themes.intro_loop()
        self.game_loop()

    def game_loop(self):
        logger.info("Game loop init")
        while True:
            self.blt.refresh()
            key = self.blt.read()
            if key in (self.blt.TK_CLOSE, self.blt.TK_ESCAPE):
                break
