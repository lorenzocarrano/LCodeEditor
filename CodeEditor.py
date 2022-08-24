from CodeViewer import *
from FileManager import FileManager
from tkinter import *
from TabsContainer import *
class Editor:
    def __init__(self, root, workingPath):
        self.TabsContainerObject = TabsContainer()
        self.TabsContainerObject.pack(side=RIGHT, anchor=N, expand=True, fill=BOTH)
        self.fileMngr = FileManager(root, "./", self)
        self.fileMngr.pack(side=LEFT, anchor=N)
        self.workingPath = workingPath

    def openFile(self, path):
        try:
            f = open(path, "r")
            data = f.read()
            cViewer = CodeViewer()
            cViewer.attachFile(path, data)
            self.TabsContainerObject.add(cViewer, text=path)
        except Exception as e:
            print(e)
            return
