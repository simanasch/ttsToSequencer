from os import path
def getFileName(filePath):
  return path.splitext( path.basename(filePath))[0]

def getFileExtension(filePath):
  return path.splitext( path.basename(filePath))[1]
