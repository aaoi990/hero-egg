import logging
from collections import namedtuple

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class Thematics:
    def __init__(self, blt):
        logger.info('Loaded themes')
        self.intro_complete = False
        self.terminal = blt

    def __del__(self):
        pass

    def intro(self, blt):
        self.terminal.puts(80-14, 3, "[c=orange][U+2588]")
