import bpy
from os import path
from bpy.props import StringProperty
from bpy.types import Operator
from ..tts.handler import record
from ..util.path import getProjectPath, sanitizeFilePath
import time

def getFileName(libraryName):
  # ファイル名にタイムスタンプを利用する
  return sanitizeFilePath(libraryName + '_' + time.strftime('%Y%m%d%H%M%S') +'.wav')

class TTSTOSEQUENCER_OT_Recorder(Operator):
  """入力テキストを録音する"""
  bl_idname="ttstosequencer.recorder"
  bl_label="録音&シーケンサ追加"
  bl_options = {'REGISTER', 'UNDO'}

  text:StringProperty(options={"HIDDEN"})
  library:StringProperty(options={"HIDDEN"})
  engine:StringProperty(options={"HIDDEN"})

  def execute(self, context):
    ttsConfig = context.scene.ttsConfig
    if  not ttsConfig.folder:
      ttsConfig.folder = getProjectPath()
    ttsConfig.wavPath = getFileName(self.library)
    record(self.library,self.text,path.join(bpy.path.abspath(ttsConfig.folder), ttsConfig.wavPath) , self.engine )
    # やること
    return {'FINISHED'}
