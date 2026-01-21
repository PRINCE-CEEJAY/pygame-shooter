import pygame
from settings import *
from states.playing import PlayingState

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(
            (SCREEN_WIDTH, SCREEN_HEIGHT)
        )
        pygame.display.set_caption("SHOOTING MANIAC")
        self.clock = pygame.time.Clock()
        self.running = True

        self.state = PlayingState(self)

    def run(self):
        while self.running:
            dt = self.clock.tick(FPS) / 1000
            self.state.handle_events()
            self.state.update(dt)
            self.state.draw(self.screen)

        pygame.quit()
