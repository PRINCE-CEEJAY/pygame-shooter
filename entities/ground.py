import pygame
from settings import *

class Ground:
    def __init__(self):
        self.rect = pygame.Rect(
            0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 50
        )

    def draw(self, screen):
        pygame.draw.rect(screen, (100, 100, 100), self.rect)
