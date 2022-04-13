import numpy as np
import tcod
from tcod import Console
from classes import Scene
from scenes.main.event_handler import EventHandler

class Main(Scene):
    def __init__(self, payload):
        self.name = "Main"
        if payload:
            self.x = payload["x"]
            self.y = payload["y"]

    @property
    def event_handler(self):
        return EventHandler(self)

    def render(self, root_console: Console):
        console, = tcod.console.load_xp('./assets/smile.xp', order="F")   
        CP437_TO_UNICODE = np.asarray(tcod.tileset.CHARMAP_CP437)  
        console.ch[:] = CP437_TO_UNICODE[console.ch]

        KEY_COLOR = (255, 0, 255)
        is_transparent = (console.rgb["bg"] == KEY_COLOR).all(axis=-1)
        console.rgba[is_transparent] = (ord(" "), (0,), (0,))

        console.blit(root_console)