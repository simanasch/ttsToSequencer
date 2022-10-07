import bpy
from ..operators.observer import TTSTOSEQUENCER_OT_observer

# やること:シーケンサの画面のサイドバー上でフォルダ監視の切り替え、
# Listで音声入力の設定をできるようにする
class TTSToSequencer_PT_UiPanel(bpy.types.Panel):
  """tts To SequencerのUI"""
  bl_idName = "ttstosequencer.TTS_PT_UiPanel"
  bl_label= "ttsToSequencer UI"
  bl_space_type="SEQUENCE_EDITOR"
  bl_region_type="UI"
  bl_category="tts"
  bl_label="tts設定"

  def draw(self,context):
    layout = self.layout
    ttsConfig = context.scene.ttsConfig
    scene = context.scene
    layout.prop(ttsConfig, "folder",text="音声保存先フォルダ")
    # layout.prop(ttsConfig, "isObserverRunning",text="フォルダ監視")
    layout.operator(TTSTOSEQUENCER_OT_observer.bl_idname,depress=ttsConfig.isObserverRunning)
    # print(observer.folder)
    # print(observer.isrecursive)
    # observer.watchFolder = ttsConfig.folder
    layout.separator()
    for library in scene.libraryConfigs:
      col=layout.column()
      col.prop(library,"name",text="ライブラリ名")
      col.prop(library,"fileNamePattern",text="ファイル名正規表現")
      col.prop(library,"channel",text="音声追加先チャンネル")
      col.prop(library,"hasSubtitle",text="字幕")
      if library.hasSubtitle:
        subtitle=library.subtitleConfig
        col.prop(subtitle,"font")
        col.prop(subtitle,"size")
        col.prop(subtitle,"color")
        col.prop(subtitle,"position")
        pass
      removeButton = col.operator("ttstosequencer.remove_library_config")
      removeButton.index = scene.libraryConfigs.find(library.name)
      # pattern = observer.watchRegexList.add()
      # print(pattern)
      col.separator()

    layout.operator("ttstosequencer.add_library_config")