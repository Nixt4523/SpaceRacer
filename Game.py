import math

import pygame
import random
from Settings import *
from Spaceship import Spaceship
from Asteroids import Asteroids

pygame.init()
pygame.font.init()
pygame.mixer.init()


class Game:

    def __init__(self):

        self.SCREEN_WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Space Racer")
        self.background_image = pygame.image.load("./assets/background/background_space.jpg").convert()
        self.background_image = pygame.transform.scale(self.background_image, (self.SCREEN_WINDOW.get_width() * 2, self.SCREEN_WINDOW.get_height()))
        self.asteroids = []
        self.asteroids_wave = 5
        self.asteroids_velocity = 1
        self.CLOCK = pygame.time.Clock()
        self.RUN_GAME = True

        self.Spaceship = Spaceship(int(WIDTH/2), HEIGHT - 128, 64, 64, self.SCREEN_WINDOW)

        self.level = 0
        self.score = 0
        self.font = pygame.font.SysFont("comicsans", 24)
        self.title_font = pygame.font.SysFont("comicsans", 64)

        self.bg_scroll = 0
        self.tile = math.ceil(self.SCREEN_WINDOW.get_height() / self.SCREEN_WINDOW.get_height()) + 4
        pygame.mixer.music.load("./assets/background_music/background_music.mp3")
        pygame.mixer.music.set_volume(0.9)
        pygame.mixer.music.play()

    def update_screen_window(self):

        i = 0
        while i < self.tile:
            self.SCREEN_WINDOW.blit(self.background_image, (-int(self.SCREEN_WINDOW.get_width() - self.Spaceship.x_position / 2), -self.SCREEN_WINDOW.get_height() * i - self.bg_scroll))
            i += 1

        if abs(self.bg_scroll) > self.SCREEN_WINDOW.get_height():
            self.bg_scroll = 0

        self.bg_scroll -= self.asteroids_velocity * 1.5

        for asteroid in self.asteroids:
            asteroid.draw()

        if len(self.asteroids) == 0:
            self.asteroids_velocity += 0.5
            self.asteroids_wave += 2
            self.level += 1

            for i in range(self.asteroids_wave):
                asteroid = Asteroids(random.randrange(self.Spaceship.width, self.SCREEN_WINDOW.get_width() - self.Spaceship.width),
                                     random.randrange(-8000, -100),
                                     self.SCREEN_WINDOW, self.asteroids_velocity + len(self.asteroids)/2)
                self.asteroids.append(asteroid)

        for asteroid in self.asteroids[:]:
            asteroid.move()
            if asteroid.y_position >= HEIGHT:
                self.asteroids.remove(asteroid)

            offset = (int(self.Spaceship.x_position - asteroid.x_position), int(self.Spaceship.y_position - asteroid.y_position))
            collision = asteroid.mask.overlap(self.Spaceship.mask, offset)
            if collision:
                self.game_over()

        self.score = int(pygame.time.get_ticks() / 100)

        live_label = self.font.render(f"Level {self.level}", True, (255, 255, 255))
        score_label = self.font.render(f"Score {self.score}", True, (255, 255, 255))

        self.SCREEN_WINDOW.blit(live_label, (self.SCREEN_WINDOW.get_width() - live_label.get_width() - 10, 10))
        self.SCREEN_WINDOW.blit(score_label, (10, 10))

        self.Spaceship.update()
        pygame.display.update()

    def game_over(self):

        run = True

        while run:
            label = self.font.render("Press ESCAPE to Quit the Game", True, (255, 255, 255))
            title = self.title_font.render("Game Over", True, (255, 255, 255))
            score = self.font.render(f"Your Score : {self.score}", True, (255, 255, 255))
            self.SCREEN_WINDOW.fill("black")
            self.SCREEN_WINDOW.blit(label, (self.SCREEN_WINDOW.get_width() / 2 - label.get_width() / 2,
                                            self.SCREEN_WINDOW.get_height() / 2 - label.get_height() / 2 + label.get_height()))
            self.SCREEN_WINDOW.blit(title, (self.SCREEN_WINDOW.get_width() / 2 - title.get_width() / 2,
                                            self.SCREEN_WINDOW.get_height() / 2 - title.get_height() / 2 - 48))
            self.SCREEN_WINDOW.blit(score, (self.SCREEN_WINDOW.get_width() / 2 - score.get_width() / 2,
                                            self.SCREEN_WINDOW.get_height() / 2 - score.get_height() / 2 + 100))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    exit()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                pygame.quit()
                exit()

    def run(self):

        while self.RUN_GAME:

            self.CLOCK.tick(FPS)
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    self.RUN_GAME = False
                    pygame.quit()
                    exit()

            self.update_screen_window()


if __name__ == "__main__":
    game = Game()
    game.run()
