from tkinter import *
import os
import sys
from verticalScrolledFrame import VerticalScrolledFrame

class FileManager(VerticalScrolledFrame):
    def __init__(self, root, fileViewerInstance, *args, **kw):
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

    def openFile(self, button):
        path = button["text"]
        try:
            f = open(path, "r")
            data = f.read()
            self.fileViewerInstance.attachFile(path, data)
        except Exception as e:
            print(e)
            return
