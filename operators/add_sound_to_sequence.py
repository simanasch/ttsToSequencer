from os import path
from bpy.props import StringProperty,IntProperty
from bpy.types import Operator

def getFileName(filePath):
  return path.splitext( path.basename(filePath))[0]

def getFileExtension(filePath):
  return path.splitext( path.basename(filePath))[1]

def addSoundToScene(context, filePath):
  fileName=getFileName(filePath)
  result = None
  print(fileName)
  # ファイル名が"orig_"で始まる場合は除外
  if (not fileName.startswith("orig_")):
    # まだ追加してない場合は追加、ある場合はframe_endを取得
    for config in context.scene.libraryConfigs:
      if fileName.startswith(config.name):
        for seq in context.scene.sequence_editor.sequences:
          if (seq.type=="SOUND"):
            if (seq.sound.filepath == filePath):
              context.scene.frame_current = seq.frame_start
              context.scene.sequence_editor.sequences.remove(seq)
        result = context.scene.sequence_editor.sequences.new_sound(fileName, filePath,config.channel,frame_start=context.scene.frame_current)
        # 追加後、末尾フレームに移動
        context.scene.frame_current = result.frame_final_end
  return result

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
