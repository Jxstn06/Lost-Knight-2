import pygame, sys
from settings import Settings

from manager import Manager
from Szenen.menu import Menuszene


class LostKnight:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.bildschirm_breite, self.settings.bildschirm_hoehe))
        self.clock = pygame.time.Clock()
        self.running = True

        self.manager = Manager('menuszene')
        self.menuszene = Menuszene(self.screen, self.manager)

        self.szenen = {
            'menuszene': self.menuszene
        }
        self.manager.szenen = self.szenen

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.szenen[self.manager.get_szene()].handle_events(event)
            self.szenen[self.manager.get_szene()].draw()
            pygame.display.update()
            self.clock.tick(self.settings.fps)

        pygame.quit()
        sys.exit()
