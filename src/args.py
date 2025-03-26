from sys import argv as ARGS
import pygame

class Args:
    def __init__(self):
        args=""

        for arg in ARGS[1:]:
            if "-" in arg:
                arg = arg.strip("-")

            if "help" in arg.lower():
                print("HELP     \trunning options listed below.\n"
        "FULLSCREEN \tcreate a fullscreen display\n"
        "DOUBLEBUF  \tonly applicable with OPENGL\n"
        "HWSURFACE  \thardware accelerated, only in FULLSCREEN\n"
        "OPENGL     \tcreate an OpenGL-renderable display\n"
        "RESIZABLE  \tdisplay window should be sizeable\n"
        "NOFRAME    \tdisplay window will have no border or controls\n"
        "SCALED     \tresolution depends on desktop size and scale graphics\n"
        "SHOWN      \twindow is opened in visible mode (default)\n"
        "HIDDEN     \twindow is opened in hidden mode")
                exit()

            args += f" pygame.{arg.upper()} |"

        args = args[:-1] if args != "" else 0

        exec(f"self.HEAD ={args}")
