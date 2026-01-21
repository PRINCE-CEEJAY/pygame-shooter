from core.state import GameState
from systems.input import InputManager
from systems.physics import Physics
from systems.collision import Collision
from entities.player import Player
from entities.enemy import Enemy
from entities.ground import Ground
from settings import *

class PlayingState(GameState):
    def __init__(self, game):
        self.game = game
        self.input = InputManager()
        self.player = Player(400, 200)
        self.enemy = Enemy(200, 200)
        self.ground = Ground()

    def handle_events(self):
        self.input.update()
        if self.input.quit:
            self.game.running = False

    def update(self, dt):
        self.player.handle_input(self.input)
        Physics.apply_gravity(self.player, dt)
        self.player.update(dt)
        Collision.player_ground(self.player, self.ground)

        if self.player.rect.top > SCREEN_HEIGHT:
            from states.gameover import GameOverState
            self.game.state = GameOverState(self.game)

    def draw(self, screen):
        screen.fill((30, 30, 30))
        self.ground.draw(screen)
        self.enemy.draw(screen)
        self.player.draw(screen)

        import pygame
        pygame.display.flip()

