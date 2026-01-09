import pygame


class Settings:
    def __init__(self):
        pygame.init()
        self.bildschirm_breite = pygame.display.Info().current_w
        self.bildschirm_hoehe = pygame.display.Info().current_h

        self.maze_breite = 30
        self.maze_hoehe = 10

        self.hintergrundFarbe = (0, 0, 0)
        self.field_of_view = 2
        self.fps = 30
