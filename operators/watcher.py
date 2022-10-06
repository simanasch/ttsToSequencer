from bpy.types import Operator
from bpy.props import BoolProperty()
from watchdog.observers import Observer

observer = Observer()
class TTSTOSEQUENCER_OT_watcher(Operator):
  """ttsで生成したファイルの監視を行い、シーケンサに追加する"""
  bl_idname="ttstosequencer.watcher"
  bl_label="tts to sequencer file watcher"
  bl_options = {'REGISTER', 'UNDO'}

  isObserving:BoolProperty()

  def execute(self, context):
    global observer
    # observerの切り替えをする
    print(observer)
    if (observer is not None) & (observer.is_alive()):
      print("stop observer")
      observer.stop()
      self.isObserving = False
    else:
      print("start observer")
      observer.start()
      self.isObserving = True
    return {'FINISHED'}
