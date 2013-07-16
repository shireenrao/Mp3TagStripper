
from PySide.QtCore import *
from PySide.QtGui import *
import sys
from ui import Ui_Mp3TagStripper
import os

class MainDialog(QDialog, Ui_Mp3TagStripper.Ui_MainDialog):

    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)

app = QApplication(sys.argv)
form = MainDialog()
form.show()
form.raise_()
sys.exit(app.exec_())
