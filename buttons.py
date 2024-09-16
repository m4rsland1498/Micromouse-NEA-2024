import pygame

class Buttons:
    instances = []

    def __init__(self, button_name, x, y):
        self.name = button_name
        self.x_pos = x
        self.y_pos = y
        Buttons.instances.append(self)

    def get_name(self):
        return self.name
    
    def get_x_pos(self):
        return self.x_pos
    
    def get_y_pos(self):
        return self.y_pos
    
    def set_function_():
        pass
    