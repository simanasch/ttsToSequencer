from os import path
import bpy
from bpy.props import StringProperty,IntProperty
from bpy.types import Operator
from .add_subtitle_to_sequence import addSubtitleToScene
from ..util.path import getFileExtension, getFileName

def addSoundToSequence():
  scene = bpy.context.scene
  ttsConfig = scene.ttsConfig
  currentFrame = scene.frame_current
  activeLibrary = scene.libraryConfigs[scene.ttsConfig.selectedLibraryIndex]

  soundSequence = scene.sequence_editor.sequences.new_sound(getFileName(ttsConfig.wavPath) ,filepath=path.join(bpy.path.abspath(ttsConfig.folder), ttsConfig.wavPath), frame_start=currentFrame, channel=activeLibrary.channel)
  scene.frame_current = soundSequence.frame_final_end
  # TODO:追加した音声内容をblendファイル内のテキストに追加する
  # 追加処理色々が終わったらttsConfigとかの値をクリアする
  if activeLibrary.hasSubtitle:
    addSubtitleToScene(scene, ttsConfig.text, soundSequence)
  ttsConfig.text = ''
  ttsConfig.wavPath = ''
  return soundSequence

class TTSTOSEQUENCER_OT_AddSoundToSequence(Operator):
  """サウンドをシーケンサに追加する"""
  bl_idname="ttstosequencer.add_sound_to_sequence"
  bl_label="tts to sequencer file watcher"
  bl_options = {'REGISTER', 'UNDO'}

  filePath:StringProperty()
  channel:IntProperty()

  def execute(self, context):
    soundEffect = addSoundToSequence()
    return {'FINISHED'}
