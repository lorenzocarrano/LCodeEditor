from tkinter import *
import os
import editortheme as et
class TerminalPanel(Canvas):
    def __init__(self, *args, **kwargs):
        Canvas.__init__(self, *args, **kwargs)
        wid = self.winfo_id()
        cmd = 'xterm -into %d -fn *-fixed-*-*-*-20-* -geometry 300x30 -bg ' %wid #set font and window frame
        cmd = cmd + et.SelectedTheme["TerminalBG"] #set background
        cmd = cmd + ' -fg ' + et.SelectedTheme["TerminalFG"] #set foreground
        cmd = cmd + ' -sb &'
        os.system(cmd)


if __name__ == "__main__":
    root = Tk()

    root.geometry("900x300")
    tp = TerminalPanel(root)
    tp.pack(side=BOTTOM, expand=True, fill=BOTH)

    root.mainloop()
