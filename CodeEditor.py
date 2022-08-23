import fileViewer
from fileManager import FileManager
from tkinter import *
from TabsContainer import *
class Editor:
    def __init__(self, root, workingPath):
        self.TabsContainerObject = TabsContainer()
        self.TabsContainerObject.pack(side=RIGHT, anchor=N, expand=True, fill=BOTH)
        self.fileMngr = FileManager(root)
        self.fileMngr.pack(side=LEFT, anchor=N)
        self.workingPath = workingPath
        filesList = self.fileMngr.getFilesList()
        #creating buttons
        for file in filesList:
            fileBtn = Button(self.fileMngr.interior, text=file, font=("Helvetica",10))
            fileBtn.configure(command=lambda btn = fileBtn: self.openFile(btn))
            fileBtn.pack(anchor="w")
            #fileButtonsList.append(fileBtn) variable deleted

    def openFile(self, button):
        path = button["text"]
        fViewer = fileViewer.FileViewer()
        try:
            f = open(path, "r")
            data = f.read()
            fViewer.attachFile(path, data)
            self.TabsContainerObject.add(fViewer, text=path)

        except Exception as e:
            print(e)
            return


