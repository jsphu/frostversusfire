from pygame import (K_DOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_SPACE, K_UP, KEYDOWN,
                    QUIT, K_q)

class EventHandler:
    def __init__(self, screen, game_state):
        self._screen = screen
        self._game_screen = game_state

    def pygame_quit(self):
        self._game_screen.running = False

    def key_bindings(self, key):
        if key == K_LEFT:
            self._game_screen.direction = "l"
        elif key == K_RIGHT:
            self._game_screen.direction = "r"
        elif key == K_UP:
            self._game_screen.direction = "u"
        elif key == K_DOWN:
            self._game_screen.direction = "d"

    def handle_events(self, event):
        if event.type == QUIT:
            self.pygame_quit()

        if event.type == KEYDOWN:
            self.key_bindings(event.key)
