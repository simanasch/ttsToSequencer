import bpy
from bpy.types import PropertyGroup, TextSequence
from bpy.props import StringProperty, FloatProperty, IntProperty,FloatVectorProperty, EnumProperty

# bpy.props.EnumPropertyの既知バグ回避のためのワークアラウンド
# EnumPropertyに持たせる文字列への参照をキャッシュする(ないと文字化けする。。。)
STRING_CACHE = {}
def intern_enum_items(items):
  def intern_string(s):
    if not isinstance(s, str):
      return s
    global STRING_CACHE
    if s not in STRING_CACHE:
      STRING_CACHE[s] = s
    return STRING_CACHE[s]
  return [tuple(intern_string(s) for s in item) for item in items]

class subtitleConfig(PropertyGroup):
  """ttsの字幕設定を持つクラス"""
  bl_idname="ttstosequencer.subtitle_config"
  bl_label="subtitleConfig"

  # itemsからEnum値を生成する
  def getFontList(self, context):
    fonts = bpy.data.fonts
    result = []
    for i in range(len(fonts)):
      result.append((fonts[i].name,fonts[i].name,""))
    return intern_enum_items(result)
  
  fontName: EnumProperty(items=getFontList)
  size:IntProperty()
  # フォント色
  color:FloatVectorProperty(subtype="COLOR",size=4)
  # 位置
  position:FloatVectorProperty(size=2)