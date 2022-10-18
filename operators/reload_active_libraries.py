from bpy.props import StringProperty,IntProperty
from bpy.types import Operator
from ..tts.handler import getLibraries

class TTSTOSEQUENCER_OT_ReloadAvailableTts(Operator):
  """ttsライブラリ設定を追加"""
  bl_idname="ttstosequencer.reload_available_tts"
  bl_label="利用可能なttsライブラリの読み込み"
  bl_options = {'REGISTER', 'UNDO'}


  def execute(self, context):
    # context.scene.libraryConfigs.add()
    context.scene.libraryConfigs.clear()
    activeLibraries = getLibraries()
    for library in activeLibraries:
      libraryConfig = context.scene.libraryConfigs.add()
      libraryConfig.engineName = library.EngineName
      libraryConfig.libraryName = library.LibraryName
      print(library.EngineName)
      print(library.LibraryName)
    return {'FINISHED'}
