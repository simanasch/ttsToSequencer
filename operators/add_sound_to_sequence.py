from os import path
from bpy.props import StringProperty,IntProperty
from bpy.types import Operator

def addSoundToScene(context, filePath, channel):
  fileName=path.splitext( path.basename(filePath))[0]
  return context.scene.sequence_editor.sequences.new_sound(fileName, filePath,channel,frame_start=context.scene.frame_current)

class TTSTOSEQUENCER_OT_AddSoundToSequence(Operator):
  """サウンドをシーケンサに追加する"""
  bl_idname="ttstosequencer.add_sound_to_sequence"
  bl_label="tts to sequencer file watcher"
  bl_options = {'REGISTER', 'UNDO'}

  filePath:StringProperty()
  channel:IntProperty()

  def execute(self, context):
    soundEffect = addSoundToScene(context, self.filePath, self.channel)
    # 音声追加後、追加した音声の終了フレームにカーソル移動する
    context.scene.frame_current = soundEffect.frame_final_end
    return {'FINISHED'}
