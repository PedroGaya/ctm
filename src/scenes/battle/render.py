from typing import Any, List
from tcod import Console
from scenes.component import Component


def render(root_console: Console, components: List[Component], controller: Any):
    NAV_MAP = [[]]

    for component in components:
        i = component.nav_index[0]
        j = component.nav_index[1]

        NAV_MAP[i][j] = component

    pass