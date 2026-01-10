from sqlobject import *


sqlhub.processConnection = connectionForURI('sqlite:LostKnightDB.sqlite')


class Spieler(SQLObject):
    Name = StringCol(default="Justin")
    Leben = IntCol(default=1)
    Kraft = IntCol(default=1)
    Verteidigung = IntCol(default=1)
    x = IntCol(default=0)
    y = IntCol(default=0)
    Maze = StringCol(default="")
    LastUsage = DateTimeCol(default=None)
