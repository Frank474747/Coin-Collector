import pygame
from setup import *

# Button class with rounded edges
class Button:
    def __init__(self, x, y, width, height, color, text, radius=20):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.font = pygame.font.Font(None, 36)
        self.text_surface = self.font.render(self.text, True, BLACK)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)
        self.radius = radius

    def draw(self, screen):
        # Draw the rounded rectangle (button)
        pygame.draw.rect(screen, self.color, self.rect, border_radius=self.radius)

        # Draw the text on the button
        screen.blit(self.text_surface, self.text_rect)

    def is_hovered(self, pos):
        return self.rect.collidepoint(pos)

    def click(self):
        print(f"Button '{self.text}' clicked!")

