from tcod import Console
from classes import Scene
from scenes.battle.event_handler import EventHandler

class Battle(Scene):
    def __init__(self, payload):
        self.name = "Battle"
        if payload:
            self.x = payload["x"]
            self.y = payload["y"]

    @property
    def event_handler(self):
        return EventHandler(self)

    def render(self, console: Console):
        console.print(self.x, self.y, "B", fg=(255, 0, 0))
