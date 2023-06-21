import sys
sys.path.insert(0, '/home/lorenzo/src/PythonApps/CodeEditor')
sys.path.insert(1, '/home/lorenzo/src/PythonApps/CodeEditor/modules')
sys.path.insert(2, '/home/lorenzo/src/PythonApps/CodeEditor/modules/primitives')
sys.path.insert(3, '/home/lorenzo/src/PythonApps/CodeEditor/conf')
sys.path.insert(4, '/home/lorenzo/src/PythonApps/CodeEditor/ThirdParty/TkTerm/tkterm')

from tkinter import *
from CodeEditor import Editor
import editortheme as et
from tkinter import filedialog

def main():
    if len(sys.argv) == 1:
        pathToStart = '.'
    elif len(sys.argv) == 2:
        if sys.argv[1] == '-O':
            #Open file browser and chose a path?
            pathToStart = filedialog.askdirectory()
        else:
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
