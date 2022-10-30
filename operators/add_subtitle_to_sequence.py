import bpy
from bpy.types import Operator
from bpy.props import StringProperty, PointerProperty
from ..classes.subtitleConfig import subtitleConfig
from ..util.path import getFileName

defaultSeparator="＞"

def addSubtitleToScene(scene,text, soundEffect):
  activeLibrary = scene.libraryConfigs[scene.ttsConfig.selectedLibraryIndex]
  subtitleConfig = activeLibrary.subtitleConfig
  soundSeq = soundEffect
  # 既にサウンド作成済みの場合に字幕を追加する
  textEffect = scene.sequence_editor.sequences.new_effect(text, type="TEXT",channel=activeLibrary.channel+1,frame_start=soundSeq.frame_start,frame_end=soundSeq.frame_final_end)
  textEffect.font = bpy.data.fonts[subtitleConfig.fontName]
  textEffect.text=text
  textEffect.font_size = subtitleConfig.size
  textEffect.location = subtitleConfig.position
  textEffect.color=subtitleConfig.color
  return textEffect

class TTSTOSEQUENCER_OT_AddSubtitleToSequence(Operator):
  """字幕をシーケンサに追加する"""
  bl_idname="ttstosequencer.add_subtitle_to_sequence"
  bl_label="tts to sequencer addSubtitleToSequence"
  bl_options = {'REGISTER', 'UNDO'}

  text: StringProperty()
  config: PointerProperty(type=subtitleConfig)
  def execute(self, context):
    # bpy.ops.sequencer.effect_strip_add(type={"TEXT"}, frame_start=1,frame_end=30,channel=5)
    textEffect = context.scene.sequence_editor.sequences.new_effect(self.text, type="TEXT",channel=5,frame_start=1,frame_end=20)
    textEffect.text=self.text
    return {'FINISHED'}
