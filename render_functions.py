from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tcod import Console
    from engine import Engine
    from game_map import GameMap
    from entity import Actor


def get_names_at_location(x: int, y: int, game_map: GameMap) -> str:
    names = ', '.join([entity.name for entity in game_map.entities if entity.x == x and entity.y == y and
                       game_map.visible[x, y]])

    return names.capitalize()


def render_menu(console: Console, map_height: int, menu_width: int) -> None:
    console.draw_frame(0, map_height, menu_width, 7, "MENU", True,
                       fg=(255, 255, 255),
                       bg=(0, 0, 0))

    console.draw_frame(80, 0, 20, 43, "EVENTS", True,
                       fg=(255, 255, 255),
                       bg=(0, 0, 0))


def render_stats(console: Console, character: Actor) -> None:
    console.print(x=1, y=47, string=f'ATT: {character.fighter.power}')
    console.print(x=1, y=48, string=f'DEF: {character.fighter.defense}')


def render_bar(console: Console, character: Actor, current_value: int, maximum_value: int, total_width: int) -> None:
    bar_width = int(float(current_value) / maximum_value * total_width)

    console.draw_rect(x=1, y=44, width=20,
                      height=1, ch=1, bg=(191, 0, 0))

    if bar_width > 0:
        console.draw_rect(x=1, y=44, width=bar_width,
                          height=1, ch=1, bg=(0, 191, 0))

    console.print(
        x=1, y=45, string=f'HP: {current_value}/{maximum_value}')

    render_stats(console, character)


def render_inventory_menu(console: Console, engine: Engine) -> None:
    """
    Render an inventory menu, which displays the items in the inventory, and the letter to select them.
    Will move to a different position based on where the player is located, so the player can always see where
    they are.
    """

    console.draw_frame(80, 0, 20, 43, "INVENTORY", True,
                       fg=(255, 255, 255),
                       bg=(0, 0, 0))

    number_of_items_in_inventory = len(engine.player.inventory.items)

    width = 20
    # number_of_items_in_inventory + 2
    height = engine.player.inventory.capacity + 2

    if height <= 3:
        height = 3

    # TODO: Fix these values, not quite right
    if engine.player.x <= 20:
        x = 20
    else:
        x = 0

    if engine.player.y <= 20:
        y = 20
    else:
        y = 0

    # console.draw_frame(x=x, y=y, width=width, height=height, title="Inventory", clear=True, fg=(255, 255, 255),
    #                   bg=(0, 0, 0))

    letter_index = ord('a')

    for i in range(engine.player.inventory.capacity):
        try:
            text = f"({chr(letter_index)}) {engine.player.inventory.items[i].name}"
        except AttributeError:
            text = f"({chr(letter_index)})"

        console.print(81, y=i+1, string=text)

        letter_index += 1


def render_names_at_mouse_location(console: Console, x: int, y: int, engine: Engine) -> None:
    mouse_x, mouse_y = engine.mouse_location

    names_at_mouse_location = get_names_at_location(
        x=mouse_x,
        y=mouse_y,
        game_map=engine.game_map
    )

    console.print(x=x, y=y, string=names_at_mouse_location)
