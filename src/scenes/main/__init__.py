import numpy as np
import tcod
from tcod import Console
from classes import Scene
from component_loader import CONSOLE_MANAGER
from scenes.main.event_handler import EventHandler


class Main(Scene):
    def __init__(self, payload):
        self.name = "Main"


    @property
    def event_handler(self):
        return EventHandler(self)

    def render(self, root_console: Console):
        console = CONSOLE_MANAGER.get_console('smile')

        console.blit(root_console)