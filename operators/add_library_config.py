from bpy.props import StringProperty,IntProperty
from bpy.types import Operator

class TTSTOSEQUENCER_OT_AddLibraryConfig(Operator):
  """ttsライブラリ設定を追加"""
  bl_idname="ttstosequencer.add_library_config"
  bl_label="ttsライブラリ追加"
  bl_options = {'REGISTER', 'UNDO'}


  def execute(self, context):
    context.scene.libraryConfigs.add()
    return {'FINISHED'}
