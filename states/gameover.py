from core.state import GameState

class GameOverState(GameState):
    def __init__(self, game):
        self.game = game

    def handle_events(self):
        for event in __import__("pygame").event.get():
            if event.type == __import__("pygame").QUIT:
                self.game.running = False

    def update(self, dt):
        pass

    def draw(self, screen):
        screen.fill((0, 0, 0))
        __import__("pygame").display.flip()
