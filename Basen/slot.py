from Basen.button import Button


class Slot:
    def __init__(self, x, y, b, h, spieler=None):
        self.button = Button(x, y, b, h, text='Leerer Slot', auswahlbar=bool(spieler))
        self.spieler = spieler

    def get_text(self):
        if self.spieler:
            return f'UID: {self.spieler.id} - {self.spieler.Name}' if self.spieler else 'Leerer Slot'
        else:
            return 'Leerer Slot'

    def handle_events(self, event):
        return self.button.handle_events(event)

    def draw(self, screen):
        self.button.draw(screen, newtext=self.get_text())
