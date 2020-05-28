import logging
import random
from collections import namedtuple
from bearlibterminal import terminal
from thematics import Thematics

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class Game:
    def __init__(self):
        self.blt = terminal
        self.themes = Thematics(self.blt)
        self.board_w = 80
        self.board_h = 30

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

    def draw_game_boarders(self):
        logger.info('Drawing game board edges')
        for x in range(self.board_w):
            self.blt.put(x, 0, 'x' if x % 2 else '#')
            self.blt.put(x, self.board_h - 1, 'x' if x % 2 else '#')

        for y in range(self.board_h):
            self.blt.put(0, y, 'x' if y % 2 else '#')
            self.blt.put(self.board_w - 1, y, 'x' if y % 2 else '#')

        self.blt.refresh()

    def game_loop(self):
        self.blt.clear()
        self.draw_game_boarders()

        logger.info("Game loop init")
        while True:
            key = self.blt.read()
            self.blt.put(1, 10, 'x')
            if key in (self.blt.TK_CLOSE, self.blt.TK_ESCAPE):
                logger.info('Quitting')
                break

            logger.info("Key press: " + str(key))
            self.blt.refresh()
