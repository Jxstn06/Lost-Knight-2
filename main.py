from lostknight import LostKnight
from lostknightdb import Spieler

if __name__ == "__main__":
    Spieler.createTable(ifNotExists=True)
    LostKnight = LostKnight()
    LostKnight.run()
