from tkinter import *

class YesNoPopupMessage(Toplevel):
    def __init__(self, message, containerWidget, linkedWidget, closeCallback):
        Toplevel.__init__(self, containerWidget)
        self.containerWidget = containerWidget
        self.closeCallback = closeCallback

        msgLabel = Label(self, text=message)
        yesBtn = Button(self, text="Yes", command=lambda: self.close(True))
        noBtn = Button(self, text="No", command=lambda: self.close(False))

        msgLabel.pack(side=TOP)
        yesBtn.pack(side=LEFT, expand=True, fill=X)
        noBtn.pack(side=RIGHT, expand=True, fill=X)

    def close(self, save):
        self.closeCallback(save)
        try:
            self.destroy()
        except:
            pass
