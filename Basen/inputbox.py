import pygame


class Inputbox:
    def __init__(self, x, y, b, h, text='', color=(200, 200, 200), active_color=(255, 255, 0), maxtextlenght=12):
        self.rect = pygame.Rect(x, y, b, h)
        self.text = text
        self.font = pygame.font.Font(None, 30)

        # Farben
        self.color = color
        self.grundfarbe = color
        self.active_c = active_color

        self.active = False
        self.mtl = maxtextlenght

    def handle_events(self, event):
        # Hier wird geguckt, ob der letzte Mouseclick auf dem Feld war
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)

        # Schreib events
        if event.type == pygame.KEYDOWN and self.active:
            # Delete
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif len(self.text) < self.mtl:
                self.text += event.unicode

    def get_value(self):
        return self.text

    def draw(self, screen):
        pygame.draw.rect(screen, self.grundfarbe, self.rect)

        # Active Makierung
        pygame.draw.rect(screen, self.active_c if self.active else (0, 0, 0), self.rect, 3)

        text_rect = self.font.render(self.text, True, (0, 0, 0))
        text_center = text_rect.get_rect(center=self.rect.center)
        screen.blit(text_rect, text_center)
