from sqlobject import *


sqlhub.processConnection = connectionForURI('sqlite:LostKnightDB.sqlite')


class Spieler(SQLObject):
    Name = StringCol()
    Leben = IntCol()
    Kraft = IntCol()
    Verteidigung = IntCol()
    x = IntCol()
    y = IntCol()
    Maze = StringCol()
    LastUsage = DateTimeCol()
