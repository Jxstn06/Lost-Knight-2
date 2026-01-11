import pygame
import sys

from Basen.basis_szene import Szene
from Basen.button import Button
from Basen.inputbox import Inputbox


from settings import Settings

from lostknightdb import Spieler
from Mazestuff.maze import Maze


class Newcharszene(Szene):
    def __init__(self, display, manager):
        super().__init__()
        self.display = display
        self.manager = manager
        self.s = Settings()

        self.inputboxen = [
            Inputbox(
                x=self.s.bildschirm_breite//2-200,
                y=self.s.bildschirm_hoehe//10*3,
                b=400,
                h=50,
                text=''
            )
        ]

        self.buttons = [
            Button(self.s.bildschirm_breite//2-200, self.s.bildschirm_hoehe//10*8, 400, 50, 'Create')
        ]

    def new_maze(self):
        maze = Maze(self.s.maze_breite, self.s.maze_hoehe)
        px, py = maze.koords['Spawn']
        m = maze.to_string()
        return px, py, m

    def input_reset(self):
        for box in self.inputboxen:
            box.text = ''

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        for box in self.inputboxen:
            box.handle_events(event)

        for button in self.buttons:
            if button.handle_events(event):
                if button.text == 'Create':
                    name = self.inputboxen[0].get_value()
                    Spieler(
                        Name=name,
                        Leben=20,
                        Kraft=3,
                        Verteidigung=5,
                        x=self.new_maze()[0],
                        y=self.new_maze()[1],
                        Maze=self.new_maze()[2]
                    )
                    # Sorgt für einen leeren String am Anfang der Szene
                    self.input_reset()
                    self.manager.set_szene('auswahlszene')

    def draw(self):
        self.display.fill(self.s.hintergrundFarbe)
        for i in self.inputboxen:
            i.draw(self.display)

        for b in self.buttons:
            b.draw(self.display)
