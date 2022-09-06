from tkinter import *
import editortheme as et

class YesNoPopupMessage(Toplevel):
    def __init__(self, message, containerWidget, linkedWidget, closeCallback):
        Toplevel.__init__(self, containerWidget, background=et.SelectedTheme["YesNoPopupBG"])
        self.containerWidget = containerWidget
        self.closeCallback = closeCallback

        msgLabel = Label(self, text=message, background=et.SelectedTheme["YesNoPopup_LabelBG"], foreground=et.SelectedTheme["YesNoPopup_LabelFG"])
        yesBtn = Button(self, text="Yes", background=et.SelectedTheme["YesNoPopupLabel_YesButtonBG"], foreground=et.SelectedTheme["YesNoPopupLabel_YesButtonFG"], command=lambda: self.close(True))
        noBtn = Button(self, text="No", background=et.SelectedTheme["YesNoPopupLabel_NoButtonBG"], foreground=et.SelectedTheme["YesNoPopupLabel_NoButtonFG"], command=lambda: self.close(False))

        msgLabel.pack(side=TOP)
        yesBtn.pack(side=LEFT, expand=True, fill=X)
        noBtn.pack(side=RIGHT, expand=True, fill=X)

    def close(self, save):
        self.closeCallback(save)
        try:
            self.destroy()
        except:
            pass
