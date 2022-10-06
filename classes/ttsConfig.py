from bpy.types import PropertyGroup, TextSequence
from bpy.props import BoolProperty, PointerProperty, StringProperty, FloatProperty, IntProperty
# from .subtitleConfig import subtitleConfig

class ttsConfig(PropertyGroup):
  """音声保存先のフォルダなど、tts全般の設定を保存するクラス"""
  bl_idname="ttstoseuencer.tts_config"
  bl_label="ttsConfig"

  # channel:IntProperty(default=0)
  folder:StringProperty(subtype="DIR_PATH")
  isObserverRunning:BoolProperty()