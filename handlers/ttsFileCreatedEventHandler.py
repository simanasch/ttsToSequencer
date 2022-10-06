from  watchdog.events import RegexMatchingEventHandler
from bpy.types import Context
from ..operators.add_sound_to_sequence import addSoundToScene

class ttsFileCreatedEventHandler(RegexMatchingEventHandler):
  # クラス初期化
  def __init__(self, regexes):
    super(ttsFileCreatedEventHandler, self).__init__(regexes=regexes,ignore_directories=True)

  def on_modified(self,event):
    # 音声は(書き込みが後なので)onModifiedで処理
    print("on_modified detected")
    # print(event)
    soundEffect = addSoundToScene(Context, event.src_path, 5)
    # print(event.src_path)