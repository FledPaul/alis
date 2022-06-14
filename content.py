# Import Libraries
import json
import time
import os


# 'Alis' Class
class Alis:
    def Run(self):
        # Load Configuration File
        ConfigJson = open('alis.json', 'r+')
        Config = json.load(ConfigJson)
        Updated = Config['updated']

        # Libraries Installed?
        if Updated == False:
            time.sleep(1)
            print()
            Libs = Config['libs'].split(' ')
            CurrentLib = -1

            # Install Libraries
            for i in range(len(Libs)):
                CurrentLib = CurrentLib + 1
                os.system('python3 -m pip install ' + Libs[CurrentLib])

            # Updated = True
            LibsRaw = Config['libs']
            SuccessMsg = Config['success_msg']
            RunPy = Config['run_py']
            UpdatedTrue = {'updated': True, 'libs': LibsRaw, 'success_msg': SuccessMsg, 'run_py': RunPy}

            # Delete Configuration
            ConfigJson.seek(0)
            ConfigJson.truncate()

            # Dump Configuration
            json.dump(UpdatedTrue, ConfigJson, indent = 2)
            print(SuccessMsg)


# Run & Define Alis
Alis = Alis()
Alis.Run()