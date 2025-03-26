from sys import argv as ARGS
import pygame

class Args:
    def __init__(self):
        self.HEAD = 0

        arguments = []
        if   "--noframe" in ARGS:
            arguments.append("pygame.NOFRAME")

        elif "--resizable" in ARGS:
            arguments.append("pygame.RESIZABLE")

        elif "--scaled" in ARGS:
            arguments.append("pygame.SCALED")

        elif "--fullscreen" in ARGS:
            arguments.append("pygame.FULLSCREEN")

        if len(arguments) > 0:

            args = ""
            for arg in arguments:
                args += str(arg) + " | "

            args = args[:-3]

            exec(f"self.HEAD = {args}")

