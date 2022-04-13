from typing import Iterable, Any

from tcod.context import Context
from tcod.console import Console

from classes import Scene, Player

from navigator import Navigator

class Engine:
    def __init__(self, player: Player, navigator: Navigator, start_scene: Scene):
        self.player = player
        self.current_scene = start_scene
        self.navigator = navigator
        
    def handle_events(self, events: Iterable[Any], context: Context) -> Console | None:
        for event in events:
                action = self.current_scene.event_handler.dispatch(event)

                if action is None:
                    continue
                    
                if action.navigate:
                    self.current_scene.on_unload()
                    self.current_scene = self.navigator.navigate(action.key, action.payload)
                elif action.resize:
                    return context.new_console(order="F")
                else:
                    action.perform(self)

    def render(self, root_console: Console, context: Context) -> None:
        self.current_scene.render(root_console)
        context.present(root_console, integer_scaling=True)
        root_console.clear()