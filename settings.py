import pygame


class Settings:
    def __init__(self):
        pygame.init()
        self.bildschirm_breite = pygame.display.Info().current_w
        self.bildschirm_hoehe = pygame.display.Info().current_h

        self.maze_breite = 30
        self.maze_hoehe = 10
        self.feld_size = 32
        self.maze_pixel_breite = self.maze_breite * self.feld_size
        self.maze_pixel_hoehe = self.maze_hoehe * self.feld_size

        self.hintergrundFarbe = (0, 0, 0)
        self.field_of_view = 3
        self.fps = 30
