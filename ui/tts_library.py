import bpy
from ..operators.select_active_tts import TTSTOSEQUENCER_OT_SelectActiveTts

class TTSToSequencer_MT_TtsLibrary(bpy.types.Menu):
  bl_idname = "ttstosequencer.TTS_PT_TtsLibrary"
  bl_label = "tts menu item"
  bl_description = "ttsを選択"

  def draw(self, context):
    layout = self.layout
    # メニュー項目の追加
    scene = context.scene
    for index,library in enumerate(scene.libraryConfigs):
      op = layout.operator(TTSTOSEQUENCER_OT_SelectActiveTts.bl_idname,text=library.libraryName, text_ctxt = library.engineName)
      op.index = index