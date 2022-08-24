import tkinter as tk
import fileViewer
import os
import re
from syntaxconf import regexList, applyTagCalls, CExtensionsList, PyExtensionsList
class TextLineNumbers(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
        self.textwidget = None

    def attach(self, text_widget):
        self.textwidget = text_widget

    def redraw(self, *args):
        #redraw line numbers
        self.delete("all")

        i = self.textwidget.index("@0,0")
        while True :
            dline= self.textwidget.dlineinfo(i)
            if dline is None: break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(2,y,anchor="nw", text=linenum)
            i = self.textwidget.index("%s+1line" % i)

class CodeText(fileViewer.FileViewer):
    def __init__(self, *args, **kwargs):
        fileViewer.FileViewer.__init__(self, *args, **kwargs)

        # create a proxy for the underlying widget
        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)

    def _proxy(self, *args):
        # let the actual widget perform the requested action
        cmd = (self._orig,) + args
        result = self.tk.call(cmd)

        # generate an event if something was added or deleted,
        # or the cursor position changed
        if (args[0] in ("insert", "replace", "delete") or
            args[0:3] == ("mark", "set", "insert") or
            args[0:2] == ("xview", "moveto") or
            args[0:2] == ("xview", "scroll") or
            args[0:2] == ("yview", "moveto") or
            args[0:2] == ("yview", "scroll")
        ):
            self.event_generate("<<Change>>", when="tail")

        # return what the actual widget returned
        return result

class CodeViewer(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.text = CodeText(self)
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.text.yview)
        self.text.configure(yscrollcommand=self.vsb.set)
        self.text.tag_configure("bigfont", font=("Helvetica", "24", "bold"))
        self.linenumbers = TextLineNumbers(self, width=30)
        self.linenumbers.attach(self.text)

        self.vsb.pack(side="right", fill="y")
        self.linenumbers.pack(side="left", fill="y")
        self.text.pack(side="right", fill="both", expand=True)

        self.text.bind("<<Change>>", self._on_change)
        self.text.bind("<Configure>", self._on_change)

        self.displayedFile =  ""

    def _on_change(self, event):
        self.linenumbers.redraw()
        self._syntaxSetup()

    def attachFile(self, fPath, data):
        self.text.attachFile(fPath, data)
        self.displayedFile = fPath
        self._syntaxSetup()


    def _syntaxSetup(self):
        #set the right syntax highlighting depending on detected language
        #get the file extension
        fileExtension = self._getFileExtension(self.displayedFile)
        #get the index for the syntax highlightinh configuration
        index = self._syntaxHighlightingConfiguration(fileExtension)
        #prepare a regular expression (language-dependent)
        try:
            regex = regexList[index]

            #apply tags
            applyTagCalls[0](self)
        except:
            pass
    def _getFileExtension(self, fPath):
        # this will return a tuple of root and extension
        split_tup = os.path.splitext(fPath)
        # extract the file name and extension
        file_name = split_tup[0]
        file_extension = split_tup[1]
        return file_extension

    def _configure_tags(self, text_widget, tags):
        for tag, color in tags.items():
            text_widget.tag_delete(tag)
            text_widget.tag_config(tag, foreground=color)

    def _syntaxHighlightingConfiguration(self, extension):
        if extension in CExtensionsList:
            return 0
        elif extension in PyExtensionsList:
            return 1
        else:
            return 2
'''
if __name__ == "__main__":
    root = tk.Tk()
    CodeViewer(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
'''
