from bpy.props import IntProperty
from bpy.types import Operator

class TTSTOSEQUENCER_OT_SelectActiveTts(Operator):
  """使用するttsエンジンを選択"""
  bl_idname="ttstosequencer.select_active_tts"
  bl_label="使用するttsエンジンを選択"
  bl_options = {'REGISTER', 'UNDO'}

  index:IntProperty(default=0,options={'HIDDEN'})

  def execute(self, context):
    context.scene.ttsConfig.selectedLibraryIndex = self.index
    print('selected:' +str(context.scene.ttsConfig.selectedLibraryIndex))
    return {'FINISHED'}
