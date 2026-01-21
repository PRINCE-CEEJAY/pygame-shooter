import pygame

class InputManager:
    def __init__(self):
        self.left = self.right = self.jump = False
        self.quit = False

    def update(self):
        self.left = self.right = self.jump = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.left = True
                if event.key == pygame.K_RIGHT:
                    self.right = True
                if event.key == pygame.K_SPACE:
                    self.jump = True
