
from PySide.QtCore import *
from PySide.QtGui import *
import sys
from ui import Ui_Mp3TagStripper
import os

__appname__ = "Mp3 Tag Stripper"

class MainDialog(QDialog, Ui_Mp3TagStripper.Ui_MainDialog):

    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)
        self.mp3dir = ''

        self.btnLoadDirectory.setFocus()
        self.btnLoadDirectory.clicked.connect(self.loadDir)


    def loadDir(self):
        dir = "."
        flags = QFileDialog.DontResolveSymlinks | QFileDialog.ShowDirsOnly
        d = QFileDialog.getExistingDirectory(self, __appname__ +
                                             " Open Directory", os.getcwd()
                                             , flags)
        if d != '':
            self.lblDirName.setText(d)
            self.mp3dir = d
            self.getmp3list(d)

    def getmp3list(self, path):
        fileList = []
        if os.path.exists(path):
            for root, dirs, files in os.walk(path):
                for name in files:
                    filename = os.path.join(root,name)
                    if filename.lower().endswith('.mp3'):
                        fileList.append(filename)
        print fileList


app = QApplication(sys.argv)
form = MainDialog()
form.show()
form.raise_()
sys.exit(app.exec_())
