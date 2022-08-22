from tkinter import *
import os
import sys
class FileManager:
    def __init__(self, rootWidget, fileButtonsList, fileViewerInstance):
        #rootWidget.
        #root.winfo_screenwidth()
        self.fileViewerInstance = fileViewerInstance
        pathToStart = "./"
        yScrollBar = Scrollbar(rootWidget, orient="vertical")
        yScrollBar.pack(side=RIGHT, fill='y')
        filesList = []
        for root, dirs, files in os.walk(pathToStart):
            for file in files:
                Path = os.path.join(root, file)
                Path = Path[2:]
                if not Path.startswith(".git"):
                    filesList.append(Path)

        for file in filesList:
            fileBtn = Button(rootWidget, text=file, font=("Helvetica",10))
            fileBtn.configure(command=lambda btn = fileBtn: self.openFile(btn))
            fileBtn.pack(anchor="w")

            fileButtonsList.append(fileBtn)

    def openFile(self, button):
        path = button["text"]
        try:
            f = open(path, "r")
            data = f.read()
            self.fileViewerInstance.attachFile(path, data)
        except Exception as e:
            print(e)
            return
