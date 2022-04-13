from classes import Scene
from scenes.battle import Battle
from scenes.main import Main

class Navigator:
    def __init__(self):
        self.map: dict[str, Scene] = {
            "MAIN": Main,
            "BATTLE": Battle
        }
        self.entry = Main(payload={ "x": 1, "y": 1 })

    def navigate(self, key, payload=None):
        scene = self.map[key]
        return scene(payload)

