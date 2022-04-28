import numpy as np
import tcod


class Component:
    def __init__(self, name):
        self.name = name
        self.selected = False
        self.nav_map = [[]]
        self.nav_index = [0, 0]
    
    def select(self):
        self.selected = True

    def deselect(self):
        self.selected = False

    def render(self, console):
        pass
