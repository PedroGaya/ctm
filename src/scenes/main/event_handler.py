from typing import Optional
import tcod.event

from classes import Action, BaseEventHandler, ChangeSceneAction, WindowResizeAction

from scenes.main.actions import MovementAction

class EventHandler(BaseEventHandler):
    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym

        if key == tcod.event.K_UP:
            action = MovementAction(dx=0, dy=-1)
        elif key == tcod.event.K_DOWN:
            action = MovementAction(dx=0, dy=1)
        elif key == tcod.event.K_LEFT:
            action = MovementAction(dx=-1, dy=0)
        elif key == tcod.event.K_RIGHT:
            action = MovementAction(dx=1, dy=0)

        elif key == tcod.event.K_s:
            action = ChangeSceneAction('BATTLE', payload={ "x": 1, "y": 1 })

        elif key == tcod.event.K_ESCAPE:
            raise SystemExit()

        # No valid key was pressed
        return action

    def ev_windowresized(self, event: tcod.event.WindowResized) -> Optional[Action]:
        return WindowResizeAction()