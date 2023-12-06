import editortheme as et
import os
import tkinter as tk
import tkinter.ttk as ttk

class FileManager(tk.Frame):
    def __init__(self, rootWindow, path, containerWidget = ""):
        #defining style
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=et.SelectedTheme["FileManagerTextFONT"], foreground=et.SelectedTheme["FileManagerTextFG"], background=et.SelectedTheme["FileManagerTextBG"]) # Modify the font of the body
        style.configure('Treeview', rowheight=et.SelectedTheme["FileManagerROW_HEIGHT"])
        style.configure("mystyle.Treeview.Heading", font=et.SelectedTheme["FileManagerHeaderTextFONT"], foreground=et.SelectedTheme["FileManagerHeaderTextFG"], background=et.SelectedTheme["FileManagerHeaderTextBG"]) # Modify the font of the headings
        style.configure("myStyle.Tree.Heading", rowwidth=et.SelectedTheme["FileManagerROW_WIDTH"])
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders
        #code
        tk.Frame.__init__(self, rootWindow)
        self.tree = ttk.Treeview(self, style="mystyle.Treeview", height=50)

        ysb = ttk.Scrollbar(self, orient='vertical', command=self.tree.yview)
        xsb = ttk.Scrollbar(self, orient='horizontal', command=self.tree.xview)
        self.tree.configure(yscroll=ysb.set, xscroll=xsb.set)
        self.tree.heading('#0', text=path, anchor='w')

        relpath = os.path.relpath(path)
        abspath = os.path.relpath(path)
        root_node = self.tree.insert('', 'end', text=relpath, open=True)
        self.rootNodePath = relpath
        #root_node.configure(value=abspath) SBAGLIATO ma l'idea è questa
        self.process_directory(root_node, relpath)

        self.tree.grid(row=0, column=0)
        ysb.grid(row=0, column=1, sticky='ns')
        xsb.grid(row=1, column=0, sticky='ew')
        #self.grid()
        #bind event on double-click
        self.tree.bind("<Double-1>", self.OnDoubleClick)
        self.containerWidget = containerWidget
        self.startingPath=path

    def OnDoubleClick(self, event):
        item = self.tree.selection()[0] #clicked item
        path = self.tree.item(item)["text"]
        pathReconstructed = False
        while not pathReconstructed:
            parent_iid = self.tree.parent(item)
            parentPath = self.tree.item(parent_iid)["text"]
            if parentPath == self.rootNodePath:
                pathReconstructed = True #last append to be performed, then exit while

            path = parentPath + '/' + path
            item = parent_iid

        isdir = os.path.isdir(path)
        if isdir == True:
            #if it is a directory, nothing to do
            pass
        else:
            #if it is a file, open it
            try:
                self.containerWidget.openFile(path)
            except Exception as e:
                pass

        '''
        print("you clicked on: ", self.tree.item(item,"text"))
        if parent_iid:
            print("parent: ", self.tree.item(parent_iid)['text'])
        else:
            print("parent: ", self.tree.item(item)['text'])
        '''
        #print("you clicked on", self.tree.item(item,"text"))
        #print("you clicked on", self.tree.item(item))

    def process_directory(self, parent, path):
        for p in os.listdir(path):
            relpath = os.path.join(path, p)
            isdir = os.path.isdir(relpath)
            oid = self.tree.insert(parent, 'end', text=p, open=False)
            if isdir:
                self.process_directory(oid, relpath)

    def GetAll(self):
        return self.tree.get_children()
'''
root = tk.Tk()
path_to_my_project = "./../"
fManager = FileManager(root, path=path_to_my_project)
fManager.mainloop()
'''
