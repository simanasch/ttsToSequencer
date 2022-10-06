from bpy.types import PropertyGroup, TextSequence
from bpy.props import BoolProperty, PointerProperty, StringProperty, FloatProperty, IntProperty
# やること:
# シーケンサ上に表示する音声入力設定
# 字幕の設定()

class subtitleConfig(PropertyGroup):
  """ttsの字幕設定を持つクラス"""
  bl_idname="ttstosequencer.subtitle_config"
  bl_label="subtitleConfig"

  font:StringProperty()
  size:FloatProperty()