from bpy import path
from bpy.types import Operator
from bpy.props import CollectionProperty,StringProperty,BoolProperty
from watchdog.observers import Observer
from ..handlers.ttsFileCreatedEventHandler import ttsFileCreatedEventHandler
import re

observer = None
class TTSTOSEQUENCER_OT_observer(Operator):
  """ttsで生成したファイルの監視を行い、シーケンサに追加する"""
  bl_idname="ttstosequencer.observer"
  bl_label="監視有効/無効切り替え"
  bl_options = {'REGISTER', 'UNDO'}

  # 監視するパスの正規表現のリスト
  # patterns = CollectionProperty(type=StringProperty,default=[])
  # 監視するフォルダ
  folder = StringProperty(subtype="DIR_PATH",default="//")
  # 再帰探索の有無
  isrecursive = BoolProperty()

  def stopObserver(self,context):
    global observer
    print("exiting observer")
    if observer is not None:
      observer.stop()
    observer=None
    context.scene.ttsConfig.isObserverRunning=False


  def execute(self, context):
    # 実行するたびにファイル監視の有効/無効を切り替える(初期では監視無効)
    global observer
    # print(self.patterns)
    print(context.scene.ttsConfig.folder)
    # 実行時にcontext.scene.libraryConfigsから監視対象の正規表現をとる
    # patterns = [".+"]
    patterns = ["*.txt","*.wav"]
    # for config in context.scene.libraryConfigs:
      # patterns.append(re.compile(repr(config.fileNamePattern)))
      # if config.fileNamePattern != '':
      #   patterns.append(config.fileNamePattern)
    if (observer is None):
      observer=Observer()
      print(patterns)
      event_handler = ttsFileCreatedEventHandler(patterns)
      # event_handler = ttsFileCreatedEventHandler(self.patterns)
      observer.schedule(event_handler, path.abspath(context.scene.ttsConfig.folder), recursive=False)
      observer.start()
      context.scene.ttsConfig.isObserverRunning=True
    else:
      self.stopObserver(context)
    return {'FINISHED'}
