import pygame


class Spaceship(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, window):
        super().__init__()
        self.x_position = x
        self.y_position = y
        self.width = width
        self.height = height
        self.window = window
        self.movement_speed = 5
        self.image = pygame.image.load(f"./assets/space_ship/space_ship.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (width * 1, height * 1))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

    def handle_movement(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.x_position -= self.movement_speed
            if self.x_position <= self.width:
                self.x_position = self.width

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.x_position += self.movement_speed
            if self.x_position >= self.window.get_width() - self.width:
                self.x_position = self.window.get_width() - self.width

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.y_position -= self.movement_speed
            self.rect = self.image.get_rect()
            if self.y_position <= self.window.get_height() / 2:
                self.y_position = self.window.get_height() / 2

        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.y_position += self.movement_speed
            self.image = self.image
            if self.y_position >= self.window.get_height() - self.height:
                self.y_position = self.window.get_height() - self.height

        self.rect.center = (self.x_position, self.y_position)

    def draw(self):
        self.window.blit(self.image, self.rect)

    def update(self):
        self.draw()
        self.handle_movement()
