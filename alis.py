# Import Libraries
import json
import time
import os

# 'Alis' class
class Alis:
  def ReadJson(self):
    # Open Json
    global ConfigJson
    ConfigJson = open('alis.json', 'r+')
    global Config
    Config = json.load(ConfigJson)

  def ReadConfig(self):
    # Installation Required
    if Config['updated'] == False:
      time.sleep(1)
      print()
      global Libs
      Libs = Config['libs'].split(' ')
      global CurrentLib
      CurrentLib = -1
    
  def InstallLibs(self):
    # Install Libraries
    for i in range(len(Libs)):
      CurrentLib = CurrentLib + 1
      os.system('pip install ' + Libs[CurrentLib]

  def UpdateJson(self):
    # New Data + Delete Json
    Updated = {"updated": true, "libs": Config['libs']}
    ConfigJson.seek(0)
    ConfigJson.truncate()
    # Dump Json Data
    json.dump(Updated, ConfigJson, indent=2)
    print(Config['sucess_msg'])

    
# Define & Run Alis
Alis = Alis()
Alis.ReadJson()
Alis.ReadConfig()
Alis.InstallLibs()
Alis.UpdateJson()