import sys
sys.path.insert(0, './modules')
sys.path.insert(1, './conf')
from tkinter import *
from CodeEditor import Editor
import editortheme as et

def main():
    root = Tk()
    #root.overrideredirect(True)

    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.configure(bg=et.SelectedTheme["MainWindowBG"])

    Editor(root, "./")
    root.mainloop()

if __name__ == "__main__":
    main()
