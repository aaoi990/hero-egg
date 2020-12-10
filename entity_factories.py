from components.ai import BaseAI, HostileEnemy
from components.consumable import HealthPotion
from components.fighter import Fighter
from components.inventory import Inventory
from entity import Actor, Item
import enum

player = Actor(char="@", color=(255, 255, 0), name="EGG", ai=BaseAI(),
               fighter=Fighter(hp=30, defense=2, power=5), inventory=Inventory(capacity=15))

orc = Actor(char="S", color=(63, 127, 63), name="Spoon", ai=HostileEnemy(),
            fighter=Fighter(hp=10, defense=0, power=3), inventory=Inventory(capacity=0))

troll = Actor(char="T", color=(0, 127, 0), name="Troll", ai=HostileEnemy(),
              fighter=Fighter(hp=16, defense=1, power=4), inventory=Inventory(capacity=0))

health_potion = Item(char="!", color=(255, 255, 255),
                     name="HP Potion +4", consumable=HealthPotion(amount=4))

health_potion_medium = Item(char="!", color=(255, 255, 255),
                            name="HP Potion +10", consumable=HealthPotion(amount=10))

health_potion_max = Item(char="!", color=(255, 255, 255),
                         name="MAX HP Potion", consumable=HealthPotion(amount=100))


ConsumableItems = [health_potion, health_potion_medium, health_potion_max]
