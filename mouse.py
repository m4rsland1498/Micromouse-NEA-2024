class mouse_sprite(object):

    def __init__(self):
        self.x = 175
        self.y = 175
        self.width_height = 20

    def draw(self, window, pygame):
        mouse_image = pygame.draw.rect(window, (0, 0, 255),
        [self.x, self.y, self.width_height, self.width_height])