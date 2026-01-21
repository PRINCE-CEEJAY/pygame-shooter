import pygame
from settings import *
from systems.collision import Collision
from systems.physics import Physics

class Enemy:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.velocity = pygame.Vector2(150, 0)  # horizontal patrol speed
        self.on_ground = False

    def update(self, dt):
        # Player
        self.player.handle_input(self.input)
        Physics.apply_gravity(self.player, dt)
        self.player.update(dt)
        Collision.player_ground(self.player, self.ground)

        # Enemy
        Physics.apply_gravity(self.enemy, dt)
        self.enemy.update(dt)
        Collision.player_ground(self.enemy, self.ground)

        # Player ↔ Enemy collision
        if Collision.player_enemy(self.player, self.enemy):
            from states.gameover import GameOverState
            self.game.state = GameOverState(self.game)

        # Player falls off screen
        if self.player.rect.top > SCREEN_HEIGHT:
            from states.gameover import GameOverState
            self.game.state = GameOverState(self.game)



    def draw(self, screen):
        pygame.draw.rect(screen, (220, 60, 60), self.rect)
