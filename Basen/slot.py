from Basen.button import Button


class Slot:
    def __init__(self, x, y, b, h, spieler=None):
        self.button = Button(x, y, b, h, text='Leerer Slot')
        self.spieler = spieler

    def get_text(self):
        if self.spieler:
            return f'{self.spieler.Name}'
        else:
            return 'Leerer Slot'

    def handle_events(self, event):
        return self.button.handle_events(event)

    def draw(self, screen):
        self.button.draw(screen, newtext=self.get_text())
