import pygame

from src.config import (SCREEN_WIDTH, SCREEN_HEIGHT, Colors)
from src.control.events import EventHandler
from src.control.states import GameState
from src.args import Args

class Main:
    def __init__(self):
        pygame.init()
        self.flags = Args()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags=self.flags.HEAD)
        pygame.display.set_caption("FrostVersusFire")
        self.state = GameState()
        self.events = EventHandler(self.screen, self.state)

    def main(self):
        clock = pygame.time.Clock()
        dt = None

        while self.state.running:
            self.state.current_time = pygame.time.get_ticks()

            for event in pygame.event.get():
                self.events.handle_events(event)

            self.screen.fill(Colors.WHITE)

            pygame.display.flip()

            dt = clock.tick(self.state.fps)
            dt /= 100

        pygame.quit()
