from CodeViewer import *
from FileManager import FileManager
from tkinter import *
from TabsContainer import *
from CascadeMenu import *
from YesNoPopupMessage import *
import os
import filecmp
from StdOutManager import StdOutManager

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
                return

    def CloseFileRequested(self, path):
        stdoutMngr = StdOutManager()
        stdoutMngr.stdoutPrint(data="CodeEditor: closeFile REQUESTED", endCharacter="\n")
        self.FileBeingClosed = path
        mod = self.fileModified()
        stdoutMngr.stdoutPrint(data=mod, endCharacter="\n")
        if self.fileModified() == True:
            top = YesNoPopupMessage(containerWidget=self.ContainerWindow, linkedWidget=self, closeCallback=self.CloseFile, message="Save changes to file?")
        else:
            stdoutMngr.stdoutPrint(data="CloseFileRequested --> CodeEditor: no save", endCharacter="\n")
            self.CloseFile(False)


    def CloseFile(self, save):
        stdoutMngr = StdOutManager()
        try:
            stdoutMngr.stdoutPrint(data="CodeEditor: CloseFile --> try", endCharacter="\n")
            self.TabsContainerObject.removeTab()
        except:
            stdoutMngr.stdoutPrint(data="CodeEditor: CloseFile --> except", endCharacter="\n")
            return
        if save == True:
            stdoutMngr.stdoutPrint(data="CodeEditor: CloseFile --> save", endCharacter="\n")
            cmd = "cat " + self.FileBeingClosed + ".bak > " + self.FileBeingClosed
            os.system(cmd)

        stdoutMngr.stdoutPrint(data="CodeEditor: CloseFile --> removing bak file", endCharacter="\n")
        cmd = "rm " + self.FileBeingClosed + ".bak"
        os.system(cmd)
        self.openedFiles.remove(self.FileBeingClosed)


    def insertInCommandBar(self, event):
        pass

    def onClosingWindow(self):
        self.ContainerWindow.destroy()

    def fileModified(self):
        #check if .bak file is equal to the original file
        f1Path = self.FileBeingClosed #original file
        f2Path = self.FileBeingClosed + ".bak" #.bak file to compare

        f = open(f1Path, "r")
        f1Lines = f.read().splitlines()
        f.close()
        f = open(f2Path, "r")
        f2Lines = f.read().splitlines()

        if len(f1Lines) != len(f2Lines):
            return True
        for i in range(len(f1Lines)):
            if f1Lines[i] != f2Lines[i]:
                return True
        return False

