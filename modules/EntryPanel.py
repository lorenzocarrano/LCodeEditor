from tkinter import *
class EntryPanel(Toplevel):
    def __init__(self, containerWidget, name, labels, callbacks):
        Toplevel.__init__(self, containerWidget)
        self.title(name)
        self.bind('<Escape>', self.closePanel)
        if len(labels) == len(callbacks):
            self.patternEntry = Entry(self, width=50)
            self.patternEntry.pack(side=TOP, expand=True, fill=X)
            for i in range(len(labels)):
                button_i = Button(self, text=labels[i])
                button_i.configure(command=lambda btn = button_i, callback=callbacks[i]: self.invokeCallback(callback, btn))
                button_i.pack(side=LEFT, expand=True, fill=X)

        self.patternEntry.focus() #it is possible to directly write inside entry after creation


    def invokeCallback(self, callback, btn):
        callback(self.patternEntry.get())

    def closePanel(self, event):
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
