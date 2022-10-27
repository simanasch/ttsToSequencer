from bpy.types import Operator
from bpy.props import StringProperty, PointerProperty
from ..classes.subtitleConfig import subtitleConfig
from ..util.path import getFileName

defaultSeparator="＞"

def addSubtitleToScene(context,filePath):
  fileName=getFileName(filePath)
  print("text File Path:"+filePath)
  textEffect=None
  for config in context.scene.libraryConfigs:
    if fileName.startswith(config.name) & config.hasSubtitle:
      soundSeq = None
      for seq in [seq for seq in context.scene.sequence_editor.sequences if seq.type=="SOUND"]:
        if (getFileName(seq.sound.filepath) == fileName):
          soundSeq = seq

      if soundSeq != None:
        # 既にサウンド作成済みの場合に字幕を追加する
        with open(filePath, encoding="shift_jis") as f:
          s=f.read()
          print(s)
          textEffect = context.scene.sequence_editor.sequences.new_effect(s, type="TEXT",channel=config.channel+1,frame_start=soundSeq.frame_start,frame_end=soundSeq.frame_final_end)
          textEffect.text=s.split(defaultSeparator)[-1]
          textEffect.location[1]=0.2
          textEffect.use_box=True
          textEffect.box_color=(0.2,0.2,0.2,0.3)
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
