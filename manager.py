class Manager:
    def __init__(self, szene):
        self.szene = szene
        self.szenen = {}

        self.spieler = None
        self.maze = None

    def get_szene(self):
        return self.szene

    def set_szene(self, szene):
        self.szene = szene
