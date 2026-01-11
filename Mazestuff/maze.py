import random as r
from Mazestuff.feld import Feld


class Maze:
    def __init__(self, breite, hoehe, grid=None, spawn=None):
        self.b = breite if breite % 2 == 1 else breite + 1
        self.h = hoehe if hoehe % 2 == 1 else hoehe + 1

        if grid:
            self.grid = grid
        else:
            self.grid = [[Feld(x, y, 'Wand') for x in range(self.b)] for y in range(self.h)]

        self.koords = {
                'Spawn': [r.randrange(1, self.b, 2), r.randrange(1, self.h, 2)]
            }
        sx, sy = self.koords['Spawn']
        self.grid[sy][sx].feldtyp = 'Spawn'

        # 20% Wahrscheinlichkeit, das eine Wand zum Weg wird.
        self.weg_algo(0.20)

    def weg_algo(self, chance):
        richtungen = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        start_x, start_y = self.koords['Spawn']

        stack = [(start_x, start_y)]
        visited = set()
        visited.add((start_x, start_y))

        while stack:
            x, y = stack[-1]
            # Damit der Spawnpunkt bleibt
            self.grid[y][x].feldtyp = 'Weg' if (x, y) != (start_x, start_y) else 'Spawn'

            nachbarn = []
            # dy/dy heißt zukünftige Position
            for dx, dy in richtungen:
                nachbar_x, nachbar_y = x + dx, y + dy
                # Ist der Nachbar/Schritt möglich?
                if 0 < nachbar_x < self.b and 0 < nachbar_y < self.h and (nachbar_x, nachbar_y) not in visited:
                    if self.grid[nachbar_y][nachbar_x].feldtyp == 'Wand':
                        nachbarn.append((nachbar_x, nachbar_y))

            if nachbarn:
                nachbar_x, nachbar_y = r.choice(nachbarn)
                self.grid[y + (nachbar_y - y) // 2][x + (nachbar_x - x) // 2].feldtyp = 'Weg'
                visited.add((nachbar_x, nachbar_y))
                stack.append((nachbar_x, nachbar_y))
            else:
                stack.pop()

        # Alle Wege mit Wand dazwischen
        for y in range(1, self.h-1):
            for x in range(1, self.b-1):
                if self.grid[y][x].feldtyp != 'Wand':
                    continue

                if self.grid[y][x-1].feldtyp == 'Weg' and self.grid[y][x+1].feldtyp == 'Weg' and r.random() < chance:
                    self.grid[y][x].feldtyp = 'Weg'

                elif self.grid[y-1][x].feldtyp == 'Weg' and self.grid[y+1][x].feldtyp == 'Weg' and r.random() < chance:
                    self.grid[y][x].feldtyp = 'Weg'

    def to_string(self):
        lines = []
        for zeile in self.grid:
            line = ''
            for zelle in zeile:
                match zelle.feldtyp:
                    case 'Wand':
                        line += '█'
                    case 'Spawn':
                        line += 'S'
                    case 'Weg':
                        line += ' '
                    case _:
                        line += '?'
            lines.append(line)
        return '\n'.join(lines)

    @classmethod
    def from_string(cls, text):
        lines = text.split('\n')
        h = len(lines)
        b = len(lines[0])
        grid = [[Feld(x, y, 'Wand') for x in range(b)] for y in range(h)]
        spawn = [0, 0]

        for y in range(h):
            for x in range(b):
                char = lines[y][x]
                feld = grid[y][x]

                if char == "█":
                    feld.feldtyp = 'Wand'
                elif char == " ":
                    feld.feldtyp = 'Weg'
                elif char == "S":
                    feld.feldtyp = 'Spawn'
                    spawn = [x, y]

        maze = cls(b, h, grid=None, spawn=None)
        maze.grid = grid
        maze.koords = {'Spawn': spawn}

        return maze

