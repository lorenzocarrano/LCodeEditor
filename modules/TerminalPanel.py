from tkinter import *
import subprocess
import editortheme as et
import os

class TerminalPanel(Canvas):
    def __init__(self, *args, **kwargs):
        Canvas.__init__(self, *args, **kwargs)

        self.terminalProcess = None
        self.attachedPID = None
        self.attachedPID = None

        self._openTerminal()

    def killProcess(self):
        #self.terminalProcess.kill()
        cmd = "kill -9 %d" % self.attachedPID
        os.system(cmd)

    def _openTerminal(self):
        wid = self.winfo_id()
        cmd = 'xterm -into %d -fn *-fixed-*-*-*-20-* -geometry 300x30 -bg ' %wid #set font and window frame
        cmd = cmd + et.SelectedTheme["TerminalBG"] #set background
        cmd = cmd + ' -fg ' + et.SelectedTheme["TerminalFG"] #set foreground
        cmd = cmd + ' -sb &'

        self.terminalProcess = subprocess.Popen('exec ' + cmd, shell=True)
        self.attachedPID = self.terminalProcess.pid
        self.attachedPID = self.attachedPID+1

    def refreshTerminal(self):
        self.killProcess()
        self._openTerminal()
