import tkinter as tk
import fileViewer
import os
import re
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
        #get file lines
        lines = self.text.get(1.0, tk.END).splitlines()
        #prepare a regular expression (language-dependent)
        regex = re.compile(
            r"(^\s*"
            r"(?P<if>if)" + "|"  # if condition
            r"(?P<for>for)" + "|"  # for loop
            r"(?P<include>#include\s+[\"<]\S+)" + "|"
            r"(?P<int>\bint\b)" + "|"   # variable
            r"(?P<float>\bfloat\b)" + "|" #float variable
            r"(?P<char>\bchar\b)" + "|" #float variable
            r"(?P<return>\breturn\b)" +  #return
            r"[\s\(]+)"
        )

        #apply tags
        for idx, line in enumerate(lines):
            int_tag = f"int_{idx}"
            float_tag = f"float_{idx}"
            char_tag = f"char_{idx}"
            for_tag = f"for_{idx}"
            if_tag = f"if_{idx}"
            include_tag = f"include_{idx}"
            return_tag = f"return_{idx}"
            tags = {
                int_tag: "blue",
                float_tag: "blue",
                char_tag: "blue",
                for_tag: "green",
                if_tag: "purple",
                include_tag: "green",
                return_tag: "blue"
                # add new tag here
            }
            self.configure_tags(self.text, tags)

            for match in regex.finditer(line):
                for tag in tags:
                    group_name = tag.split("_")[0]
                    if -1 != match.start(group_name):
                        self.text.tag_add(
                            tag,
                            "{0}.{1}".format(idx+1, match.start(group_name)),
                            "{0}.{1}".format(idx+1, match.end(group_name))
                        )

        pass
    def _getFileExtension(self, fPath):
        # this will return a tuple of root and extension
        split_tup = os.path.splitext(fPath)
        # extract the file name and extension
        file_name = split_tup[0]
        file_extension = split_tup[1]
        return file_extension

    def configure_tags(self, text_widget, tags):
        for tag, color in tags.items():
            text_widget.tag_delete(tag)
            text_widget.tag_config(tag, foreground=color)
'''
if __name__ == "__main__":
    root = tk.Tk()
    CodeViewer(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
'''
