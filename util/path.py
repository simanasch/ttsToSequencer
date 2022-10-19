from os import path
import re
import bpy

def getFileName(filePath):
  return path.splitext( path.basename(filePath))[0]

def getFileExtension(filePath):
  return path.splitext( path.basename(filePath))[1]

def getProjectPath():
  return bpy.path.abspath('//')

def sanitizeFilePath(path):
  return re.sub(r"[\/:*?\"<>|]","_",path )