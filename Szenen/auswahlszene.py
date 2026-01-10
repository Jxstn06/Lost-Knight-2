import pygame
import sys

from Basen.basis_szene import Szene
from Basen.button import Button
from Basen.slot import Slot

from settings import Settings
from lostknightdb import Spieler


class Auswahlszene(Szene):
    def __init__(self, display, manager):
        super().__init__()
        self.display = display
        self.manager = manager
        self.settings = Settings()

        self.slots = []
        self.spieler = list(Spieler.select())
        self.ausgewaehlt = None

        self.buttons = [
            Button(self.settings.bildschirm_breite//10*7,
                   self.settings.bildschirm_hoehe//10*5,
                   self.settings.bildschirm_breite//10*2,
                   (self.settings.bildschirm_hoehe//10*1)/2,
                   'Delete')
        ]

        self.build_slots()

    def build_slots(self):
        self.slots.clear()
        for i in range(self.settings.slot_anzahl):
            spieler = self.spieler[i] if i < len(self.spieler) else None

            slot = Slot(
                x=self.settings.bildschirm_breite // 2 - 200,
                y=150 + i * 100,
                b=400,
                h=50,
                spieler=spieler
            )
            self.slots.append(slot)

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        for slot in self.slots:
            if slot.handle_events(event):
                if slot.spieler:
                    # Alle werden unselected
                    for s in self.slots:
                        s.button.selected = False
                    # Angeklickter Slot wird makiert
                    slot.button.selected = True
                    print(f'Gewählt| UID: {slot.spieler.id} - {slot.spieler.Name}')
                else:
                    self.manager.set_szene('newcharszene')

    def draw(self):
        self.display.fill(self.settings.hintergrundFarbe)

        # Spielerliste Aktualisieren
        self.spieler = list(Spieler.select())
        for i, spieler in enumerate(self.spieler):
            if i < len(self.slots):
                self.slots[i].spieler = spieler
                self.slots[i].button.auswahlbar = True

        for slot in self.slots:
            slot.draw(self.display)

        for b in self.buttons:
            b.draw(self.display)
