from bpy.props import StringProperty,IntProperty
from bpy.types import Operator

class TTSTOSEQUENCER_OT_removeLibraryConfig(Operator):
  """ttsライブラリ設定を削除"""
  bl_idname="ttstosequencer.remove_library_config"
  bl_label="ttsライブラリ削除"
  bl_options = {'REGISTER', 'UNDO'}

  index:IntProperty(default=0,options = {'HIDDEN'})

  def execute(self, context):
    print(self.index)
    context.scene.libraryConfigs.remove(self.index)
    return {'FINISHED'}
