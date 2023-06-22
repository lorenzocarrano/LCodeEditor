from tkinter import *
import subprocess
import editortheme as et
import os
from tkterm import *
class TerminalPanel(Terminal):
    def __init__(self, parent, text=None, *args, **kwargs):

        super().__init__(parent, *args, **kwargs)

    def killProcess(self):
        # compatibility with older version with terminal widget different from tkterm
        return
