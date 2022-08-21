from tkinter import *
class FileViewer:
    def __init__(self, rootWidget):
        #creating the scroll bar
        yScrollBar = Scrollbar(rootWidget)
        yScrollBar.pack(side=RIGHT, fill='y')
        #creating the textWidget
        textWidget = Text(rootWidget)#, height=rootWidget.winfo_screenheight(), width=rootWidget.winfo_screenwidth(),  yscrollcommand=yScrollBar.set)
        textWidget.pack(side=LEFT, fill='y')
        # Attach the scrollbar with the text widget
        yScrollBar.config(command=textWidget.yview)



