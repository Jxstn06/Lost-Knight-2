import pygame
import sys

from Basen.basis_szene import Szene
from Basen.button import Button
from settings import Settings


class Menuszene(Szene):
    def __init__(self, display, manager):
        super().__init__()
        self.display = display
        self.manager = manager
        self.settings = Settings()

        self.buttons = [
            Button(int(self.settings.bildschirm_breite//2-100), self.settings.bildschirm_hoehe/10*3, 200, 50, 'Play'),
            Button(int(self.settings.bildschirm_breite//2-100), self.settings.bildschirm_hoehe/10*6, 200, 50, 'Quit')
        ]

    def handle_events(self, event):
        for button in self.buttons:
            if button.handle_events(event):
                if button.text == 'Play':
                    self.manager.set_szene('auswahlszene')
                if button.text == 'Quit':
                    pygame.quit()
                    sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    def draw(self):
        self.display.fill(self.settings.hintergrundFarbe)

        for button in self.buttons:
            button.draw(self.display)
