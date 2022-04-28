from typing import List
from tcod import Console
from classes import Scene
from scenes.battle.event_handler import EventHandler
from scenes.battle.render import render
from scenes.component import Component

class Battle(Scene):
    def __init__(self, payload):
        self.name = "Battle"
        self.components: List[Component] = []
        self.controller = None

    @property
    def event_handler(self):
        return EventHandler(self)

    def render(self, root_console: Console):
        render(root_console, self.components, self.controller)
