from bpy.types import Operator
from bpy.props import BoolProperty
from watchdog.observers import Observer
from ..handlers.ttsFileCreatedEventHandler import ttsFileCreatedEventHandler

observer = None
class TTSTOSEQUENCER_OT_observer(Operator):
  """ttsで生成したファイルの監視を行い、シーケンサに追加する"""
  bl_idname="ttstosequencer.observer"
  bl_label="tts to sequencer file observer"
  bl_options = {'REGISTER', 'UNDO'}

  isObserving:BoolProperty(default=False)

  def stopObserver(self):
    global observer
    print("exiting observer")
    observer.stop()
    observer=None
    self.isObserving = False


  def execute(self, context):
    # 実行するたびにファイル監視の有効/無効を切り替える(初期では監視無効)
    global observer
    if (observer is None):
      observer=Observer()
      event_handler = ttsFileCreatedEventHandler(["*.wav","*.txt"])
      observer.schedule(event_handler, "A:\Videos\編集中tmp", recursive=True)
      observer.start()
      self.isObserving = True
    else:
      self.stopObserver()
    return {'FINISHED'}
