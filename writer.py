import threading
import sys
import queue
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL)   #permette di prevenire il broken pipen

class Writer(threading.Thread):

  def __init__(self, file_name):
    threading.Thread.__init__(self)
    #self.stream_file = open(file_name, 'w')
    self.q = queue.Queue(maxsize=80000)

  def run(self):
   while True:
    strng = self.q.get()
		#self.stream_file.write(strng)
    sys.stdout.write(strng)

  def add(self, strng):
  	self.q.put(strng)
