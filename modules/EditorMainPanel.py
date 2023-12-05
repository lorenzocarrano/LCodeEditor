from tkinter import Frame
from tkinter import VERTICAL
from tkinter import BOTH
from tkinter import ttk
import sys
sys.path.insert(0, '../../modules')
sys.path.insert(1, '../../conf')
sys.path.insert(2, '../../modules/primitives')
sys.path.insert(2, '../../ThirdParty/TkTerm/tkterm')
from CodeViewer    import *
from TabsContainer import *
from TerminalPanel import *

class EditorMainPanel(Frame):
    def __init__(self, rootWindow, editorApp = None):
        Frame.__init__(self, rootWindow)

        self.editorApp = editorApp

        # change style to classic (Windows only)
        # to show the sash and handle
        self.style = ttk.Style()
        #style.theme_use('classic')

        # paned window
        self.pw = ttk.PanedWindow(self, orient=VERTICAL)

        # Left listbox
        self.TabsContainerObject = TabsContainer(self, self.editorApp)
        #self.cViewer = CodeViewer()
        #self.TabsContainerObject.add(self.cViewer, text="new")
        self.TabsContainerObject.pack(side=LEFT)
        self.pw.add(self.TabsContainerObject)

        # Right listbox
        self.terminalPanel = TerminalPanel(self)
        self.terminalPanel.pack(side=LEFT)
        self.pw.add(self.terminalPanel)

        # place the panedwindow on the root window
        self.pw.pack(fill=BOTH, expand=True)

    # TabsContainer methods interface
    def add(self, widget, text):
        self.TabsContainerObject.add(widget, text=text)

        lastAddedTabIndex = self.TabsContainerObject.index('end') - 1
        self.TabsContainerObject.select(lastAddedTabIndex)

    def removeTab(self, forceRemove=False):
        return self.TabsContainerObject.removeTab(forceRemove)

    def getActiveTabText(self):
        return self.TabsContainerObject.getActiveTabText()

    def getActiveTabID(self):
        return self.TabsContainerObject.index('current')

    def setActiveTabByID(self, tabID):
        self.TabsContainerObject.select(tabID)

    def removeTabRequestedFromExternalEvent(self):
        self.TabsContainerObject.removeTabRequestedFromExternalEvent()

    def atLeastOneFileModified(self):
        return self.TabsContainerObject.atLeastOneFileModified()

    def isFileBeingClosedModified(self):
        return self.TabsContainerObject.isFileBeingClosedModified()

    def saveContentOfModifiedFiles(self):
        self.TabsContainerObject.saveContentOfModifiedFiles()

    def saveClosingFileContent(self):
        self.TabsContainerObject.saveClosingFileContent()

    def saveCurrentFileContent(self):
        self.TabsContainerObject.saveCurrentFileContent()

    def saveAllOpenedFiles(self):
        self.TabsContainerObject.saveAllOpenedFiles()

    def searchPatternInCurrentFile(self, pattern):
        self.TabsContainerObject.searchPatternInCurrentFile(pattern)

    def searchPatternInOpenedFiles(self, pattern):
        self.TabsContainerObject.searchPatternInOpenedFiles(pattern)
    # #################################################

