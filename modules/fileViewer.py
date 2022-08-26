from tkinter import *
import tkinter.font as tkfont
class FileViewer(Text):
    def __init__(self, *args, **kw):
        Text.__init__(self, *args, **kw)
        #set the tab character width
        font = tkfont.Font(font=self['font'])  # get font associated with Text widget
        tab_width = font.measure(' ' * 3)  # compute desired width of tabs
        self.config(tabs=(tab_width,))  # configure Text widget tab stops

        self.DisplayedFile = ""


    def attachFile(self, fPath, data):
        self.delete('1.0', END)
        self.insert('1.0', data)
        self.DisplayedFile = fPath

    def getDisplayedFile(self):
        return self.DisplayedFile
