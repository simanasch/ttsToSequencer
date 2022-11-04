from bpy.types import PropertyGroup
from bpy.props import StringProperty, IntProperty, BoolProperty

class ttsConfig(PropertyGroup):
  """音声保存先のフォルダなど、tts全般の設定を保存するクラス"""
  bl_idname="ttstoseuencer.tts_config"
  bl_label="ttsConfig"

  folder:StringProperty(subtype="DIR_PATH")
  selectedLibraryIndex:IntProperty(default=0)
  text:StringProperty()
  wavPath: StringProperty()
  saveTextOnSave:BoolProperty()