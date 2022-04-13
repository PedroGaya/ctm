from typing import Optional
from tcod import Console
import tcod.event

class Action:
    def __init__(self):
        self.navigate = False
        self.resize = False

    def perform(self, engine):
        pass

class ChangeSceneAction(Action):
    def __init__(self, key, payload):
        super().__init__()

        self.navigate = True
        self.key = key
        self.payload = payload

class EscapeAction(Action):
    pass

class WindowResizeAction(Action):
    def __init__(self):
        super().__init__()
        
        self.resize = True

class BaseEventHandler(tcod.event.EventDispatch[Action]):
        def __init__(self, parent_scene):
            self.scene = parent_scene

        def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
            raise SystemExit()

class Scene:
    def __init__(self, payload=None):
        self.payload = payload
        event_handler = BaseEventHandler(parent_scene=self)

    def on_load(self):
        pass

    def on_unload(self):
        pass

    def render(self, console: Console):
        pass

class Player:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
