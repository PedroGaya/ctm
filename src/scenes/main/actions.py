from classes import Action

class MovementAction(Action):
    def __init__(self, dx: int, dy: int):
        super().__init__()

        self.dx = dx
        self.dy = dy

    def perform(self, engine):
        engine.current_scene.x += self.dx
        engine.current_scene.y += self.dy