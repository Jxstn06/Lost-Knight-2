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

        spawn_x, spawn_y = self.maze.koords['Spawn']
        self.spieler = Spieler(Name='Justin', x=spawn_x, y=spawn_y)

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    def draw(self):
        self.display.fill(self.settings.hintergrundFarbe)

        maze_offset_x = (self.settings.bildschirm_breite - self.settings.maze_pixel_breite) // 2
        maze_offset_y = (self.settings.bildschirm_hoehe - self.settings.maze_pixel_hoehe) // 2

        px, py = self.spieler.x, self.spieler.y

        for dy in range(-self.settings.field_of_view, self.settings.field_of_view+1):
            for dx in range(-self.settings.field_of_view, self.settings.field_of_view + 1):
                # x/y aktuelle Spieler_pos | Offset
                x = px + dx
                y = py + dy

                # Für Ränder
                if 0 <= x < self.maze.b and 0 <= y < self.maze.h:
                    feld = self.maze.grid[y][x]

                    # Chebyshev Absolute Entfernung + Diagonale
                    abstand = max(abs(dx), abs(dy))

                    if feld.feldtyp == 'Wand':
                        grundfarbe = (255, 255, 255)
                    else:
                        grundfarbe = (0, 0, 0)

                    if abstand <= 1:
                        color = grundfarbe
                    else:
                        color = tuple(color//2 for color in grundfarbe)

                    # Draw Maze Felder
                    pygame.draw.rect(
                        self.display,
                        color,
                        (
                            x*self.settings.mazetilesize,
                            y*self.settings.mazetilesize,
                            self.settings.mazetilesize,
                            self.settings.mazetilesize)
                    )
        pygame.draw.rect(
            self.display,
            (255, 0, 0),
            (
                px*self.settings.mazetilesize,
                py*self.settings.mazetilesize,
                self.settings.mazetilesize,
                self.settings.mazetilesize)
        )
