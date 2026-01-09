from sqlobject import *

sqlhub.processConnection = connectionForURI('sqlite:LostKnightDB.sqlite')


class Spieler(SQLObject):
    Name = StringCol()
    x = IntCol()
    y = IntCol()
