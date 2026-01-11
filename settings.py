import pygame


class Settings:
    def __init__(self):
        pygame.init()
        self.bildschirm_breite = pygame.display.Info().current_w
        self.bildschirm_hoehe = pygame.display.Info().current_h

        self.maze_breite = 30
        self.maze_hoehe = 15
        self.feld_size = 30
        self.maze_pixel_breite = self.maze_breite * self.feld_size
        self.maze_pixel_hoehe = self.maze_hoehe * self.feld_size

        # Charakter Auswahl
        self.slot_anzahl = 8

        self.hintergrundFarbe = (0, 0, 0)
        self.fov = 1
        self.fps = 60
