from CodeViewer import *
from FileManager import FileManager
from tkinter import *
from TabsContainer import *
from CascadeMenu import *
from YesNoPopupMessage import *
import os

class Editor:
    def __init__(self, root, workingPath):
        self.TabsContainerObject = TabsContainer(self)
        self.TabsContainerObject.pack(side=RIGHT, anchor=N, expand=True, fill=BOTH)
        self.fileMngr = FileManager(root, "./", self)
        self.fileMngr.pack(side=LEFT, anchor=N)
        self.workingPath = workingPath
        #self.topMenu = CascadeMenu(root, ["Open"], [self.openFile("")])
        #bind keys
        root.bind('<Escape>', self.insertInCommandBar)
        #bind on close window event
        root.protocol("WM_DELETE_WINDOW", self.onClosingWindow)
        self.ContainerWindow = root
        self.openedFiles = []
        self.FileBeingClosed = "" #init

    def openFile(self, path):
        if path not in self.openedFiles:
            try:
                f = open(path, "r")
                data = f.read()
                cViewer = CodeViewer()
                cViewer.attachFile(path, data)
                self.TabsContainerObject.add(cViewer, text=path)
                self.openedFiles.append(path)
            except Exception as e:
                print(e)
                return

    def CloseFileRequested(self, path):
        self.FileBeingClosed = path
        top = YesNoPopupMessage(containerWidget=self.ContainerWindow, linkedWidget=self, closeCallback=self.CloseFile, message="Save changes to file?")


    def CloseFile(self, save):
        try:
            self.TabsContainerObject.removeTab()
        except:
            return
        if save == True:
            cmd = "cat " + self.FileBeingClosed + ".bak > " + self.FileBeingClosed
            os.system(cmd)

        cmd = "rm " + self.FileBeingClosed + ".bak"
        os.system(cmd)
        self.openedFiles.remove(self.FileBeingClosed)


    def insertInCommandBar(self, event):
        print("escape pressed")

    def onClosingWindow(self):
        print("quit")
        self.ContainerWindow.destroy()
