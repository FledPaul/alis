# Import Libraries
import imp
import sys
import os
import time
import json

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton
from PyQt5.QtCore import QSize
from datetime import date


# Main Windows
class AppWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # GUI Style
        self.setFixedSize(700, 305)
        self.setWindowTitle('Automatic Library Installation Software')
        self.setStyleSheet('background-color: #FFFFFF;')

        # Libraries Input
        self.Libraries = QLineEdit(self)
        self.Libraries.move(35, 35)
        self.Libraries.resize(305, 60)
        self.Libraries.setPlaceholderText('Libraries')
        self.Libraries.setStyleSheet('border: none; border-radius: 20px; background-color: #EEEEEE; color: #606060; padding-left: 10px; font-weight: 500; font-size: 15px;')

        # Python File Input
        self.PyFile = QLineEdit(self)
        self.PyFile.move(360, 35)
        self.PyFile.resize(305, 60)
        self.PyFile.setPlaceholderText('Python File')
        self.PyFile.setStyleSheet('border: none; border-radius: 20px; background-color: #EEEEEE; color: #606060; padding-left: 10px; font-weight: 500; font-size: 15px;')

        # Path Input
        self.PathInput = QLineEdit(self)
        self.PathInput.move(35, 115)
        self.PathInput.resize(305, 60)
        self.PathInput.setPlaceholderText('File Path')
        self.PathInput.setStyleSheet('border: none; border-radius: 20px; background-color: #EEEEEE; color: #606060; padding-left: 10px; font-weight: 500; font-size: 15px;')

        # Success Message Input
        self.SuccessMsg = QLineEdit(self)
        self.SuccessMsg.move(360, 115)
        self.SuccessMsg.resize(305, 60)
        self.SuccessMsg.setPlaceholderText('Success Message')
        self.SuccessMsg.setStyleSheet('border: none; border-radius: 20px; background-color: #EEEEEE; color: #606060; padding-left: 10px; font-weight: 500; font-size: 15px;')

        # Install Function
        def Install():
            # Get Inputs
            Libraries = self.Libraries.text()
            File = self.PyFile.text()
            Path = self.PathInput.text()
            SuccessMsg = self.SuccessMsg.text()

            # Get Current Date
            Date = date.today()
            Date = Date.strftime('%b-%d-%Y')

            # Delete (Existing) Log File
            try:
                os.remove(Date + '.log')
            except FileNotFoundError:
                pass

            # Create Log File
            LogFile = open(Date + '.log', 'a')

            #####################################################

            if len(Libraries) < 1:
                print('Error : No Libraries Given')
                LogFile.write('Error : No Libraries Given\n')
                time.sleep(2)
                exit()
            else:
                print('Success : Libraries Given')
                LogFile.write('Success : Libraries Given\n')


            #####################################################

            # Valid Path => Yes
            if os.path.isdir(Path):
                print('Success : Valid Path')
                LogFile.write('Success : Valid Path\n')
            else:
                print('Error : Invalid Path')
                LogFile.write('Error : Invalid Path\n')
                time.sleep(2)
                exit()

            # Slash Given => Yes/No
            if Path.endswith('/'):
                Slash = ''
            else:
                Slash = '/'

            #####################################################

            # Python File => Yes --- Not Empty => Yes
            if str(File).endswith('.py'):
                print('Success : Python File')
                LogFile.write('Success : Python File\n')
            else:
                print('Error : No Python File')
                LogFile.write('Error : No Python File\n')
                time.sleep(2)
                exit()

            # File Exists => Yes --- Path Exists => Yes
            if os.path.isfile(Path + Slash + File):
                print('Success : Valid File')
                LogFile.write('Success : Valid File\n')
            else:
                print('Error : Invalid File')
                LogFile.write('Error : Invalid File\n')
                time.sleep(2)
                exit()

            #####################################################

            # Create Json File (Given Path)
            try:
                ExtJson = open(Path + Slash + 'alis.json', 'w', encoding='utf-8')
                JsonData = {'updated': False, 'libs': Libraries, 'success_msg': SuccessMsg, 'run_py': File}
                json.dump(JsonData, ExtJson, indent=2)
                print('Success : Json Creation')
                print('Success : Wrote Json Data')
                LogFile.write('Success : Json Creation\n')
                LogFile.write('Success : Wrote Json Data\n')
            except:
                print('Error : Json Creation Failed')
                LogFile.write('Error : Json Creation Failed\n')
                time.sleep(2)
                exit()

            # Create Python File (Given Path)
            try:
                ExtPython = open(Path + Slash + 'run.py', 'w')
                IntPython = open('content.py', 'r')
                # Copy Data
                for Data in IntPython:
                    ExtPython.write(Data)
                print('Success : Python Creation')
                LogFile.write('Success : Python Creation\n')
            except:
                print('Error : Python Creation Failed')
                LogFile.write('Error : Python Creation Failed\n')
                time.sleep(2)
                exit()

            #####################################################

            # Change 'Install' To 'Installed'
            self.InstallBtn.setText('Installed')


        # Install Button
        self.InstallBtn = QPushButton('Install', self)
        self.InstallBtn.move(35, 210)
        self.InstallBtn.resize(630, 60)
        self.InstallBtn.setStyleSheet('border: none; border-radius: 20px; background-color: #006EE6; color: #FFFFFF; font-weight: 500; font-size: 15px;')
        self.InstallBtn.clicked.connect(Install)

# Define & Run
if __name__ == '__main__':
    App = QtWidgets.QApplication(sys.argv)
    AppWindow = AppWindow()
    AppWindow.show()
    sys.exit(App.exec())