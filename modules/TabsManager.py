import tkinter as tk
from tkinter import ttk

class TabsManager(ttk.Notebook):
    def __init__(self, *args, **kwargs):
        ttk.Notebook.__init__(self, *args, **kwargs)
    def addTabElement(self, elementToEmbed, elementText):
        #elementToEmbed will be the
