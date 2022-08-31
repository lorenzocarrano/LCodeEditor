from CodeViewer import *
from FileManager import FileManager
from tkinter import *
from TabsContainer import *
from CascadeMenu import *
from YesNoPopupMessage import *
from EntryPanel import *
from TerminalPanel import TerminalPanel
import os
import filecmp
#from StdOutManager import StdOutManager

class Editor:
    def __init__(self, root, workingPath):
        self.terminalPanel = TerminalPanel(root)
        self.terminalPanel.pack(side=BOTTOM, expand=True, fill=BOTH, anchor=S+W)
        self.terminalShown = True
        self.TabsContainerObject = TabsContainer(root, editorApp=self)
        self.TabsContainerObject.pack(side=RIGHT, anchor=N, expand=True, fill=BOTH)
        self.fileMngr = FileManager(root, workingPath, self)
        self.fileMngr.pack(side=LEFT, anchor=N)
        self.fManagerShown = True
        self.workingPath = workingPath
        #self.topMenu = CascadeMenu(root, ["Open"], [self.openFile("")])
        #bind keys
        root.bind('<Escape>', self.closeCurrentFile)
        root.bind("<Control-s>", self._save)
        root.bind("<Control-Shift-S>", self._saveAll)
        #bind on close window event
        root.protocol("WM_DELETE_WINDOW", self.onClosingWindow)
        root.bind("<Control-Shift-Q>", self.onClosingWindowByKeyword)
        #bind find pattern event
        root.bind("<Control-f>", self.onSearchPattern)
        #bind show/hide terminal
        root.bind("<Control-Shift-T>", self.onTerminalShowHide)
        #bind show/hide FileManager panel
        root.bind("<Control-Shift-M>", self.onFileManagerShowHide)
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
        #stdoutMngr = StdOutManager()
        #stdoutMngr.stdoutPrint(data="CodeEditor: closeFile REQUESTED", endCharacter="\n")
        self.FileBeingClosed = path
        mod = self.fileModified()
        #stdoutMngr.stdoutPrint(data=mod, endCharacter="\n")
        if self.fileModified() == True:
            top = YesNoPopupMessage(containerWidget=self.ContainerWindow, linkedWidget=self, closeCallback=self.CloseFile, message="Save changes to file?")
        else:
            #stdoutMngr.stdoutPrint(data="CloseFileRequested --> CodeEditor: no save", endCharacter="\n")
            self.CloseFile(False)

    def CloseFile(self, save):
        #stdoutMngr = StdOutManager()
        try:
            #stdoutMngr.stdoutPrint(data="CodeEditor: CloseFile --> try", endCharacter="\n")
            flag = self.TabsContainerObject.removeTab()
        except:
            #stdoutMngr.stdoutPrint(data="CodeEditor: CloseFile --> except", endCharacter="\n")
            return
        if save == True:
            #stdoutMngr.stdoutPrint(data="CodeEditor: CloseFile --> save", endCharacter="\n")
            cmd = "cat " + self.FileBeingClosed + ".bak > " + self.FileBeingClosed
            os.system(cmd)

        if flag == True:
            #stdoutMngr.stdoutPrint(data="CodeEditor: CloseFile --> removing bak file", endCharacter="\n")
            cmd = "rm " + self.FileBeingClosed + ".bak"
            os.system(cmd)
            self.openedFiles.remove(self.FileBeingClosed)


    def closeCurrentFile(self, event):
        pass

    def onClosingWindow(self):
        if self.atLeastOneFileModified():
            top = YesNoPopupMessage(containerWidget=self.ContainerWindow, linkedWidget=self, closeCallback=self.closeSavingAllFiles, message="Some files modified. Save changes?")
        else:
            self.closeSavingAllFiles(False)

    def onClosingWindowByKeyword(self, event):
        if self.atLeastOneFileModified():
            top = YesNoPopupMessage(containerWidget=self.ContainerWindow, linkedWidget=self, closeCallback=self.closeSavingAllFiles, message="Some files modified. Save changes?")
        else:
            self.closeSavingAllFiles(False)

    def closeSavingAllFiles(self, save):
        if save == False:
            for file in self.openedFiles:
                cmd = "rm " + file + ".bak"
                os.system(cmd)
            self.ContainerWindow.destroy()
        else:
            for file in self.openedFiles:
                #saving the content of .bak file in original one
                cmd = "cat " + file + ".bak > " + file
                os.system(cmd)

                #removing .bak file
                cmd = "rm " + file + ".bak"
                os.system(cmd)
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

    def atLeastOneFileModified(self):
        for file in self.openedFiles:
            f1Path = file #original file
            f2Path = file + ".bak" #.bak file to compare
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

    def onSearchPattern(self, event):
        #SearchWindow = EntryPanel(self.ContainerWindow, text1="Search in current file", text2="Search in all files   ", callback1=self.searchInCurrentFile, callback2=self.searchInOpenedFiles)
        textsList = ["Find in current file", "Find in opened files", "Find in all files   "]
        callbacksList = [self.searchInCurrentFile, self.searchInOpenedFiles, self.searchInAllFiles]
        SearchWindow = EntryPanel(containerWidget=self.ContainerWindow, name="Find", labels=textsList, callbacks=callbacksList)

    def searchInCurrentFile(self, pattern):
        self.TabsContainerObject.searchPatternInCurrentFile(pattern)

    def searchInOpenedFiles(self, pattern):
        self.TabsContainerObject.searchPatternInOpenedFiles(pattern)

    def searchInAllFiles(self, pattern):
        pass

    def _save(self, event=None):
        filePath = self.TabsContainerObject.getActiveTabText()
        #saving the content of .bak file in original one
        cmd = "cat " + filePath + ".bak > " + filePath
        os.system(cmd)

    def _saveAll(self, event):
        for filePath in self.openedFiles:
            cmd = "cat " + filePath + ".bak > " + filePath
            os.system(cmd)

    def onTerminalShowHide(self, event):
        #toggle the show/hide state for terminal panel
        if self.terminalShown == False:
            #first we remove everything from the screen
            self.fileMngr.pack_forget()
            self.TabsContainerObject.pack_forget()
            self.terminalPanel.pack(side=BOTTOM, expand=True, fill=BOTH, anchor=S+W)
            self.TabsContainerObject.pack(side=RIGHT, anchor=N, expand=True, fill=BOTH)
            if self.fManagerShown == True:
                self.fileMngr.pack(side=LEFT, anchor=N)
                self.fManagerShown = True
            self.terminalShown = True
        else:
            self.terminalPanel.pack_forget()
            self.terminalShown = False

    def onFileManagerShowHide(self, event):
        #toggle the show/hide state for terminal panel
        if self.fManagerShown == False:
            self.fileMngr.pack(side=LEFT, anchor=N)
            self.fManagerShown = True
        else:
            self.fileMngr.pack_forget()
            self.fManagerShown = False

    #def _innest_closingFileEvent(self, event):
        #filePath = self.TabsContainerObject.getActiveTabText()
        #self.TabsContainerObject.closeFileRequestByKeyboard(filePath)
