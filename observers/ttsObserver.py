import time
from bpy.types import Operator
from watchdog.observers import Observer
from  watchdog.events import FileSystemEventHandler

class ttsObserver(FileSystemEventHandler):
  observer = Observer()

  def startObserver(isRecursive=True):
    global observer 
    observer.stop()
    # observer = Observer()
    # observer.schedule(event_handler, path, recursive=isRecursive)
    observer.start()
    # try:
    #   while True:
    #     time.sleep(1)
    # except KeyboardInterrupt:
    #     observer.stop()
    observer.join()
  
  def stopObserver():
    global observer
    observer.stop()