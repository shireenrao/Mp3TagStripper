
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

        self.btnLoadDirectory.setFocus()
        self.btnLoadDirectory.clicked.connect(self.loadDir)


    def loadDir(self):
        dir = "."
        flags = QFileDialog.DontResolveSymlinks | QFileDialog.ShowDirsOnly
        d = QFileDialog.getExistingDirectory(self, __appname__ +
                                             " Open Directory", os.getcwd()
                                             , flags)
        self.lblDirName.setText(d)

app = QApplication(sys.argv)
form = MainDialog()
form.show()
form.raise_()
sys.exit(app.exec_())
