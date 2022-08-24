from tkinter import *
from tkinter import filedialog
import re

class CascadeMenu(Frame):
    def __init__(self, top, commandLabelsList, callbacksList):
        Frame.__init__(self, top)

        menu = Menu(top)
        top.config(menu=menu)
        self.file_menu = Menu(menu)
        menu.add_cascade(label="File", menu=self.file_menu)
        try:
            for i in range(len(commandLabelsList)):
                self.file_menu.add_command(label=commandLabelsList[i], command=callbacksList[i])
        except:
            pass

        #self.listNodes = Listbox(top, height=1, width=5)
        #self.listNodes.pack(side=LEFT, fill=Y, expand=True)

        #self.scrollbar = Scrollbar(top, orient="vertical")
        #self.scrollbar.config(command=self.listNodes.yview)
        #self.scrollbar.pack(side=RIGHT, fill=Y, expand=True)

        #self.listNodes.config(yscrollcommand=self.scrollbar.set)
