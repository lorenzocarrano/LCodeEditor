from CodeViewer import *
from FileManager import FileManager
from tkinter import *
from TabsContainer import *
from CascadeMenu import *
from YesNoPopupMessage import *
from EntryPanel import *
from TerminalPanel import TerminalPanel
from EditorMainPanel import EditorMainPanel
import os
import filecmp
#from StdOutManager import StdOutManager

class Editor:
    def __init__(self, root, workingPath):
        #the order in which widgets are instantiated is important to display them in a correct manner
        self.fileMngr = FileManager(root, workingPath, self)
        self.fileMngr.pack(side=LEFT, anchor=N)
        self.editorMainPanel = EditorMainPanel(root, editorApp=self)
        self.editorMainPanel.pack(fill=BOTH, expand=True)
        self.terminalShown = True
        self.fManagerShown = True
        self.findPanelShown = False
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
        #bind show/hide FileManager panel
        root.bind("<Control-Shift-M>", self.onFileManagerShowHide)
        self.ContainerWindow = root
        self.openedFiles = []
        self.FileBeingClosedTABName = "" #init
        self.SearchWindow = None #init
        self.ForceCloseTab = False #init

    def _ExtractFileName(self, fileFullPath):
        fileNameIndexBeforeStart = fileFullPath.rfind('/')
        if fileNameIndexBeforeStart < 0:
            return fileFullPath
        else:
            return fileFullPath[fileNameIndexBeforeStart+1:]

    def openFile(self, path):
        if path not in self.openedFiles:
            try:
                f = open(path, "r")
                data = f.read()
                cViewer = CodeViewer()
                cViewer.attachFile(path, data)
                fileName = self._ExtractFileName(path)
                self.editorMainPanel.add(cViewer, text=fileName)
                tabName = self.editorMainPanel.getActiveTabName()
                self.openedFiles.append((tabName, path))
            except Exception as e:
                print("error", e)
                return

        # next line should not be reached
        return None
    def CloseFileRequested(self, tabName):
        #stdoutMngr = StdOutManager()
        #stdoutMngr.stdoutPrint(data="CodeEditor: closeFile REQUESTED", endCharacter="\n")
        self.FileBeingClosedTABName = tabName
        #mod = self.fileModified()
        #stdoutMngr.stdoutPrint(data=mod, endCharacter="\n")
        if self.fileModified() == True:
            top = YesNoPopupMessage(containerWidget=self.ContainerWindow, linkedWidget=self, closeCallback=self.CloseFile, message="Save changes to file?")
        else:
            #stdoutMngr.stdoutPrint(data="CloseFileRequested --> CodeEditor: no save", endCharacter="\n")
            self.CloseFile(False)

    def CloseFile(self, save):
        #stdoutMngr = StdOutManager()
        if save == True:
            self.editorMainPanel.saveClosingFileContent()
        try:
            #stdoutMngr.stdoutPrint(data="CodeEditor: CloseFile --> try", endCharacter="\n")
            flag = self.editorMainPanel.removeTab(forceRemove=self.ForceCloseTab)
        except:
            #stdoutMngr.stdoutPrint(data="CodeEditor: CloseFile --> except", endCharacter="\n")
            return
        self.ForceCloseTab = False

        if flag == True:
            fileDescIndex = self.getFileDescIndexByTabName(self.FileBeingClosedTABName)
            if fileDescIndex >= 0:
                del self.openedFiles[fileDescIndex]

    def closeCurrentFile(self, event):
        self.ForceCloseTab = True
        self.editorMainPanel.removeTabRequestedFromExternalEvent()

    def getFileDescIndexByTabName(self, tabName):
        # since tabName is unique, the resulting list of indexes will always be composed of one element
        # for this reason just the first element is returned, being the unique index for the file being closed.
        print(self.openedFiles)
        l = [x for x, y in enumerate(self.openedFiles) if y[0] == tabName]
        if len(l) == 1:
            return l[0]
        else:
            return -1

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
        if save == True:
            self.editorMainPanel.saveContentOfModifiedFiles()

        #close App
        self.ContainerWindow.destroy()

    def fileModified(self):
        return self.editorMainPanel.isFileBeingClosedModified()

    def atLeastOneFileModified(self):
        return self.editorMainPanel.atLeastOneFileModified()

    def onSearchPattern(self, event):
        if self.findPanelShown == False:
            textsList = ["Find in current file", "Find in opened files", "Find in all files   "]
            callbacksList = [self.searchInCurrentFile, self.searchInOpenedFiles, self.searchInAllFiles]
            self.SearchWindow = EntryPanel(containerWidget=self.ContainerWindow, name="Find", labels=textsList, callbacks=callbacksList, onClosingCallback=self.findPanelClosed)
            self.findPanelShown = True
        else:
            self.SearchWindow.focus()

    def searchInCurrentFile(self, pattern):
        print("currFile search")
        self.editorMainPanel.searchPatternInCurrentFile(pattern)

    def searchInOpenedFiles(self, pattern):
        print("openedFiles search")
        self.editorMainPanel.searchPatternInOpenedFiles(pattern)

    def searchInAllFiles(self, pattern):
        print("allFiles search")
        pass

    def _save(self, event=None):
        self.editorMainPanel.saveCurrentFileContent()

    def _saveAll(self, event):
        self.editorMainPanel.saveAllOpenedFiles()

    def onFileManagerShowHide(self, event):
        #toggle the show/hide state for terminal panel
        if self.fManagerShown == False:
            self.fileMngr.pack(side=LEFT, anchor=N)
            self.editorMainPanel.pack_forget()
            self.editorMainPanel.pack(fill=BOTH, expand=True)
            self.fManagerShown = True
        else:
            self.fileMngr.pack_forget()
            self.fManagerShown = False

    def findPanelClosed(self):
        self.findPanelShown = False

    #def _innest_closingFileEvent(self, event):
        #filePath = self.editorMainPanel.getActiveTabText()
        #self.editorMainPanel.closeFileRequestByKeyboard(filePath)
