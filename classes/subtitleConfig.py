from bpy.types import PropertyGroup, TextSequence
from bpy.props import BoolProperty, PointerProperty, StringProperty, FloatProperty, IntProperty,FloatVectorProperty

class subtitleConfig(PropertyGroup):
  """ttsの字幕設定を持つクラス"""
  bl_idname="ttstosequencer.subtitle_config"
  bl_label="subtitleConfig"

  font:StringProperty()
  size:FloatProperty()
  # フォント色
  color:FloatVectorProperty(subtype="COLOR_GAMMA")
  # 位置
  position:FloatVectorProperty(size=2)