import sys
sys.path.insert(0, './modules')
from tkinter import *
from CodeEditor import Editor

def main():
    root = Tk()
    #root.overrideredirect(True)

    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

    Editor(root, "./")
    root.mainloop()

if __name__ == "__main__":
    main()
