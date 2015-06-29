'''
TODO : 	1. Make some kind of db, or use fs
'''

import os
import shutil
class FileOperations:
    def file_copy(self,file_to_copy):
      str_ = file_to_copy.name.split('/').pop()
      shutil.copy2(file_to_copy.name,'torrents/'+str_)
      return os.getcwd()+'/torrents/'+str_