import sys
sys.path.insert(0, '../conf')
import editortheme as et
import tkinter as tk
import sys
sys.path.insert(0, '../conf')
import fileViewer
import os
import re
from syntaxconf import regexList, applyTagCalls, CExtensionsList, PyExtensionsList
from StdOutManager import StdOutManager

class TextLineNumbers(tk.Canvas):
    def __init__(self, *args, **kwargs):
        try:
            kwargs["bg"] = et.SelectedTheme["LinesBG"]
            #kwargs["foreground"] = et.SelectedTheme["CodeLinesColorFG"]
            tk.Canvas.__init__(self, *args, **kwargs)
        except Exception as e:
            print(e)
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

            self.create_text(2,y,anchor="nw", text=linenum, font=et.SelectedTheme["CodeLinesNumberFONT"], fill=et.SelectedTheme["CodeLinesColorFG"])

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
        if (args[0] in ("insert", "replace", "delete")): #or
            #args[0:3] == ("mark", "set", "insert") or
            #args[0:2] == ("xview", "moveto") or
            #args[0:2] == ("xview", "scroll") or
            #args[0:2] == ("yview", "moveto") or
            #args[0:2] == ("yview", "scroll")
        #):
            self.event_generate("<<Change>>", when="tail")

        # return what the actual widget returned
        return result

    def contentModified(self, path):
        f = open(path, "r")
        fLines = f.read().splitlines() #file lines
        tLines = self.get("1.0", tk.END).splitlines() #text lines

        if len(fLines) != len(tLines):
            return True
        for i in range(len(fLines)):
            if tLines[i] != fLines[i]:
                return True

        return False



    def highlightMatches(self, pattern):
        self.tag_remove('found', '1.0', tk.END)
        ser = pattern
        if ser:
            idx = '1.0'
            while 1:
                idx = self.search(ser, idx, nocase=1,
                                stopindex=tk.END)
                if not idx: break
                lastidx = '%s+%dc' % (idx, len(ser))

                self.tag_add('found', idx, lastidx)
                idx = lastidx
            self.tag_config('found', foreground=et.SelectedTheme["SearchedTextFG"], background=et.SelectedTheme["SearchedTextBG"])

    def getPatternOccurrencies(self, pattern):
        ser = pattern
        stdoutMngr = StdOutManager()
        if ser:
            idx = '1.0'
            while 1:
                idx = self.search(ser, idx, nocase=1,
                                stopindex=tk.END)
                if not idx: break
                lastidx = '%s+%dc' % (idx, len(ser))
                idx = lastidx

                stdoutMngr.stdoutPrint(data=lastidx, endCharacter='\n')

class CodeViewer(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        self.text = CodeText(self, background=et.SelectedTheme["EditorBG"], foreground=et.SelectedTheme["CodeTextColorFG"], font=et.SelectedTheme["CodeTextFONT"], insertbackground = et.SelectedTheme["EntryPanel_CursorColor"])

        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.text.yview)
        self.text.configure(yscrollcommand=self.vsb.set)
        self.text.tag_configure("bigfont", font=("Helvetica", "24", "bold"))
        self.linenumbers = TextLineNumbers(self, width=30)
        self.linenumbers.attach(self.text)

        self.vsb.pack(side="right", fill="y")
        self.linenumbers.pack(side="left", fill="y")
        self.text.pack(side="right", fill="both", expand=True)
        #bind on generated events
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

    def fileContentModified(self):
        return self.text.contentModified(self.displayedFile)

    def saveContent(self):
        stdoutMngr = StdOutManager()
        lines = self.text.get("1.0", tk.END).splitlines()
        nLines = len(lines)
        f = open(self.displayedFile, "w")
        f.close()
        count = 0
        for line in lines:
            if count == nLines-1:
                stdoutMngr.stdoutPrint(data=line, fOut=self.displayedFile, mode="a", endCharacter="")
            else:
                stdoutMngr.stdoutPrint(data=line, fOut=self.displayedFile, mode="a", endCharacter="\n")
            count = count +1
        #the flag is reset since the file content has been saved
        self.contentModified = False

    def searchPattern(self, pattern):
        self.text.highlightMatches(pattern)
        #self.text.highlightExactMatches(pattern)

    def getPatternOccurrencies(self, pattern):
        #return a list of tuples containing the pattern's matches
        self.text.getPatternOccurrencies(pattern)
        pass

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
            applyTagCalls[index](self)
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

