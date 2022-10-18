import bpy
from ..operators.player import TTSTOSEQUENCER_OT_Player
from .tts_library import TTSToSequencer_MT_TtsLibrary

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
    layout = self.layout
    # for config in scene.libraryConfigs:
    #   layout.prop_enum(scene.ttsConfig,"selectedLibrary", value=config.libraryName)
    # layout.prop(TTSTOSEQUENCER_OT_Player, "text")
    layout.menu(TTSToSequencer_MT_TtsLibrary.bl_idname,text="ライブラリ選択")
    ot = layout.operator(TTSTOSEQUENCER_OT_Player.bl_idname,text="音声を再生")
    # layout.prop_with_menu(scene,"libraryConfigs",text="ライブラリ選択")
    # layout.prop_with_menu(scene,"libraryConfigs",text="ライブラリ選択")
