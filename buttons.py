from mazes import mazes

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

    def draw(self, mouse, pygame, window, button_font, clicked):
        button_text = button_font.render(self.get_name(), True, (255,255,255))

        if self.get_x_pos() <= mouse[0] <= self.get_x_pos()+140 and self.get_y_pos() <= mouse[1] <= self.get_y_pos()+40:
            pygame.draw.rect(window, (150,150,150), [self.get_x_pos(), self.get_y_pos(), 140, 40])
        else:
            pygame.draw.rect(window, (0,0,0), [self.get_x_pos(), self.get_y_pos(), 140, 40])

        window.blit(button_text, (self.get_x_pos()+5, self.get_y_pos()+10))

    