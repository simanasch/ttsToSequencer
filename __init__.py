'''
Copyright (C) 2022 simana
tktossi@live.com

Created by simana

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

bl_info = {
  "name": "tts To Sequencer",
  "author": "simana",
  "version": (0, 0, 1),
  "blender": (2, 93, 3),
  "location": "Sequencer",
  "description": "tts access and saved wav to sequencer",
  "warning": "",
  "doc_url": "",
  "tracker_url": "",
  "category": "Sequencer",
}

# "reload Script"でスクリプトを再読み込みした場合に関連ファイルを再読み込みする
if "bpy" in locals():
  from . import auto_load
  auto_load.reload()

import bpy
try:
  import clr
except ModuleNotFoundError:
  # watchdogがインストールされていない場合、インストールを行う
  print("clr not installed, installing...")
  import sys,subprocess
  subprocess.call([sys.executable, '-m','pip', 'install', 'clr' ])
except Exception as e:
  # subprocessが落ちたらエラー出力
  import logging
  logging.error(e);
from . import auto_load
auto_load.init()

#
# アドオン有効化時の処理
#
def register():
  auto_load.register()
  from .classes.ttsConfig import ttsConfig
  from .classes.libraryConfig import libraryConfig
  bpy.types.Scene.ttsConfig = bpy.props.PointerProperty(type=ttsConfig)
  bpy.types.Scene.libraryConfigs = bpy.props.CollectionProperty(type=libraryConfig)
  # アドオン登録時に音声合成エンジンの一覧を更新する
  # bpy.ops.ttstosequencer.reload_available_tts()


#
# アドオン無効化時の処理
# 
def unregister():
  auto_load.unregister()
  del bpy.types.Scene.ttsConfig
