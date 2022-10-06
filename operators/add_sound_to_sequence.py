from os import path
from bpy.props import StringProperty,IntProperty
from bpy.types import Operator

class TTSTOSEQUENCER_OT_AddSoundToSequence(Operator):
  """サウンドをシーケンサに追加する"""
  bl_idname="ttstosequencer.add_sound_to_sequence"
  bl_label="tts to sequencer file watcher"
  bl_options = {'REGISTER', 'UNDO'}

  # fileName:StringProperty()
  filePath:StringProperty()
  channel:IntProperty()

  def execute(self, context):
    # bpy.data.scenes[0].sequence_editor.sequences.new_sound("ia_test","A:\\Videos\\編集中tmp\\220717_234742_IA_身も蓋もない.wav",5,255)
    fileName=path.splitext( path.basename(self.filePath))[0]
    soundEffect = context.scene.sequence_editor.sequences.new_sound(fileName, self.filePath,self.channel,frame_start=context.scene.frame_current)
    # 音声追加後、追加した音声の終了フレームにカーソル移動する
    context.scene.frame_current = soundEffect.frame_final_end
    return {'FINISHED'}
