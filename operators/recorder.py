from os import path
from bpy.props import StringProperty,IntProperty
from bpy.types import Operator
from ..tts.handler import record
from ..util.path import getProjectPath, sanitizeFilePath
import time

def getFileName(libraryName):
  return sanitizeFilePath(libraryName + '_' + time.strftime('%Y%m%d%H%M%S') +'.wav')

class TTSTOSEQUENCER_OT_Recorder(Operator):
  """入力テキストを録音する"""
  bl_idname="ttstosequencer.recorder"
  bl_label="音声を録音"
  bl_options = {'REGISTER', 'UNDO'}

  text:StringProperty(options={"HIDDEN"})
  library:StringProperty(options={"HIDDEN"})
  engine:StringProperty(options={"HIDDEN"})

  def execute(self, context):
    ttsConfig = context.scene.ttsConfig
    if  not ttsConfig.folder:
      ttsConfig.folder = getProjectPath()
    record(self.library,self.text,path.join(ttsConfig.folder, getFileName(self.library)) , self.engine )
    return {'FINISHED'}
