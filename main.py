from lostknight import LostKnight
from LostKnightDB import Spieler

if __name__ == "__main__":
    Spieler.createTable(ifNotExists=True)
    LostKnight = LostKnight()
    LostKnight.run()
