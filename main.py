import sys
sys.path.insert(0, './modules')
sys.path.insert(1, './modules/primitives')
sys.path.insert(2, './conf')
from tkinter import *
from CodeEditor import Editor
import editortheme as et

def main():
    if len(sys.argv) == 1:
        pathToStart = '.'
    elif len(sys.argv) == 2:
        if sys.argv[1] == '-O':
            #Open file browser and chose a path?
            return
        pathToStart = sys.argv[1]
    else:
        print('uncorrect parameters number')
        return
    root = Tk()
    #root.overrideredirect(True)

    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.configure(bg=et.SelectedTheme["MainWindowBG"])

    Editor(root, pathToStart)
    root.mainloop()

if __name__ == "__main__":
    main()
