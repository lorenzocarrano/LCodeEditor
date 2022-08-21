from tkinter import *
import os
import sys
class FileManager:
    def __init__(self, rootWidget):
        #rootWidget.
        #root.winfo_screenwidth()
        pathToStart = "./"
        yScrollBar = Scrollbar(rootWidget, orient="vertical")
        yScrollBar.pack(side=RIGHT, fill='y')
        filesList = []
        for root, dirs, files in os.walk(pathToStart):
            for file in files:
                filesList.append(os.path.join(root, file))

        for file in filesList:
            fileBtn = Button(rootWidget, text=file, font=("Helvetica",10))
            fileBtn.configure(command=lambda btn = fileBtn: openFile(btn))
            fileBtn.pack(anchor="w")

    def openFile(self, button):
        pass
