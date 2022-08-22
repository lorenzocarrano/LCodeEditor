import fileViewer
import fileManager
from tkinter import *
class Editor:
    def __init__(self):
        root = Tk()
        #root.overrideredirect(True)
        fileButtonsList = []
        root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
        Frame1 = LabelFrame(root)
        Frame1.grid(row=0, column=0, sticky="ne")
        Frame2 = LabelFrame(root)
        Frame2.grid(row=0, column=1, sticky="new")
        fViewer = fileViewer.FileViewer(Frame2)
        fManager = fileManager.FileManager(Frame1, fileButtonsList, fViewer)
        root.mainloop()
