from os import path
import bpy
from bpy.props import StringProperty,IntProperty
from bpy.types import Operator
from ..util.path import getFileExtension, getFileName

def addSoundToSequence():
  scene = bpy.context.scene
  ttsConfig = scene.ttsConfig
  currentFrame = scene.frame_current
  activeLibrary = scene.libraryConfigs[scene.ttsConfig.selectedLibraryIndex]

  result = scene.sequence_editor.sequences.new_sound(getFileName(ttsConfig.wavPath) ,filepath=path.join(bpy.path.abspath(ttsConfig.folder), ttsConfig.wavPath), frame_start=currentFrame, channel=activeLibrary.channel)
  scene.frame_current = result.frame_final_end
  # TODO:追加した音声内容をblendファイル内のテキストに追加する
  # 追加処理色々が終わったらttsConfigとかの値をクリアする
  ttsConfig.text = ''
  ttsConfig.wavPath = ''

class TTSTOSEQUENCER_OT_AddSoundToSequence(Operator):
  """サウンドをシーケンサに追加する"""
  bl_idname="ttstosequencer.add_sound_to_sequence"
  bl_label="tts to sequencer file watcher"
  bl_options = {'REGISTER', 'UNDO'}

  filePath:StringProperty()
  channel:IntProperty()

  def execute(self, context):
    # soundEffect = addSoundToScene(context, self.filePath, self.channel)
    # 音声追加後、追加した音声の終了フレームにカーソル移動する
    # context.scene.frame_current = soundEffect.frame_final_end
    return {'FINISHED'}
