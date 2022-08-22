from tkinter import *
class FileViewer:
    def __init__(self, rootWidget):
        #creating the scroll bar
        yScrollBar = Scrollbar(rootWidget)
        yScrollBar.pack(side=RIGHT, fill='y', expand=True)
        #creating the textWidget
        textWidget = Text(rootWidget)#, height=rootWidget.winfo_screenheight(), width=rootWidget.winfo_screenwidth(),  yscrollcommand=yScrollBar.set)
        textWidget.pack(side=LEFT, fill='both')
        # Attach the scrollbar with the text widget
        yScrollBar.config(command=textWidget.yview)

        self.textWidget = textWidget
        self.currentlyOpenedFile = ""
        self.Container = rootWidget

    def attachFile(self, fPath, data):
        self.textWidget.delete('1.0', END)
        self.textWidget.insert('1.0', data)
        self.currentlyOpenedFile = fPath
        self.Container.configure(text=fPath)




