'''
TODO : 	1. Clear,why app is hanging,while downloading files. Seems to launching streams is good idea.
	2. Make multi-streams ^_____^!
'''
import libtorrent as lt
import Tkinter as tk
import time
import sys

class MainTorrent():
  def __init__(self,window_,file_):
      self.window = window_
      self.file = file_
      self.mainloop()
  def mainloop(self):
    ses = lt.session()
    ses.listen_on(6881, 6891)
    e = lt.bdecode(open(self.file, 'rb').read())
    info = lt.torrent_info(e)
    params = { 'save_path': '.', 'storage_mode': lt.storage_mode_t.storage_mode_sparse, 'ti': info }
    h = ses.add_torrent(params)
    self.window.text_.insert(1.0,'Starting download file '+self.file+'\n')
    while (not h.is_seed()):
	s = h.status()
	state_str = ['queued', 'checking', 'downloading metadata', 'downloading', 'finished', 'seeding', 'allocating']
	self.window.text_.insert('end','%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s \n' % (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]))
	time.sleep(1)