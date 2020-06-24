from bearlibterminal import terminal as blt
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class Terrain:
    def __init__(self, terrain_id, name, icon_seen, icon_unseen, blocks,
                 blocks_sight=None):
        self.terrain_id = terrain_id
        self.name = name
        self.icon_seen = icon_seen
        self.icon_unseen = icon_unseen
        self.blocks = blocks

        if blocks_sight is None:
            blocks_sight = blocks
        self.blocks_sight = blocks_sight


terrain_types = [Terrain(0, 'rock', 0xE060, 0xE061, True),
                 Terrain(1, 'floor', 0xE053, 0xE052, False),
                 Terrain(2, 'wall', 0xE062, 0xE060, True),
                 Terrain(3, 'door_closed', 0xE070, 0xE070, False, True)]


class Map:
    def __init__(self):
        self.map_w = 99
        self.map_h = 31

    def draw_map(self):
        blt.set("U+E200: assets/Tiles.png, size=32x32, align=center")
        blt.put(0, 0, 0xE200)
        blt.pick(0, 0)
        #blt.put(4, 2, 0xE200+1)
        logger.info('eee' + str(blt.pick(0, 0, 0)))
        #blt.put(2+3+10, 7, 0xE200+9)
        # for x in range(self.map_w):
        #    for y in range(self.map_h):
        #        if x % 4 == 0:
        #            blt.put(x, 0, 0xE200)
        #            blt.put(x, y+2, 0xE200+1)

        blt.refresh()
