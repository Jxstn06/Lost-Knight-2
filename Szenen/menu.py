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
            Button(self.settings.bildschirm_breite/2-100, self.settings.bildschirm_hoehe/9*6, 200, 50, 'Quit')
        ]

    def handle_events(self, event):
        for button in self.buttons:
            if button.handel_event(event):
                if button.text == 'Quit':
                    pygame.quit()
                    sys.exit()

    def draw(self):
        for button in self.buttons:
            button.draw(self.display)
