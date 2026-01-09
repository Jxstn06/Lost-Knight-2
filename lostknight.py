import pygame, sys
from settings import Settings


class LostKnight:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.bildschirm_breite, self.settings.bildschirm_hoehe))

    def draw(self):
        while True:
            self.screen.fill(self.settings.hintergrundFarbe)