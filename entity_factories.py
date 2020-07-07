from entity import Entity

player = Entity(100, char="@", color=(255, 255, 255),
                name="Player", blocks_movement=True)

orc = Entity(20, char="o", color=(63, 127, 63),
             name="Orc", blocks_movement=True)

troll = Entity(50, char="T", color=(0, 127, 0),
               name="Troll", blocks_movement=True)
