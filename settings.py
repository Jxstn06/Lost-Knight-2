import pygame


class Settings:
    def __init__(self):
        pygame.init()
        self.bildschirm_breite = pygame.display.Info().current_w
        self.bildschirm_hoehe = pygame.display.Info().current_h
        self.hintergrundFarbe = (0, 0, 0)
        self.fps = 30