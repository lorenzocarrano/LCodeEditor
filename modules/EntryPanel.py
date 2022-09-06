from tkinter import *
import editortheme as et

class EntryPanel(Toplevel):
    def __init__(self, containerWidget, name, labels, callbacks, onClosingCallback=None):
        Toplevel.__init__(self, containerWidget, background=et.SelectedTheme["EntryPanelBG"])
        self.title(name)
        self.onClosingCallback = onClosingCallback
        self.bind('<Escape>', self.closePanel)
        self.protocol("WM_DELETE_WINDOW", self._onClosingPanel)
        if len(labels) == len(callbacks):
            self.patternEntry = Entry(self, width=50, background=et.SelectedTheme["EntryPanel_EntryBG"], foreground=et.SelectedTheme["EntryPanel_EntryFG"], insertbackground=et.SelectedTheme["EntryPanel_CursorColor"])
            self.patternEntry.pack(side=TOP, expand=True, fill=X)
            for i in range(len(labels)):
                button_i = Button(self, text=labels[i])
                button_i.configure(background=et.SelectedTheme["EntryPanel_ButtonsBG"], foreground=et.SelectedTheme["EntryPanel_ButtonsFG"], command=lambda btn = button_i, callback=callbacks[i]: self.invokeCallback(callback, btn))
                button_i.pack(side=LEFT, expand=True, fill=X)

        self.patternEntry.focus() #it is possible to directly write inside entry after creation


    def invokeCallback(self, callback, btn):
        callback(self.patternEntry.get())

    def closePanel(self, event):
        self.onClosingCallback()
        self.destroy()

    def _onClosingPanel(self):
        self.onClosingCallback()
        self.destroy()

'''
TEST FOR EntryPanel
def cb(text):
    print("pressed")
    print("text: ", text)
def Test(container):
    ep = EntryPanel(container, text1="Search in current file", text2="Search in all files   ", callback1=cb, callback2=cb)
if __name__ == "__main__":
    root = Tk()
    txt = Text(root)
    txt.pack()

    btn = Button(text="Press", command=lambda:Test(root))
    btn.pack()
    root.mainloop()
'''
