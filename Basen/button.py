import pygame


class Button:
    def __init__(self, x, y, b, h, text='', color=(200, 200, 200), hover_color=(255, 255, 0), spieler=None, auswahlbar=False):
        self.rect = pygame.Rect(x, y, b, h)
        self.text = text
        self.font = pygame.font.Font(None, 30)
        self.color = color
        self.hover_c = hover_color

        self.auswahlbar = auswahlbar
        self.selected = False

        self.spieler = spieler

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                return True
        return False

    def draw(self, screen, newtext=None):
        maus_pos = pygame.mouse.get_pos()
        is_hover = self.rect.collidepoint(maus_pos)

        if self.auswahlbar and self.selected:
            button_color = self.hover_c
        elif is_hover:
            button_color = self.hover_c
        else:
            button_color = self.color

        pygame.draw.rect(screen, button_color, self.rect)

        text = self.font.render(newtext if newtext is not None else self.text, True, (0, 0, 0))
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)
