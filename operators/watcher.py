from bpy.types import Operator
# from watchdog.observers import Observer
# from  watchdog.events import FileSystemEventHandler

class TTSTOSEQUENCER_OT_watcher(Operator):
  """ttsで生成したファイルの監視を行い、シーケンサに追加する"""
  bl_idname="ttstosequencer.watcher"
  bl_label="tts to sequencer file watcher"
  bl_options = {'REGISTER', 'UNDO'}

  def execute(self, context):
    return {'FINISHED'}
