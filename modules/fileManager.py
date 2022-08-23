from tkinter import *
import os
import sys
from verticalScrolledFrame import VerticalScrolledFrame

class FileManager(VerticalScrolledFrame):
    def __init__(self, root, *args, **kw):
        VerticalScrolledFrame.__init__(self, root, *args, **kw)
        pathToStart = "./"
        self.filesList = []

        #filter files in subdirectories
        for root, dirs, files in os.walk(pathToStart):
            for file in files:
                Path = os.path.join(root, file)
                Path = Path[2:]
                if not Path.startswith(".git"):
                    self.filesList.append(Path)

    def getFilesList(self):
        return self.filesList
