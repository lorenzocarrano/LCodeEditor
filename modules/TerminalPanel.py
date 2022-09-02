from tkinter import *
import subprocess
import editortheme as et
import os

class TerminalPanel(Canvas):
    def __init__(self, *args, **kwargs):
        Canvas.__init__(self, *args, **kwargs)
        wid = self.winfo_id()
        cmd = 'xterm -into %d -fn *-fixed-*-*-*-20-* -geometry 300x30 -bg ' %wid #set font and window frame
        cmd = cmd + et.SelectedTheme["TerminalBG"] #set background
        cmd = cmd + ' -fg ' + et.SelectedTheme["TerminalFG"] #set foreground
        cmd = cmd + ' -sb &'
        try:
            self.terminalProcess = subprocess.Popen('exec ' + cmd, shell=True)
        except Exception as e:
            print(e)
            return
        self.attachedPID = self.terminalProcess.pid
        self.attachedPID = self.attachedPID+1

    def killProcess(self):
        #self.terminalProcess.kill()
        cmd = "kill -9 %d" % self.attachedPID
        os.system(cmd)


if __name__ == "__main__":
    root = Tk()

    root.geometry("900x300")
    tp = TerminalPanel(root)
    tp.pack(side=BOTTOM, expand=True, fill=BOTH)

    root.mainloop()
