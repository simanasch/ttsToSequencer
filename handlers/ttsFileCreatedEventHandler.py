import bpy
from  watchdog.events import PatternMatchingEventHandler
from ..util.path import addSoundToScene,getFileExtension
from ..operators.add_subtitle_to_sequence import addSubtitleToScene
class ttsFileCreatedEventHandler(PatternMatchingEventHandler):
  # クラス初期化
  def __init__(self, patterns):
    super(ttsFileCreatedEventHandler, self).__init__(patterns=patterns,ignore_patterns=["orig*.*"],ignore_directories=True)

  def on_modified(self,event):
    # 音声は(書き込みが後なので)onModifiedで処理
    print("on_modified detected" + event.src_path)
    # print(event)
    if getFileExtension(event.src_path) ==".wav":
      soundEffect = addSoundToScene(bpy.context, event.src_path)
    elif getFileExtension(event.src_path) == ".txt":
      # txtの場合、同名の.wavファイルがあったら字幕を追加する
      addSubtitleToScene(bpy.context, event.src_path)