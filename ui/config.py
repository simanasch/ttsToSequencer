import bpy
from ..operators.reload_active_libraries import TTSTOSEQUENCER_OT_ReloadAvailableTts
from .tts_library import TTSToSequencer_MT_TtsLibrary

# やること:シーケンサの画面のサイドバー上でフォルダ監視の切り替え、
# Listで音声入力の設定をできるようにする
class TTSToSequencer_PT_Config(bpy.types.Panel):
  """tts To SequencerのUI"""
  bl_idName = "ttstosequencer.TTS_PT_Config"
  bl_label= "ttsToSequencer Config"
  bl_space_type="SEQUENCE_EDITOR"
  bl_region_type="UI"
  bl_category="tts"
  bl_label="tts設定"

  def draw(self,context):
    layout = self.layout
    ttsConfig = context.scene.ttsConfig
    scene = context.scene
    layout.operator(TTSTOSEQUENCER_OT_ReloadAvailableTts.bl_idname,text="tts一覧更新")
    layout.prop(ttsConfig, "folder",text="音声保存先フォルダ")
    layout.menu(TTSToSequencer_MT_TtsLibrary.bl_idname,text="ライブラリ選択")
    layout.prop(ttsConfig, "saveTextOnSave",text="録音内容をcsvに保存")
    layout.separator()
    library = scene.libraryConfigs[scene.ttsConfig.selectedLibraryIndex]
    col=layout.column()
    col.alignment='RIGHT'
    engine_row = col.row()
    engine_row.label(text = "ttsエンジン名:")
    engine_row.label(text = library.engineName)
    label_row = col.row()
    label_row.label(text="プリセット名:")
    label_row.label(text = library.libraryName)
    # col.prop(library,"engineName",text="エンジン名")
    col.prop(library,"channel",text="音声追加先チャンネル")
    col.prop(library,"hasSubtitle",text="字幕設定")
    if library.hasSubtitle:
      subtitle=library.subtitleConfig
      col.operator('font.open') 
      col.prop(subtitle, "fontName", text="字幕のフォント")
      col.prop(subtitle,"size", text="字幕のサイズ",slider=True)
      col.prop(subtitle,"wrapWidth",text="ラップ幅")
      col.prop(subtitle,"color", text="字幕の色", slider=True)
      col.prop(subtitle,"position",text="表示位置")
