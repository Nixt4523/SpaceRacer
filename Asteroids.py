import random
import pygame


class Asteroids(pygame.sprite.Sprite):

    def __init__(self, x, y, window, velocity):
        super().__init__()
        self.x_position = x
        self.y_position = y
        self.window = window
        self.velocity = velocity
        self.height = 32
        self.width = 32
        self.scale_factor = random.randrange(2, 5)

        self.image = pygame.image.load("./assets/asteroids/asteroid_" +
                                       str(random.randrange(1, 16)) + ".png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width * self.scale_factor, self.height * self.scale_factor))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

    def move(self):
        self.y_position += self.velocity
        self.rect.center = (self.x_position, self.y_position)

    def draw(self):
        self.window.blit(self.image, self.rect)
