from scenes.component import Component


class Card(Component):
    def __init__(self, code, target, deck):
        if not self.console:
            self.console = self.console_from_xp("~/../assets/Card.xp")
    
    def render(self, parent_console, x, y):
        self.console.blit(parent_console, x, y)
