from tkinter import *
class FileViewer(Text):
    def __init__(self):
        Text.__init__(self)

        self.currentlyOpenedFile = ""

    def attachFile(self, fPath, data):
        self.delete('1.0', END)
        self.insert('1.0', data)
        self.currentlyOpenedFile = fPath





