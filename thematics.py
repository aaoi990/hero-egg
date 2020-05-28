import logging
from collections import namedtuple
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class Thematics:
    def __init__(self, blt):
        logger.info('Loaded themes')
        self.intro_complete = False
        self.blt = blt

    def __del__(self):
        pass

    def intro_loop(self):
        self.blt.clear()
        intro_txt = ("Hero [c=orange]Egg[/c]. \n"
                     "There once was an [c=orange]egg[/c].\n"
                     "He was round, and brown.\n"
                     "He lived for adventure.\n\n"
                     "1. Go on an [c=orange]egg[/c]venture.\n"
                     "2. Load an [c=orange]egg[/c]venture.\n"
                     "3. See high scores.\n"
                     "4. Quit")

        self.blt.puts(60, 5, intro_txt, align=self.blt.TK_ALIGN_CENTER)

        while True:
            self.blt.refresh()
            key = self.blt.read()
            if key == self.blt.TK_ESCAPE:
                self.blt.clear()
                break
            elif key == self.blt.TK_1:
                logger.info('Starting eggventure')
                break
            elif key == self.blt.TK_2:
                logger.info('Loading eggventure')
                self.blt.clear()
            elif key == self.blt.TK_3:
                logger.info('Showing highscores')
                self.blt.clear()
            elif key == self.blt.TK_4:
                logger.info('Terminating through menu')
                return False

        self.blt.refresh()
        return True
