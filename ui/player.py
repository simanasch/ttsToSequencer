import bpy
from ..operators.player import TTSTOSEQUENCER_OT_Player
from ..operators.recorder import TTSTOSEQUENCER_OT_Recorder

# やること:シーケンサの画面のサイドバー上でフォルダ監視の切り替え、
# Listで音声入力の設定をできるようにする
class TTSToSequencer_PT_Player(bpy.types.Panel):
  """tts To SequencerのUI"""
  bl_idName = "ttstosequencer.TTS_PT_Player"
  bl_label= "ttsToSequencer Player"
  bl_space_type="SEQUENCE_EDITOR"
  bl_region_type="UI"
  bl_category="tts"
  bl_label="音声再生/録音"

  def draw(self,context):
    scene = context.scene
    library = scene.libraryConfigs[scene.ttsConfig.selectedLibraryIndex]
    layout = self.layout
    # for config in scene.libraryConfigs:
    #   layout.prop_enum(scene.ttsConfig,"selectedLibrary", value=config.libraryName)
    layout.label(text='再生/録音するテキスト')
    layout.prop(scene.ttsConfig, "text",text="")
    layout.separator()
    row = layout.row()
    ot = row.operator(TTSTOSEQUENCER_OT_Player.bl_idname,text="音声を再生")
    ot.text = scene.ttsConfig.text
    ot.library = library.libraryName
    ot.engine  = library.engineName
    record = row.operator(TTSTOSEQUENCER_OT_Recorder.bl_idname,text="音声を録音")
    record.text = scene.ttsConfig.text
    record.library = library.libraryName
    record.engine  = library.engineName
    # layout.prop_with_menu(scene,"libraryConfigs",text="ライブラリ選択")
    # layout.prop_with_menu(scene,"libraryConfigs",text="ライブラリ選択")
