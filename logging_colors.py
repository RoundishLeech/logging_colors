# 
# Modified from https://stackoverflow.com/a/1336640 by Chris Regan with assistance from ChatGPT 3.5


import logging
import platform
import ctypes

# Define constants for text and background colors
FOREGROUND_BLUE = 0x0001
FOREGROUND_GREEN = 0x0002
FOREGROUND_RED = 0x0004
FOREGROUND_INTENSITY = 0x0008
FOREGROUND_YELLOW = 0x0006
FOREGROUND_WHITE = FOREGROUND_BLUE | FOREGROUND_GREEN | FOREGROUND_RED

BACKGROUND_YELLOW = 0x0060
BACKGROUND_INTENSITY = 0x0080

class CustomStreamHandler(logging.StreamHandler):
    def _out_handle(self):
        return ctypes.windll.kernel32.GetStdHandle(self.STD_OUTPUT_HANDLE)
    
    def _set_color(self, code):
        hdl = self._out_handle()
        ctypes.windll.kernel32.SetConsoleTextAttribute(hdl, code)

def add_coloring_to_emit_windows(fn):
    def new(*args):
        levelno = args[1].levelno
        if levelno >= 50:
            color = BACKGROUND_YELLOW | FOREGROUND_RED | FOREGROUND_INTENSITY | BACKGROUND_INTENSITY
        elif levelno >= 40:
            color = FOREGROUND_RED | FOREGROUND_INTENSITY
        elif levelno >= 30:
            color = FOREGROUND_YELLOW | FOREGROUND_INTENSITY
        elif levelno >= 20:
            color = FOREGROUND_GREEN
        elif levelno >= 10:
            color = FOREGROUND_MAGENTA
        else:
            color = FOREGROUND_WHITE
        args[0]._set_color(color)
        ret = fn(*args)
        args[0]._set_color(FOREGROUND_WHITE)
        return ret
    return new

def add_coloring_to_emit_ansi(fn):
    def new(*args):
        levelno = args[1].levelno
        if levelno >= 50:
            color = '\x1b[31m'  # red
        elif levelno >= 40:
            color = '\x1b[31m'  # red
        elif levelno >= 30:
            color = '\x1b[33m'  # yellow
        elif levelno >= 20:
            color = '\x1b[32m'  # green
        elif levelno >= 10:
            color = '\x1b[35m'  # pink
        else:
            color = '\x1b[0m'  # normal
        args[1].msg = color + args[1].msg + '\x1b[0m'  # normal
        return fn(*args)
    return new

logger = logging.getLogger('text-generation-webui')
logger.setLevel(logging.DEBUG)

# Directly sets the handler for the logger to an instance of 
# CustomStreamHandler for Windows systems and adds it to the logger
if platform.system() == 'Windows':
    handler = CustomStreamHandler()
    handler.STD_OUTPUT_HANDLE = -11
    logger.addHandler(handler)
    logger.addHandler(logging.StreamHandler())  # Adds a default handler as well if needed
else:
    handler = logging.StreamHandler()
    logger.addHandler(add_coloring_to_emit_ansi(handler))
