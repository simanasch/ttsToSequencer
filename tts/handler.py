import clr
clr.AddReference("E:/Documents/scripts/addons/ttsToSequencer/bin/Speech.dll")
from Speech import SpeechController,SoundRecorder
from ..operators.add_sound_to_sequence import addSoundToSequence

# SpeechControllerでやること
# 起動時(と呼ばれたとき)にttsの一覧を更新する
def getLibraries():
  return SpeechController.GetAllSpeechEngine()

ttsEngine = None
# SoundPlayerでやること
# ファイル名を渡してPlayを呼ぶ
def play(library, text, engine=None):
  global ttsEngine
  if engine is not None:
    ttsEngine = SpeechController.GetInstance(library, engine)
  else:
    ttsEngine = SpeechController.GetInstance(library)
  if ttsEngine is not None:
    ttsEngine.Activate()
    ttsEngine.Finished += lambda s,a :ttsEngine.Dispose()
    ttsEngine.Play(text)

recorder = None

def record(library, text, outputPath, engine=None):
  global ttsEngine
  if engine is not None:
    ttsEngine = SpeechController.GetInstance(library, engine)
  else:
    ttsEngine = SpeechController.GetInstance(library)
  if ttsEngine is not None:
    global recorder
    recorder = SoundRecorder(outputPath)
    recorder.PostWait = 300
    ttsEngine.Activate()
    # finishedの処理内でこっちのコンテキストにあるrecorder.stop()を呼びたい
    # ttsEngine.disposeはsに自身のインスタンスがあるのでできそう
    ttsEngine.Finished += onRecordFinish
    recorder.Start()
    ttsEngine.Play(text)

def onRecordFinish(s,a):
  global ttsEngine
  global recorder
  # print("onRecordFinish")
  # print(str(ttsEngine))
  if recorder is not None:
    recorder.Stop().Wait()
  addSoundToSequence()
  ttsEngine.Dispose()