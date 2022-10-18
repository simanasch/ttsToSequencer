from bpy.types import PropertyGroup, TextSequence
from bpy.props import BoolProperty, PointerProperty, StringProperty, FloatProperty, IntProperty
from .subtitleConfig import subtitleConfig

class libraryConfig(PropertyGroup):
  """ttsに対するインポート設定、字幕設定を持つクラス"""
  bl_idname="ttstoseuencer.tts_config"
  bl_label="libraryConfig"

  fileNamePattern:StringProperty()
  engineName: StringProperty()
  libraryName: StringProperty()
  channel:IntProperty(default=0)
  hasSubtitle:BoolProperty()
  
  subtitleConfig: PointerProperty(type=subtitleConfig,name="字幕設定")
