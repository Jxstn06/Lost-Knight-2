import pygame
import sys

from Basen.basis_szene import Szene
from Mazestuff.maze import Maze
from settings import Settings
from lostknightdb import Spieler


class Spielszene(Szene):
    def __init__(self, display, manager):
        super().__init__()
        self.display = display
        self.manager = manager
        self.settings = Settings()

        self.maze = Maze(self.settings.maze_breite, self.settings.maze_hoehe)
        self.spawnx, self.spawny = self.maze.koords['Spawn']

        self.maze = Maze(self.settings.maze_breite, self.settings.maze_hoehe)

        spawn_x, spawn_y = self.maze.koords['Spawn']
        self.spieler = Spieler.get(1)
        self.spieler.x, self.spieler.y = spawn_x, spawn_y

        self.offset_x = (self.settings.bildschirm_breite - self.settings.maze_pixel_breite) // 2
        self.offset_y = (self.settings.bildschirm_hoehe - self.settings.maze_pixel_hoehe) // 2

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            dx, dy = 0, 0
            if event.key in (pygame.K_w, pygame.K_UP):
                dy = -1
            elif event.key in (pygame.K_s, pygame.K_DOWN):
                dy = 1

            if event.key in (pygame.K_a, pygame.K_LEFT):
                dx = -1
            elif event.key in (pygame.K_d, pygame.K_RIGHT):
                dx = 1

            # Neue Position
            nx = self.spieler.x + dx
            ny = self.spieler.y + dy

            # Schritt Überprüfung
            if 0 <= nx < self.maze.b and 0 <= ny < self.maze.h:
                if self.maze.grid[ny][nx].feldtyp != 'Wand':
                    self.spieler.x = nx
                    self.spieler.y = ny

    def draw(self):
        self.display.fill(self.settings.hintergrundFarbe)

        px, py = self.spieler.x, self.spieler.y

        for y in range(max(0, py - self.settings.fov), min(self.maze.h, py + self.settings.fov+1)):
            for x in range(max(0, px - self.settings.fov), min(self.maze.b, px + self.settings.fov+1)):
                feld = self.maze.grid[y][x]
                # x/y aktuelle Entfernung vom Spieler
                abstand = max(abs(x - px), abs(y - py))
                # Deckt Felder auf
                if feld.feldtyp == 'Wand' or abstand <= self.settings.fov:
                    feld.entdeckt = True

        for y in range(self.maze.h):
            for x in range(self.maze.b):
                feld = self.maze.grid[y][x]
                abstand = max(abs(x - px), abs(y - py))

                # Skipped alle unentdeckten Felder
                if not feld.entdeckt:
                    continue

                if feld.feldtyp == 'Wand':
                    grundfarbe = (250, 250, 250)
                elif feld.feldtyp == 'Weg':
                    grundfarbe = (100, 100, 100)
                elif feld.feldtyp == 'Spawn':
                    grundfarbe = (40, 255, 40)
                else:
                    grundfarbe = (250, 250, 250)

                if abstand > self.settings.fov:
                    color = tuple(c//4 for c in grundfarbe)
                else:
                    fade = (self.settings.fov - abstand + 1) / self.settings.fov
                    color = tuple(max(0, min(255, int(c * fade))) for c in grundfarbe)

                # Draw Maze Felder
                pygame.draw.rect(
                    self.display,
                    color,
                    (
                        x*self.settings.feld_size + self.offset_x,
                        y*self.settings.feld_size + self.offset_y,
                        self.settings.feld_size,
                        self.settings.feld_size)
                    )
        # Draw Spieler
        pygame.draw.rect(
            self.display,
            (255, 0, 0),
            (
                px*self.settings.feld_size + self.offset_x,
                py*self.settings.feld_size + self.offset_y,
                self.settings.feld_size,
                self.settings.feld_size)
        )
