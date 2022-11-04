from os import path
import bpy
from bpy.props import StringProperty,IntProperty
from bpy.types import Operator
from .add_subtitle_to_sequence import addSubtitleToScene
from ..util.path import getFileExtension, getFileName

def addSoundToSequence():
  scene = bpy.context.scene
  currentFrame = scene.frame_current
  ttsConfig = scene.ttsConfig
  activeLibrary = scene.libraryConfigs[scene.ttsConfig.selectedLibraryIndex]

  soundSequence = scene.sequence_editor.sequences.new_sound(getFileName(ttsConfig.wavPath) ,filepath=path.join(bpy.path.abspath(ttsConfig.folder), ttsConfig.wavPath), frame_start=currentFrame, channel=activeLibrary.channel)
  scene.frame_current = soundSequence.frame_final_end
  # TODO:追加した音声内容をblendファイル内のテキストに追加する
  if ttsConfig.saveTextOnSave:
    saveTtsText(scene, soundSequence)
  # 追加処理色々が終わったらttsConfigとかの値をクリアする
  if activeLibrary.hasSubtitle:
    addSubtitleToScene(scene, ttsConfig.text, soundSequence)
  ttsConfig.text = ''
  ttsConfig.wavPath = ''
  return soundSequence

def saveTtsText(scene, sound ):
  ttsConfig = scene.ttsConfig
  activeLibrary = scene.libraryConfigs[scene.ttsConfig.selectedLibraryIndex]
  csvName = getFileName(bpy.data.filepath) + '_ttsLog.csv'
  csvPath =  path.join(bpy.path.abspath(ttsConfig.folder), csvName)
  with open(csvPath, 'w', encoding='utf-8') as f:
    if not path.exists(csvPath):
      f.write('シーン名,チャンネル,開始フレーム,エンジン名,ライブラリ名,テキスト,ファイルパス\n')
    if bpy.data.texts.get(csvName) is None:
      text = bpy.data.texts.new(csvName)
      text.filepath = csvPath
    line = ','.join(
      [
        scene.name,
        str(activeLibrary.channel),
        str(sound.frame_start),
        activeLibrary.engineName,
        activeLibrary.libraryName,
        ttsConfig.text,
        ttsConfig.wavPath
      ]
    ) + '\n'
    f.write(line)

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
