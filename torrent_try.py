'''
TODO : 	1. Make GUI more beautifull ^^ !!!!!!! USE PYQT!!!!
	2. Add list of existing torrents from db or filesystem
	3. Add support of choosing dir fo downloaded file functionality
'''
import Tkinter as tk
import tkFileDialog

import fileoperations as fo
import maintorrent as mt

class Application():
    def __init__(self,root):
      self.root_ = root
      self.frame_ = self.root_.Frame(width=768, height=576)
      self.createWidgets()
      self.frame_.pack()
      
      self.root_.mainloop()

    def createWidgets(self):
      self.frame_.add_button = tk.Button()
      self.frame_.add_button["text"] = "Add file"
      self.frame_.add_button["command"] = self.add_file
      self.frame_.add_button.pack(side="top")
      
      self.text_=self.root_.Text(self.frame_)
      self.text_.pack()
      
    def add_file(self):
      file = tkFileDialog.askopenfile(mode='r')
      if(file):
	copied_file = fo.FileOperations().file_copy(file)
	mt.MainTorrent(self,copied_file)
      else:
	self.text_.insert(1.0,'No file added')
  
app = Application(tk)
