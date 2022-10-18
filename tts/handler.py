import clr
clr.AddReference("E:/Documents/scripts/addons/ttsToSequencer/bin/Speech.dll")
from Speech import SpeechController

print( SpeechController)
# SpeechControllerでやること
# 起動時(と呼ばれたとき)にttsの一覧を更新する
def getLibraries():
  return SpeechController.GetAllSpeechEngine()

# SoundPlayerでやること
# ファイル名を渡してPlayを呼ぶ
def play(library, text, engine=None):
  ttsEngine = None
  if engine is not None:
    ttsEngine = SpeechController.GetInstance(library, engine)
  else:
    ttsEngine = SpeechController.GetInstance(library)
  if ttsEngine is not None:
    ttsEngine.Activate()
    ttsEngine.Finished += lambda s,a :ttsEngine.Dispose()
    ttsEngine.Play(text)
