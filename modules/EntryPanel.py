from tkinter import *
class EntryPanel(Toplevel):
    def __init__(self, containerWidget, text1, text2, callback1, callback2):
        Toplevel.__init__(self, containerWidget)
        self.patternEntry = Entry(self, width=50)
        self.patternEntry.pack(side=TOP, expand=True, fill=X)
        self.Btn1 = Button(self, text=text1, command=lambda:self.callbackIntern(callback1))
        self.Btn2 = Button(self, text=text2, command=lambda:self.callbackIntern(callback2))
        self.Btn1.pack(side=LEFT, expand=True, fill=X)
        self.Btn2.pack(side=RIGHT, expand=True, fill=X)
        self.callback1 = callback1
        self.callback2 = callback2

        self.patternEntry.focus() #it is possible to directly write inside entry after creation

    def callbackIntern(self, func):
        func(self.patternEntry.get())

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
