from os import path
from bpy.props import StringProperty,IntProperty
from bpy.types import Operator
from ..tts.handler import play

class TTSTOSEQUENCER_OT_Player(Operator):
  """入力テキストを再生する"""
  bl_idname="ttstosequencer.player"
  bl_label="音声を再生"
  bl_options = {'REGISTER', 'UNDO'}

  text:StringProperty(options={'HIDDEN'})
  library:StringProperty(options={'HIDDEN'})
  engine:StringProperty(options={'HIDDEN'})

  def execute(self, context):
    play(self.library,self.text)
    # soundEffect = addSoundToScene(context, self.filePath, self.channel)
    # # 音声追加後、追加した音声の終了フレームにカーソル移動する
    # context.scene.frame_current = soundEffect.frame_final_end
    return {'FINISHED'}
