import pygame
import sys

from Basen.basis_szene import Szene

from settings import Settings

from Mazestuff.maze import Maze
from LostKnightDB import Spieler


class Spielszene(Szene):
    def __init__(self, display, manager):
        super().__init__()
        self.display = display
        self.manager = manager
        self.settings = Settings()

        self.maze = Maze(self.settings.maze_breite, self.settings.maze_hoehe)
        self.maze_size = 40

        spawn_x, spawn_y = self.maze.koords['Spawn']
        self.spieler = Spieler(Name='Justin', x=spawn_x, y=spawn_y)

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    def draw(self):
        self.display.fill(self.settings.hintergrundFarbe)

        px, py = self.spieler.x, self.spieler.y

        for dy in range(-self.settings.field_of_view, self.settings.field_of_view+1):
            for dx in range(-self.settings.field_of_view, self.settings.field_of_view + 1):
                x = px + dx
                y = py + dy

