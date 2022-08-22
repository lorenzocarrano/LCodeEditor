import fileViewer
from fileManager import FileManager
from tkinter import *
class Editor:
    def __init__(self):
        root = Tk()
        #root.overrideredirect(True)

        root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

        self.fViewerFrame = LabelFrame(root)
        self.fViewerFrame.grid(row=0, column=1, sticky="new")
        self.fViewer = fileViewer.FileViewer(self.fViewerFrame)
        self.fileMngr = FileManager(root, self.fViewer)
        self.fileMngr.grid(row=0, column=0, sticky="nw")
        filesList = self.fileMngr.getFilesList()
        #creating buttons
        for file in filesList:
            fileBtn = Button(self.fileMngr.interior, text=file, font=("Helvetica",10))
            fileBtn.configure(command=lambda btn = fileBtn: self.openFile(btn))
            fileBtn.pack(anchor="w")
            #fileButtonsList.append(fileBtn) variable deleted
        root.mainloop()

    def openFile(self, button):
        path = button["text"]
        try:
            f = open(path, "r")
            data = f.read()
            self.fViewer.attachFile(path, data)
        except Exception as e:
            print(e)
            return


