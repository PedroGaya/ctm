from typing import List
from pathlib import Path
import numpy as np

import tcod
from scenes.component import Component


class CMS:
    def __init__(self):
        self.keys: List[str] = []
        self.components: List[tcod.Console] = []

        for file in Path('./assets/components').glob('**/*.xp'):
            name = file.stem
            path = './assets/components/' + name + '.xp' 
            
            self.keys.append(name)
            self.components.append(self.console_from_xp(path))

    def get_console(self, key):
        index = self.keys.index(key)
        return self.components[index]

    def console_from_xp(self, path):
        console, = tcod.console.load_xp(path, order="F")   
        CP437_TO_UNICODE = np.asarray(tcod.tileset.CHARMAP_CP437)  
        console.ch[:] = CP437_TO_UNICODE[console.ch]

        KEY_COLOR = (255, 0, 255)
        is_transparent = (console.rgb["bg"] == KEY_COLOR).all(axis=-1)
        console.rgba[is_transparent] = (ord(" "), (0,), (0,))

        return console

CONSOLE_MANAGER = CMS()