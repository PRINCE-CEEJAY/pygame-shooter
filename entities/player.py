import pygame
from settings import *

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.velocity = pygame.Vector2(0, 0)
        self.on_ground = False

    def handle_input(self, input):
        self.velocity.x = 0

        if input.left:
            self.velocity.x = -PLAYER_SPEED
        if input.right:
            self.velocity.x = PLAYER_SPEED
        if input.jump and self.on_ground:
            self.velocity.y = -JUMP_FORCE
            self.on_ground = False

    def update(self, dt):
        self.rect.x += self.velocity.x * dt
        self.rect.y += self.velocity.y * dt

    def draw(self, screen):
        pygame.draw.rect(screen, (80, 200, 255), self.rect)
