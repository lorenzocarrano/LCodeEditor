import sys
sys.path.insert(0, '../conf')
import editortheme as et
import tkinter as tk
from tkinter import ttk
from tkinter import font
from StdOutManager import StdOutManager

class TabsContainer(ttk.Notebook):
    """A ttk Notebook with close buttons on each tab"""

    __initialized = False

    def __init__(self, containerWidget, editorApp, *args, **kwargs):
        if not self.__initialized:
            self.__initialize_custom_style()
            self.__inititialized = True

        kwargs["style"] = "TabsContainer"
        ttk.Notebook.__init__(self, *args, **kwargs)
        #enable key bindings to navigate between tabs
        self.enable_traversal()
        self._active = None
        self.containerWidget = containerWidget
        self.editorApp = editorApp
        self.indexToEventuallyRemove = -1 #initValue
        self.tabWithModifiedFiles = []

        self.bind("<ButtonPress-1>", self.on_close_press, True)
        self.bind("<ButtonRelease-1>", self.on_close_release)

        ttk.Style().configure("TabsContainer", background=et.SelectedTheme["MainWindowBG"])

    def on_close_press(self, event):
        """Called when the button is pressed over the close button"""

        element = self.identify(event.x, event.y)

        if "close" in element:
            index = self.index("@%d,%d" % (event.x, event.y))
            self.state(['pressed'])
            self._active = index
            return "break"

    def on_close_release(self, event):
        """Called when the button is released"""
        if not self.instate(['pressed']):
            return

        element =  self.identify(event.x, event.y)
        if "close" not in element:
            # user moved the mouse off of the close button
            return

        index = self.index("@%d,%d" % (event.x, event.y))
        self.indexToEventuallyRemove = index
        fileBeingClosed = self.tab(index)["text"]
        self.editorApp.CloseFileRequested(fileBeingClosed)

    def removeTab(self):
        flag = False #flag becomes true if the tab is correctly removed
        #stdoutMngr = StdOutManager()
        #stdoutMngr.stdoutPrint(data="TabsContainer: removeTab invoked", endCharacter="\n")
        index = self.indexToEventuallyRemove
        if self._active == index:
            #stdoutMngr.stdoutPrint(data="TabsContainer: removeTab --> removed", endCharacter="\n")
            self.forget(index)
            self.event_generate("<<NotebookTabClosed>>")
            flag = True

        #stdoutMngr.stdoutPrint(data="TabsContainer: removeTab --> change state and active", endCharacter="\n")
        self.state(["!pressed"])
        self._active = None
        return flag

    def getActiveTabText(self):
         return self.tab(self.select())["text"]

    def atLeastOneFileModified(self):
        self.tabWithModifiedFiles = []
        if len(self.tabs()) == 0:
            return False
        for tabName in self.tabs():
            activeObject = self.nametowidget(tabName) #retrieve widget inside active tab
            if activeObject.getModifyFlag() == True:
                self.tabWithModifiedFiles.append(tabName)
        return len(self.tabWithModifiedFiles) > 0

    def isFileBeingClosedModified(self):
        activeObject = self.nametowidget(self.tabs()[self.indexToEventuallyRemove])
        return activeObject.getModifyFlag()

    def saveContentOfModifiedFiles(self):
        for tabName in self.tabWithModifiedFiles:
            activeObject = self.nametowidget(tabName)
            if activeObject.getModifyFlag == True:
                activeObject.saveContent()

        #list is empted
        self.tabWithModifiedFiles = []

    def saveClosingFileContent(self):
        activeObject = self.nametowidget(self.tabs()[self.indexToEventuallyRemove])
        activeObject.saveContent()

    def saveCurrentFileContent(self):
        activeObject = self.nametowidget(self.tabs()[self.index("current")])
        activeObject.saveContent()

    def saveAllOpenedFiles(self):
        for tabName in self.tabs():
            activeObject = self.nametowidget(tabName)
            activeObject.saveContent()

    def searchPatternInCurrentFile(self, pattern):
        activeObject = self.nametowidget(self.select()) #retrieve widget inside active tab
        activeObject.searchPattern(pattern)

    def searchPatternInOpenedFiles(self, pattern):
        for tabName in self.tabs():
            activeObject = self.nametowidget(tabName) #retrieve widget inside active tab
            activeObject.getPatternOccurrencies(pattern)

    def __initialize_custom_style(self):
        style = ttk.Style()
        self.images = (
            tk.PhotoImage("img_close", data='''
                R0lGODlhCAAIAMIBAAAAADs7O4+Pj9nZ2Ts7Ozs7Ozs7Ozs7OyH+EUNyZWF0ZWQg
                d2l0aCBHSU1QACH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU
                5kEJADs=
                '''),
            tk.PhotoImage("img_closeactive", data='''
                R0lGODlhCAAIAMIEAAAAAP/SAP/bNNnZ2cbGxsbGxsbGxsbGxiH5BAEKAAQALAAA
                AAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU5kEJADs=
                '''),
            tk.PhotoImage("img_closepressed", data='''
                R0lGODlhCAAIAMIEAAAAAOUqKv9mZtnZ2Ts7Ozs7Ozs7Ozs7OyH+EUNyZWF0ZWQg
                d2l0aCBHSU1QACH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU
                5kEJADs=
            ''')
        )

        style.element_create("close", "image", "img_close",
                            ("active", "pressed", "!disabled", "img_closepressed"),
                            ("active", "!disabled", "img_closeactive"), border=8, sticky='')
        style.layout("TabsContainer", [("TabsContainer.client", {"sticky": "nswe"})])
        style.layout("TabsContainer.Tab", [
            ("TabsContainer.tab", {
                "sticky": "nswe",
                "children": [
                    ("TabsContainer.padding", {
                        "side": "top",
                        "sticky": "nswe",
                        "children": [
                            ("TabsContainer.focus", {
                                "side": "top",
                                "sticky": "nswe",
                                "children": [
                                    ("TabsContainer.label", {"side": "left", "sticky": ''}),
                                    ("TabsContainer.close", {"side": "left", "sticky": ''}),
                                ]
                        })
                    ]
                })
            ]
        })
    ])

        style.configure("TabsContainer.Tab", background=et.SelectedTheme["TabsBG"], foreground=et.SelectedTheme["TabsFG"], font=et.SelectedTheme["TabsFONT"])
        #print(style.lookup("TabsContainer.Tab", "font")) to print currently set font in syle
'''
if __name__ == "__main__":
    root = tk.Tk()

    notebook = TabsContainer(width=2000, height=2000)
    notebook.pack(side="top", fill="both", expand=True)

    for color in ("red", "orange", "green", "blue", "violet"):
        frame = tk.Text(notebook, background=color)
        notebook.add(frame, text=color)

    root.mainloop()
'''
