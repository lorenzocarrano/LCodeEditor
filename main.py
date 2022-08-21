import sys
sys.path.insert(0, './modules')
import fileViewer
import fileManager
from CodeEditor import Editor
from tkinter import *

def main():
    root = Tk()

    #root.overrideredirect(True)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    Frame1 = LabelFrame(root)
    Frame1.pack(side=LEFT, fill='y', anchor="e")
    Frame2 = LabelFrame(root)
    Frame2.pack(side=RIGHT, fill='both', anchor="center")
    fManager = fileManager.FileManager(Frame1)
    fViewer = fileViewer.FileViewer(Frame2)
    root.mainloop()

if __name__ == "__main__":
    main()
